#!/usr/bin/env python3
"""Read-only Vite+ discovery. Never imports project code or changes manifests."""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
from functools import lru_cache
import json
import os
from pathlib import Path
import re
import shutil
import stat
import subprocess
import sys


DEFAULT_ROOTS = [r"C:\malei\job", r"C:\malei\stu"]
DEFAULT_FULL_ROOTS = [r"C:\malei\stu\bubbles", r"C:\malei\stu\antv-next-pro",
                      r"C:\malei\stu\workflow", r"C:\malei\stu\i18n"]
LOCKFILES = {"pnpm-lock.yaml", "package-lock.json", "npm-shrinkwrap.json",
             "yarn.lock", "bun.lock", "bun.lockb"}
FILENAMES = LOCKFILES | {"package.json", "pnpm-workspace.yaml"}
EXCLUDED = {"node_modules", ".git", ".hg", ".svn", ".pnpm-store", ".cache",
            ".vite", ".next", ".nuxt", ".output", "coverage", "dist", "build",
            "__pycache__", ".venv", "venv", ".codegraph", ".turbo"}
EXCLUDED_PATHS = {".vitepress/cache", ".yarn/cache"}
VP_PACKAGES = {"vite-plus", "@voidzero-dev/vite-plus-core"}
VP_ALIAS = re.compile(r"^npm:(?:vite-plus|@voidzero-dev/vite-plus-core)(?:@|$)")
VP_COMMAND = re.compile(r"(?<![\w./:@-])(?:vp|vpr|vpx)(?:\.cmd)?(?=\s|[;&|]|$)")
YAML_ENTRY = re.compile(r'''^( *)(?:'([^']+)'|"([^"]+)"|([^:#][^:]*)):\s*(.*)$''')


def absolute(value: str | Path) -> Path:
    return Path(os.path.abspath(value))


def inside(path: Path, parent: Path) -> bool:
    try:
        return os.path.normcase(os.path.commonpath([path, parent])) == os.path.normcase(str(parent))
    except ValueError:
        return False


def is_link(path: Path) -> bool:
    info = path.lstat()
    return stat.S_ISLNK(info.st_mode) or bool(
        getattr(info, "st_file_attributes", 0) & stat.FILE_ATTRIBUTE_REPARSE_POINT
    )


def discover_files(roots: list[Path], errors: list[dict]) -> tuple[list[Path], str]:
    """rg does not follow links by default; the fallback also skips reparse points."""
    valid = []
    for root in roots:
        try:
            if is_link(root) or not root.is_dir():
                raise ValueError("scan root must be a real directory, not a link")
            valid.append(root)
        except (OSError, ValueError) as exc:
            errors.append({"path": str(root), "error": str(exc)})
    if not valid:
        return [], "none"

    if shutil.which("rg"):
        command = ["rg", "--files", "--hidden", "--no-ignore", "--null"]
        for name in sorted(FILENAMES):
            command.extend(["-g", name])
        for name in sorted(EXCLUDED | EXCLUDED_PATHS):
            command.extend(["-g", f"!**/{name}/**"])
        command.extend(str(root) for root in valid)
        result = subprocess.run(command, capture_output=True, check=False)
        stderr = result.stderr.decode("utf-8", errors="replace").strip()
        if stderr or result.returncode not in (0, 1):
            errors.append({"path": "rg", "error": stderr or f"exit {result.returncode}"})
        paths = {absolute(os.fsdecode(item)) for item in result.stdout.split(b"\0") if item}
        # A linked manifest file is not followed either.
        accepted = []
        for path in paths:
            try:
                if not is_link(path):
                    accepted.append(path)
            except OSError as exc:
                errors.append({"path": str(path), "error": str(exc)})
        return sorted(accepted, key=lambda p: str(p).casefold()), "rg"

    found = set()

    def walk_error(exc: OSError) -> None:
        errors.append({"path": str(exc.filename), "error": str(exc)})

    for root in valid:
        for directory, dirs, files in os.walk(root, followlinks=False, onerror=walk_error):
            parent = Path(directory)
            retained = []
            for name in dirs:
                path = parent / name
                if name in EXCLUDED or any(path.as_posix().endswith("/" + x) for x in EXCLUDED_PATHS):
                    continue
                try:
                    if not is_link(path):
                        retained.append(name)
                except OSError as exc:
                    walk_error(exc)
            dirs[:] = retained
            for name in FILENAMES.intersection(files):
                path = parent / name
                try:
                    if not is_link(path):
                        found.add(path)
                except OSError as exc:
                    walk_error(exc)
    return sorted(found, key=lambda p: str(p).casefold()), "os.walk"


def dependency_hit(key: str, value: object) -> bool:
    return isinstance(value, str) and (key in VP_PACKAGES or bool(VP_ALIAS.match(value)))


def yaml_declarations(path: Path, source: str) -> list[dict]:
    """Conservative pnpm block-scalar extraction, not a general YAML parser."""
    result = []
    parents: list[tuple[int, str]] = []
    for line_number, line in enumerate(source.splitlines(), 1):
        match = YAML_ENTRY.match(line)
        if not match:
            continue
        indent = len(match[1])
        key = (match[2] or match[3] or match[4]).strip()
        while parents and parents[-1][0] >= indent:
            parents.pop()
        value = match[5].strip()
        context = [entry[1] for entry in parents]
        if not value or value.startswith("#"):
            parents.append((indent, key))
            continue
        if value.startswith(("'", '"')):
            quote = value[0]
            closing = value.find(quote, 1)
            value = value[1:closing] if closing > 0 else value
        else:
            value = re.split(r"\s+#", value, maxsplit=1)[0].strip()
        if (context and context[0] in {"catalog", "catalogs", "overrides"}
                and dependency_hit(key, value) and value.lower() not in {"true", "false", "null"}):
            result.append({"file": str(path), "key": ".".join(context + [key]),
                           "spec": value, "line": line_number,
                           "kind": "workspace-scalar-candidate"})
    return result


def build_inventory(roots: list[Path], full_roots: list[Path]) -> dict:
    errors: list[dict] = []
    paths, scanner = discover_files(roots, errors)
    markers = set(paths)
    manifests: dict[Path, dict] = {}
    hits: dict[Path, list[dict]] = {}
    hints: dict[Path, list[dict]] = {}
    yaml_reviews = []
    for path in paths:
        if path.name not in {"package.json", "pnpm-workspace.yaml"}:
            continue
        try:
            source = path.read_text(encoding="utf-8-sig")
            if path.name == "pnpm-workspace.yaml":
                declarations = yaml_declarations(path, source)
                if declarations:
                    hits[path] = declarations
                # Any Vite+ workspace config needs semantic review, including flow YAML.
                if re.search(r"(?:\bvite-plus\b|@voidzero-dev/vite-plus-core)", source):
                    yaml_reviews.append(str(path))
                continue
            data = json.loads(source)
            if not isinstance(data, dict):
                raise ValueError("package.json root is not an object")
            manifests[path.parent] = data
            declarations = []
            for section in ("dependencies", "devDependencies", "optionalDependencies", "peerDependencies"):
                values = data.get(section, {})
                if not isinstance(values, dict):
                    raise ValueError(f"{section} is not an object")
                for key, value in values.items():
                    if dependency_hit(key, value):
                        declarations.append({"file": str(path), "key": f"{section}.{key}",
                                             "spec": value, "kind": "dependency"})
            if declarations:
                hits[path] = declarations
            script_hits = []
            scripts = data.get("scripts", {})
            if isinstance(scripts, dict):
                for name, command in scripts.items():
                    if isinstance(command, str) and (VP_COMMAND.search(command) or "node_modules/vite-plus" in command.replace("\\", "/")):
                        script_hits.append({"file": str(path), "script": name, "command": command})
            if script_hits:
                hints[path] = script_hits
        except (OSError, ValueError) as exc:
            errors.append({"path": str(path), "error": str(exc)})

    @lru_cache(maxsize=None)
    def repository_root(directory: Path) -> Path | None:
        for parent in (directory, *directory.parents):
            if os.path.lexists(parent / ".git"):
                return parent
        return None

    @lru_cache(maxsize=None)
    def installation_root(directory: Path) -> Path:
        boundary = repository_root(directory)
        for parent in (directory, *directory.parents):
            if (parent / "pnpm-workspace.yaml" in markers
                    or any(parent / lock in markers for lock in LOCKFILES)
                    or manifests.get(parent, {}).get("workspaces")):
                return parent
            if parent == boundary:
                break
            # Do not infer workspace ownership from directories outside scan roots.
            if not any(inside(parent, root) for root in roots):
                break
        return directory

    grouped: dict[Path, dict] = {}
    for path in sorted(hits.keys() | hints.keys(), key=lambda p: str(p).casefold()):
        unit = installation_root(path.parent)
        repo = repository_root(unit)
        project = grouped.setdefault(unit, {
            "path": str(unit), "repository_root": str(repo) if repo else None,
            "mode": "all-dependencies" if any(inside(unit, root) for root in full_roots) else "vite-plus-only",
            "members": [], "declarations": [], "script_hints": [],
            "lockfiles": [str(unit / lock) for lock in sorted(LOCKFILES) if unit / lock in markers],
        })
        if str(path.parent) not in project["members"]:
            project["members"].append(str(path.parent))
        project["declarations"].extend(hits.get(path, []))
        project["script_hints"].extend(hints.get(path, []))
    projects = [p for p in grouped.values() if p["declarations"]]
    candidates = [p for p in grouped.values() if not p["declarations"]]
    full_upgrades = []
    for full_root in full_roots:
        full_members = [directory for directory in manifests if inside(directory, full_root)]
        full_units = sorted({str(installation_root(directory)) for directory in full_members}, key=str.casefold)
        full_upgrades.append({"path": str(full_root), "manifest_count": len(full_members),
                              "installation_units": full_units})
    declared_files = set(str(path) for path in hits)
    return {
        "scanned_at": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
        "roots": [str(p) for p in roots], "full_upgrade_roots": [str(p) for p in full_roots],
        "scanner": scanner, "manifest_count": len(manifests),
        "full_upgrades": full_upgrades,
        "projects": projects, "script_only_candidates": candidates,
        "workspace_files_for_review": yaml_reviews,
        "workspace_only_review_candidates": [p for p in yaml_reviews if p not in declared_files and not any(
            str(Path(p).parent) in project["members"] for project in projects)],
        "errors": errors,
        "notes": ["Installation roots are candidates: verify workspace membership before updating.",
                  "Workspace YAML uses conservative block-scalar extraction; review listed YAML files for aliases, anchors and flow mappings.",
                  "No project code was executed; lockfile content is not used as evidence of direct Vite+ use."],
    }


def markdown(report: dict) -> str:
    def cell(value: object) -> str:
        return str(value).replace("|", "\\|").replace("\n", " ")

    def link(value: str) -> str:
        return f"[{cell(value)}](<{Path(value).as_posix()}>)"

    counts = Counter(p["mode"] for p in report["projects"])
    other_repos = {p["repository_root"] for p in report["projects"] if p["mode"] == "vite-plus-only" and p["repository_root"]}
    lines = ["# 项目依赖升级扫描清单", "", f"扫描时间：{report['scanned_at']}。本轮只读扫描，没有执行安装或升级。", "",
             f"共解析 {report['manifest_count']} 个 package.json；发现 {len(report['projects'])} 个有 Vite+ 声明的安装单元候选，其中全依赖范围内 {counts['all-dependencies']} 个，仅升级 Vite+ 范围内 {counts['vite-plus-only']} 个（{len(other_repos)} 个 Git 根目录）。",
             f"仅脚本候选 {len(report['script_only_candidates'])} 个；待补充检查的 workspace 候选 {len(report['workspace_only_review_candidates'])} 个；扫描错误 {len(report['errors'])} 个。", "",
             "工作空间 YAML 按常见块状标量提取，完整列表见 JSON 的 workspace_files_for_review；需复核锚点、别名和 flow 写法。安装根也需核对 workspace 成员及嵌套仓库，不能直接把数量视为独立 Git 仓库数。", "",
             "## 全部兼容依赖升级范围", "",
             "以下项目的工作空间成员和独立模板均检查全部依赖，包括未使用 Vite+ 的包。", ""]
    for full_upgrade in report["full_upgrades"]:
        lines += [f"### {Path(full_upgrade['path']).name}", "",
                  f"范围：{link(full_upgrade['path'])}；包含 {full_upgrade['manifest_count']} 个 manifest、{len(full_upgrade['installation_units'])} 个安装单元候选。", ""]
        lines.extend(f"- {link(unit)}" for unit in full_upgrade["installation_units"])
        lines.append("")
    for mode, title in (("all-dependencies", "全依赖范围内使用 Vite+ 的安装单元"), ("vite-plus-only", "其余项目：仅升级 Vite+")):
        lines += ["", f"## {title}", "", "| 安装单元候选 | 当前声明 | Git 根目录 |", "| --- | --- | --- |"]
        for project in report["projects"]:
            if project["mode"] != mode:
                continue
            specs = sorted({f"{item['key']} = {item['spec']}" for item in project["declarations"]})
            repo = link(project["repository_root"]) if project["repository_root"] else "未发现"
            lines.append(f"| {link(project['path'])} | {cell('; '.join(specs))} | {repo} |")
    lines += ["", "## 仅脚本候选", "", "这些目录有 vp／vpr／vpx 脚本，尚未确认本地 Vite+ 依赖；不能自动补依赖或升级全局 CLI。", ""]
    lines += [f"- {link(p['path'])}" for p in report["script_only_candidates"]] or ["无。"]
    lines += ["", "## Workspace 额外候选", ""]
    lines += [f"- {link(p)}：有 Vite+ 文本，未提取到可确认声明，需人工复核。" for p in report["workspace_only_review_candidates"]] or ["无。"]
    lines += ["", "## 扫描错误", ""]
    lines += [f"- {cell(e['path'])}：{cell(e['error'])}" for e in report["errors"]] or ["无。"]
    lines += ["", "本文件是最近一次扫描的定位快照；每次升级前重新扫描。完整声明、脚本和锁文件路径见同目录 project-inventory.json。", ""]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--roots", nargs="+", default=DEFAULT_ROOTS)
    parser.add_argument("--full-upgrade-roots", "--full-upgrade-root", nargs="+", default=DEFAULT_FULL_ROOTS)
    parser.add_argument("--output", required=True, type=Path, help="JSON output outside project manifests")
    parser.add_argument("--markdown", type=Path, help="Optional Markdown inventory")
    args = parser.parse_args()
    roots = sorted({absolute(root) for root in args.roots}, key=lambda p: str(p).casefold())
    # Do not visit overlapping roots twice.
    roots = [root for root in roots if not any(root != other and inside(root, other) for other in roots)]
    outputs = [absolute(p) for p in (args.output, args.markdown) if p]
    if len(outputs) != len(set(outputs)) or any(p.name in FILENAMES for p in outputs):
        parser.error("outputs must be distinct report files, never project manifests or lockfiles")
    for output in outputs:
        output.parent.mkdir(parents=True, exist_ok=True)
    full_roots = sorted({absolute(root) for root in args.full_upgrade_roots}, key=lambda p: str(p).casefold())
    full_roots = [root for root in full_roots if not any(root != other and inside(root, other) for other in full_roots)]
    report = build_inventory(roots, full_roots)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.markdown:
        args.markdown.write_text(markdown(report), encoding="utf-8")
    print(json.dumps({"manifests": report["manifest_count"], "projects": len(report["projects"]),
                      "modes": dict(Counter(p["mode"] for p in report["projects"])),
                      "script_only_candidates": len(report["script_only_candidates"]),
                      "workspace_only_review_candidates": len(report["workspace_only_review_candidates"]),
                      "errors": len(report["errors"]), "output": str(absolute(args.output))}))
    return 2 if report["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())

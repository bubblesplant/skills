#!/usr/bin/env node
import { writeFile } from "node:fs/promises";
import { execFile } from "node:child_process";
import { get } from "node:https";
import { dirname, resolve } from "node:path";
import { promisify } from "node:util";
import { fileURLToPath } from "node:url";

const DEFAULT_URL =
  "https://developer.bjblackhole.com/api/developercenter/Doc/DocItem/list/bydcid?dcid=3a0b9cac-880a-697b-9bf4-6328c4b94612";

const execFileAsync = promisify(execFile);
const skillRoot = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const defaultOut = resolve(skillRoot, "references", "upgrade-notes.md");

function parseArgs(argv) {
  const options = {
    url: DEFAULT_URL,
    out: defaultOut,
    dryRun: false,
  };

  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === "--dry-run") {
      options.dryRun = true;
    } else if (arg === "--url") {
      options.url = argv[++i];
    } else if (arg === "--out") {
      options.out = resolve(argv[++i]);
    } else if (!arg.startsWith("--")) {
      options.url = arg;
    } else {
      throw new Error(`Unknown argument: ${arg}`);
    }
  }

  return options;
}

function requestText(url, redirects = 0) {
  return new Promise((resolvePromise, reject) => {
    const req = get(
      url,
      {
        headers: {
          Accept: "application/json",
          "User-Agent": "blackhole-engine-api-query-skill",
        },
      },
      (res) => {
        const status = res.statusCode ?? 0;
        const location = res.headers.location;
        if ([301, 302, 303, 307, 308].includes(status) && location) {
          res.resume();
          if (redirects >= 5) {
            reject(new Error("Too many redirects while fetching upgrade notes."));
            return;
          }
          resolvePromise(requestText(new URL(location, url).toString(), redirects + 1));
          return;
        }

        let body = "";
        res.setEncoding("utf8");
        res.on("data", (chunk) => {
          body += chunk;
        });
        res.on("end", () => {
          if (status < 200 || status >= 300) {
            reject(new Error(`HTTP ${status}: ${body.slice(0, 200)}`));
            return;
          }
          resolvePromise(body);
        });
      },
    );
    req.on("error", reject);
    req.end();
  });
}

async function requestTextWithCurl(url) {
  const executable = process.platform === "win32" ? "curl.exe" : "curl";
  const { stdout } = await execFileAsync(
    executable,
    ["-L", "--fail", "--silent", "--show-error", "--header", "Accept: application/json", url],
    {
      encoding: "utf8",
      maxBuffer: 20 * 1024 * 1024,
    },
  );
  return stdout;
}

async function fetchText(url) {
  try {
    return await requestText(url);
  } catch (error) {
    if (error && typeof error === "object" && "code" in error && error.code === "EACCES") {
      return requestTextWithCurl(url);
    }
    throw error;
  }
}

function htmlToMarkdown(value) {
  return String(value ?? "")
    .replace(/\r\n/g, "\n")
    .replace(/\r/g, "\n")
    .replace(/<br\s*\/?>/gi, "\n")
    .replace(/<\/?font[^>]*>/gi, "")
    .replace(/&nbsp;/g, " ")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&amp;/g, "&")
    .trim();
}

function releaseDate(record) {
  const title = String(record.secondTitle ?? "");
  const match = title.match(/(\d{4})[.\-/](\d{1,2})[.\-/](\d{1,2})/);
  if (match) {
    const [, year, month, day] = match;
    return `${year}-${month.padStart(2, "0")}-${day.padStart(2, "0")}`;
  }

  const displayTime = String(record.displayTime ?? "");
  if (/^\d{4}-\d{2}-\d{2}/.test(displayTime)) {
    return displayTime.slice(0, 10);
  }

  return "unknown-date";
}

function sdkVersion(record) {
  const title = String(record.title ?? "").trim();
  if (!title) {
    return "SDK_unknown";
  }
  return title.startsWith("SDK_") ? title : `SDK_${title}`;
}

function apiReferenceFilename(record) {
  const version = sdkVersion(record)
    .replace(/^SDK_/i, "")
    .replace(/^v/i, "v");
  return `BlackHole Engine API_Web-${version}.md`;
}

function sortRecords(records) {
  return [...records].sort((a, b) => {
    const aOrder = Number.isFinite(Number(a.order)) ? Number(a.order) : 0;
    const bOrder = Number.isFinite(Number(b.order)) ? Number(b.order) : 0;
    if (aOrder !== bOrder) {
      return aOrder - bOrder;
    }
    return String(b.displayTime ?? "").localeCompare(String(a.displayTime ?? ""));
  });
}

function renderNotes(records, sourceUrl) {
  const sorted = sortRecords(records);
  const latest = sorted[0];
  const lines = [
    "# BlackHole Engine SDK Upgrade Notes",
    "",
    `Source API: ${sourceUrl}`,
    "",
    "This file is generated from the official update-note API. Use it for SDK upgrade, compatibility, bug-fix, and migration notes. The API Markdown reference is maintained as latest-only because BlackHole Engine APIs are expected to be backward-compatible.",
    "",
    "When a user reports an SDK error, upgrade regression, changed behavior, missing API, runtime exception, initialization problem, or version-specific bug, search this file before answering.",
    "",
    "## Current Latest",
    "",
    `- SDK: \`${sdkVersion(latest)}\``,
    `- Release date: \`${releaseDate(latest)}\``,
    `- API reference: \`${apiReferenceFilename(latest)}\``,
    "",
    "## Upgrade Notes",
    "",
  ];

  for (const record of sorted) {
    const version = sdkVersion(record);
    lines.push(`### ${version} - ${releaseDate(record)}`);
    lines.push("");
    if (record.secondTitle) {
      lines.push(`- Title: ${htmlToMarkdown(record.secondTitle)}`);
    }
    if (record.accessory) {
      lines.push(`- SDK package: \`${record.accessory}\``);
    }
    if (record.operationManual) {
      lines.push(`- API manual: \`${record.operationManual}\``);
    }
    lines.push("");
    lines.push(htmlToMarkdown(record.content) || "No update content provided.");
    lines.push("");
  }

  lines.push("## Maintenance Rule");
  lines.push("");
  lines.push("- Keep only the latest full API reference Markdown file.");
  lines.push("- Do not keep full historical API Markdown snapshots.");
  lines.push("- Refresh this file from the source API when the user asks about recent/latest updates or SDK-specific errors.");
  lines.push("- If the latest API reference lacks details for a newly added interface, say the interface is listed in upgrade notes but the detailed API section is not present in the bundled API reference.");
  lines.push("");

  return lines.join("\n");
}

const options = parseArgs(process.argv.slice(2));
const body = await fetchText(options.url);
const payload = JSON.parse(body);
if (payload.isSuccess === false) {
  throw new Error(payload.errMsg || "Upgrade-note API returned isSuccess=false.");
}

const records = Array.isArray(payload.data) ? payload.data : [];
if (records.length === 0) {
  throw new Error("Upgrade-note API returned no data records.");
}

const markdown = renderNotes(records, options.url);
if (options.dryRun) {
  console.log(`Fetched ${records.length} upgrade-note records.`);
  console.log(`Latest: ${sdkVersion(sortRecords(records)[0])} (${releaseDate(sortRecords(records)[0])})`);
} else {
  await writeFile(options.out, markdown, "utf8");
  console.log(`Wrote ${records.length} upgrade-note records to ${options.out}`);
}

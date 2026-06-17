---
name: manage-prefixed-schedules
description: "Manage scheduled reminders, notifications, and scheduled tasks that are constrained to an AI-owned namespace or prefix across Windows, macOS, and Linux. Use when the user asks to create, view, inspect, update, delete, or audit reminders, notifications, scheduled tasks, planned notifications, or reminder lists that belong to the AI-managed scope. Do not manage unrelated system tasks."
---

# Manage Prefixed Scheduled Notifications

## Scope

Use this skill only for scheduled reminders, notifications, and scheduled tasks that belong to the AI-owned namespace below.

This skill defines boundaries and naming rules only. It does not provide exact command recipes. Choose the appropriate native scheduler, notification, and inspection mechanism for the current operating system.

If this skill or adjacent metadata appears garbled when read, reread it as UTF-8 and confirm the content before acting.

## Default Execution Rules

- When the user asks for a reminder, notification, or planned notification and does not explicitly request the current Codex conversation, create an operating-system user-level scheduled task plus a real system notification by default. Do not substitute a Codex app heartbeat or a chat-only reminder.
- Use a Codex app thread heartbeat only when the user explicitly asks for a current-conversation reminder, to continue this thread later, or for a heartbeat.
- When the user asks for a notification, use the platform's native notification capability. If native notifications are unavailable, use a clearly visible local fallback notification and explain the fallback.
- Before creating or updating a reminder, confirm the current date, time, and time zone. Parse formats such as `11.58` and `11:58` as local `HH:mm`. If the user omits the date and the time has not passed today, use today. If the time has already passed, ask whether they mean a catch-up run today, tomorrow, or another date.
- During a create request, if in-scope reminders have not already been queried or listed in the current turn, inspect `AI-Reminders` / `AI-Reminder-*` resources for expired reminders. Expired means a one-time reminder whose scheduled time is in the past, or a scheduled task with no future run after its scheduled time has passed. If expired reminders exist, show them in a Markdown table and ask whether the user wants to delete them. Do not delete expired reminders without explicit user confirmation unless the user already asked for deletion.
- If scheduler or notification access is blocked by permissions or sandboxing, request the required permission. Do not silently switch to a reminder mechanism that does not satisfy the user's request.

## Namespace

Always use these names:

- Owner namespace: `AI-Reminders`
- Resource prefix: `AI-Reminder-`
- Generated ID format: `AI-Reminder-<stable-id>`

When the platform supports scheduler folders, groups, labels, unit names, comments, descriptions, or metadata, use the owner namespace and resource prefix to mark resources.

Platform naming guidance:

- Windows: when available, use `AI-Reminders` as the scheduled task container namespace; task names must start with `AI-Reminder-`.
- macOS: launch labels, file names, or scheduler metadata must start with `AI-Reminder-` or clearly include `AI-Reminders`.
- Linux: user-level scheduler resources, unit names, job names, comments, or metadata must start with `AI-Reminder-` or clearly include `AI-Reminders`.

Windows implementation guidance:

- PowerShell scripts launched by Task Scheduler must be parse-safe under Windows PowerShell 5.1. Prefer ASCII-only executable script text, or save UTF-8 with BOM if non-ASCII literals are unavoidable.
- Do not put localized reminder text directly into a BOM-less `.ps1` file. Pass localized title/message text through task arguments or metadata instead.
- Do not rely only on Windows toast notifications, because toast requests can fail or be invisible depending on AppUserModelID/session behavior. Include a clearly visible fallback such as a timed `WScript.Shell.Popup`, and write a small log file with success/failure details.
- After creating or changing a Windows reminder script, run the exact script/action with a short harmless test or otherwise verify that it exits with code `0` before relying on the scheduled time.
- Treat generated helper files such as the reminder `.ps1`, `.log`, and `.json` as owned adjacent artifacts for that reminder. Never treat platform binaries such as `powershell.exe`, `schtasks.exe`, shell interpreters, or shared runtime files as owned artifacts.

## Safety Rules

- Manage only resources that are clearly intended for scheduled reminders and clearly belong to this namespace or prefix.
- Do not create, update, disable, enable, or delete unrelated scheduled task resources.
- Do not operate on broad scheduler paths, all jobs, all startup items, vendor update tasks, security software tasks, browser update tasks, or operating-system-managed tasks.
- Treat any resource without the `AI-Reminder-` prefix or `AI-Reminders` namespace as out of scope.
- If the user asks to modify a task that does not clearly belong to this scope, explain that this skill only manages prefixed reminder resources.
- Prefer user-level scheduled tasks rather than system-level tasks unless the user explicitly asks for system-level tasks and understands the permission implications.
- Before destructive operations such as delete, overwrite, or disable, confirm the exact resource name or ID.

## Create, List, View, Update, Delete, Audit

Create:

- If the current turn has not already listed or queried in-scope reminders, check for expired owned reminders while creating the new one. The expired-reminder table should include at least: ID, title or purpose, scheduled time, last run, execution result, platform resource, and metadata status.
- Generate a stable ID with the `AI-Reminder-` prefix.
- Store enough information in the scheduled task resource or adjacent metadata for later lookup, including title, message, time, recurrence rule, user intent, generated helper script path, log path, and metadata path when those artifacts exist.
- When the platform supports it, enable catch-up behavior for missed times so reminders can still run after restart.
- After creation, verify that the underlying platform resource exists, then report the reminder ID, platform resource name, notification method, and scheduled time to the user.

List:

- Return only resources that match this namespace or prefix.
- Include, where possible, ID, title or purpose, scheduled time, recurrence rule, enabled state, and underlying platform resource name.
- When the user asks to view, list, or query planned notifications, return the result as a Markdown table. The table must include at least: ID, title or purpose, scheduled time, recurrence rule, state, next run, last run, platform resource, and notification method or execution result.
- If no matching resources exist, return a clear no-results statement and do not list unrelated system tasks.

View:

- Inspect only the specified prefixed resource.
- If metadata and scheduler resources disagree, report the mismatch clearly.
- For a single resource view, prefer a Markdown table for key fields, followed by any mismatch, permission limit, or execution failure details.

Update:

- Preserve the stable ID when possible.
- Modify only matching prefixed resources and their owned metadata.
- Recreate an owned resource only when in-place updates are unsafe or unsupported by the platform.

Delete:

- Delete only the exact prefixed resource specified by the user.
- If owned adjacent artifacts exist for that exact resource, delete them as well. Owned adjacent artifacts include metadata files, generated helper scripts or small executables created specifically for that reminder, and that reminder's log files.
- Before deleting adjacent artifacts, verify that each file is clearly owned by the exact reminder ID, either because its name starts with the exact ID or because trusted metadata for that exact ID points to it. Do not delete broad directories, wildcard matches outside the owned artifact set, shared helper programs, platform binaries, shell interpreters, or unrelated files.
- Report both the deleted scheduler resource and the deleted adjacent artifacts.
- Do not affect unrelated platform resources.

Audit:

- Check for orphaned metadata or orphaned scheduled task resources only within the `AI-Reminders` namespace or `AI-Reminder-` prefix.
- Provide repair suggestions or repair actions only for owned resources.

## User Communication

Reply in the user's language. When reporting a creation or change, include the reminder ID and the corresponding platform resource name. If the current environment cannot safely access the scheduler or notification system, explain the blocker and the required permission or session context.

Query responses must use tables. Create, update, and delete responses may use short prose, but must still include the ID and platform resource name.

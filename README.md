# Weekly Updates — Irondale Marching Knights

Archive of IHSMK weekly updates and event insteps, converted to Markdown for easy reading, diffing, and searching on GitHub.

## Structure

- `updates/` — Weekly updates, one file per issue, named `YYYY-MM-DD.md` (sorted chronologically)
- `insteps/` — Performance itineraries ("Insteps") for the season
- `slack_post_formatting_guide.md` — Formatting conventions for the weekly Slack DM
- `IHSMK_header.png` — Band header image

## Conventions

All documents are Markdown (`.md`), not PDF. Source PDFs are published on [irondalebands.org](https://www.irondalebands.org) and can be re-downloaded from there if the original fixed-layout versions are needed. Hyperlinks from the original PDFs are preserved inline.

## Automation

A scheduled task ("Irondale weekly update check") runs hourly on Wednesdays. It checks irondalebands.org for a new weekly update, converts it to Markdown, commits it to `updates/`, and DMs Derek a formatted draft. Derek reviews the DM and copy/pastes it into the real Announcements channel by hand — there is no automated posting step.

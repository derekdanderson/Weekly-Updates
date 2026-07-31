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

### Insteps change detection

Unlike weekly updates (a new file each week), an Instep is tied to a specific event and may be revised in place on irondalebands.org after its initial posting — the source PDF's URL doesn't change, only its content. The site doesn't reliably expose trustworthy `Last-Modified` data, so change detection uses a content hash of the source PDF instead of a date.

`insteps/.checksums.json` tracks the last known state of each Instep's source PDF:

```json
{
  "stockyard-days": {
    "source_url": "https://www.irondalebands.org/uploads/.../instep_stockyard_days.pdf",
    "sha256": "...",
    "last_checked": "2026-07-30"
  }
}
```

On each run: fetch the current PDF, compute its SHA-256, and compare to the stored value for that key. Only reprocess and recommit the corresponding `insteps/*.md` file if the hash differs or the entry doesn't exist yet. Always update `last_checked` regardless of whether the content changed.

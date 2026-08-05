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

A separate scheduled task checks irondalebands.org for new or revised Insteps (see below).

### Scraping the listing pages — don't use WebFetch

Both `insteps.html` and `weekly-updates.html` are plain listing pages with PDF `<a href>` links. `WebFetch`'s summarization step has been observed fabricating a link (returned a `zeffy.com` domain that appears nowhere in the actual HTML). Since these links determine what gets downloaded and committed, always get them directly instead:

```bash
curl -sL -A "Mozilla/5.0" "https://www.irondalebands.org/insteps.html" | grep -oE 'href="[^"]*\.pdf"'
```

### Change detection (Insteps and Weekly Updates)

Both routines track source-PDF state in a `.checksums.json` file (`insteps/.checksums.json`, `updates/.checksums.json`) so a run doesn't have to reprocess a PDF it's already seen:

```json
{
  "stockyard-days": {
    "source_url": "https://www.irondalebands.org/uploads/.../instep_stockyard_days.pdf",
    "etag": "6256c13c8f5b6a0720910b10b0d16944",
    "sha256": "...",
    "last_checked": "2026-07-30"
  }
}
```

Check order, cheapest first:

1. **ETag pre-check.** `curl -sI` the source URL and compare the `etag` response header to the stored value. The site returns a stable ETag per file. If it matches, skip the download entirely and just refresh `last_checked`.
2. **SHA-256 fallback.** If the ETag differs, is missing from the stored entry, or the server doesn't return one, download the PDF and compare its SHA-256 to the stored value — this is the authoritative check, since an ETag match/mismatch isn't a cryptographic guarantee. Only reprocess and recommit the corresponding Markdown file if the hash differs or the entry doesn't exist yet.

Always update `last_checked` and the stored `etag`/`sha256` after a run, regardless of whether the content changed.

An Instep is tied to a specific event and may be revised in place on irondalebands.org after its initial posting — the source PDF's URL doesn't change, only its content — so `insteps/.checksums.json` is keyed by event slug and checked every run. Weekly updates get a new dated URL each week, so `updates/.checksums.json` is keyed by issue date (`YYYY-MM-DD`); its main value is catching the (rare) case where that week's PDF is corrected in place at the same URL after already being committed. The site doesn't reliably expose trustworthy `Last-Modified` data, which is why both use ETag/hash instead of a date comparison.

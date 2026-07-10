# IHSMK Weekly Update — Slack Post Formatting Guide

## Overview

This guide covers formatting rules for converting the Irondale Marching Knights weekly update — published as a PDF at irondalebands.org, and archived as Markdown at `updates/YYYY-MM-DD.md` in the derekdanderson/Weekly-Updates repo — into a Slack post.

There is one delivery method: a single DM to Derek via the `slack_send_message` MCP tool, containing **two versions of the same post**:

1. A **rendered preview**, using standard markdown (`**bold**`), so it displays properly right in the DM for Derek to proofread
2. A **copy-paste block**, fenced in a code block (` ``` `) and written in real Slack mrkdwn (`*bold*`, `<url|text>` links) — code blocks pass through untouched by markdown parsing, so this is exactly what Slack's compose box needs when Derek pastes it into the Announcements channel by hand

Derek reviews the preview, copies the code-block version, and posts it to the real channel himself. There is no automated posting step and no separate script — `send_update.py` has been removed.

---

## Workflow

- Happens every Wednesday (scheduled task "Irondale weekly update check" runs hourly on Wednesdays)
- Fetch the newest weekly update PDF from irondalebands.org and use WebFetch/the pdf skill to extract content and hyperlinks
- No local download needed — the scheduled task runs fully remotely. Dedupe and archival live in the derekdanderson/Weekly-Updates GitHub repo (`updates/YYYY-MM-DD.md`, Markdown)
- Build both versions of the post (preview + mrkdwn copy-paste block, see Overview) and send them together in one DM to Derek (user ID: `U03FHQD6MBN`, channel: `D03FFDGPD6W`) — he reviews and posts to the real channel himself

---

## Post Structure

Same structure for both the preview and the copy-paste block:

```
[Header]
[Subtitle — linked to PDF]
[Important Dates]
[Section 1]
[Section 2]
...
[Section N]
```

---

## Header

```
:ihsmk_knight: IRONDALE MARCHING KNIGHTS :ihsmk_knight:
Weekly Update – [Date]  ← linked to PDF URL
```

- `:ihsmk_knight:` emoji flanks the org name only — not the subtitle
- The "Weekly Update – [Date]" line links to the original PDF on irondalebands.org (the public source)

**Preview (standard markdown):**
```
:ihsmk_knight: **IRONDALE MARCHING KNIGHTS** :ihsmk_knight:
**[Weekly Update – May 20, 2026](PDF_URL)**
```

**Copy-paste block (Slack mrkdwn):**
```
:ihsmk_knight: *IRONDALE MARCHING KNIGHTS* :ihsmk_knight:
*<PDF_URL|Weekly Update – May 20, 2026>*
```

---

## Important Dates

Always placed directly under the header, before the first section. The label links to the Irondale Bands calendar.

**Preview syntax:**
```
**[Important Dates](https://www.irondalebands.org/calendar.html):**
• **Thursday, May 21** — Uniform Measurement Night (5:30–7:00pm)
• **Saturday, June 6** — All Forms Due, June Camp Day
```

- Scan the full update and compile all key dates and deadlines here
- Format: `• **Day, Month Date** — Description`
- Day of week always takes a comma: "Thursday, May 21" not "Thursday May 21"

---

## Section Headers

Emoji + bold header on its own line, body content on the next line.

**Preview syntax:**
```
:mega: **PARENT VOLUNTEERS FOR SPONSORSHIP DAY:**
Body text here...
```

**Copy-paste block (Slack mrkdwn):** same structure, single-asterisk bold:
```
:mega: *PARENT VOLUNTEERS FOR SPONSORSHIP DAY:*
Body text here...
```

### Emoji Mapping

| Section | Emoji |
|---|---|
| Parent Volunteers / Sponsorship Day | `:mega:` |
| Kick-Off Day PowerPoint | `:bar_chart:` |
| What to Bring & Wear | `:athletic_shoe:` |
| Register / Health Forms | `:clipboard:` |
| Commitment Contracts | `:memo:` |
| All Forms Due (general forms section) | `:memo:` |
| Absence Request Form (ARF) | `:calendar:` |
| Uniform Measurement Night | `:shirt:` |
| Financial Aid | `:money_with_wings:` |
| Mega Raffle | `:ticket:` |
| Band Camp Parent Volunteers | `:raised_hands:` |
| June Camp Day | `:sunny:` |
| Band Camp Handbook | `:books:` |

### Standing URLs

| Resource | URL |
|---|---|
| Forms page | `http://irondalebands.org/forms.html` (use instead of homepage when linking to forms) |
| Google Calendar (embedded) | `https://www.irondalebands.org/calendar.html` — link from "Important Dates" label and any reference to "the Google Calendar" |
| One-Page Calendar (printable) | `https://docs.google.com/document/d/1B9f32KEW2Y-brFYof47dDMmWk8zuCGnP/edit` — link when update references the "One-Page Calendar" (e.g. date changes, schedule updates) |

---

## Emphasis & Formatting

| Use case | Format |
|---|---|
| Key sentences, deadlines, important notes | _italics_ |
| Strong plain-language warnings | PLAIN ALL CAPS (no markdown) |
| Key dates/deadlines inline in body text | bold |
| Bold all caps | ❌ Do not use |

**Examples (preview / standard markdown shown; copy-paste block uses single `*`):**
- `_Wear athletic clothes and close-toed athletic shoes._`
- `_Uniform Measurement Night is scheduled for **Thursday, May 21st from 5:30–7:00pm** at Irondale High School._`
- `YOU DO NOT NEED TO INCLUDE SPRING TRAINING CONFLICTS`

For dense sections with a distinct callout or warning, put it on its own line with a blank line before it.

---

## Links

- Always bold linked text
- Use descriptive link text — never generic "HERE"

**Preview syntax:** `**[link text](URL)**`

**Copy-paste block (Slack mrkdwn) syntax:** `*<URL|link text>*`

---

## Voice & Attribution

- Derek forwards these updates on behalf of Dr. Longabaugh
- Always refer to him as **Dr. L** — never "Dr. Longabaugh"
  - Exception: email addresses are fixed text (e.g. `cameron.longabaugh@moundsviewschools.org`)
- Replace all first-person references with "Dr. L"
  - "email me" → "email Dr. L"
  - "let me know" → "let Dr. L know"
- When the update asks readers to email Dr. L, always include his address as a clickable link:

**Preview syntax:** `[cameron.longabaugh@moundsviewschools.org](mailto:cameron.longabaugh@moundsviewschools.org)`

**Copy-paste block (Slack mrkdwn) syntax:** `<mailto:cameron.longabaugh@moundsviewschools.org|cameron.longabaugh@moundsviewschools.org>`

---

## Punctuation

- Always apply correct punctuation — the source PDF may contain typos
- Day of week always takes a comma: "Thursday, May 21st" not "Thursday May 21st"
- Correct typos in section headers (e.g. "VOLUTNEERS" → "VOLUNTEERS")

---

## Rehearsal Schedules (when present)

Add an "Upcoming Rehearsals & Events" section at the end of the post:

**Preview syntax:**
```
**Upcoming Rehearsals & Events:**
• _Thursday, May 22, 6–9pm_
• _**Saturday, May 30 — Sponsorship Day**_
```

- Regular rehearsals: italics only
- Special events (competitions, performances, fundraisers): bold + italics

---

## Syntax Reference

### Preview (rendered in the DM) — standard markdown

| Effect | Syntax |
|---|---|
| Bold | `**text**` |
| Italic | `_text_` |
| Bold link | `**[text](URL)**` |
| Regular link | `[text](URL)` |
| Email link | `[email@domain.com](mailto:email@domain.com)` |

### Copy-paste block (for pasting into Announcements) — Slack mrkdwn, inside a fenced code block

| Effect | Syntax |
|---|---|
| Bold | `*text*` |
| Italic | `_text_` |
| Link | `<URL\|text>` |

⚠️ Never mix these: single `*text*` in the preview renders as italic, not bold — and double `**text**` inside the mrkdwn copy-paste block will show literal asterisks once pasted into Slack's composer.

Sections separate with a blank line between them in both versions.

---

# Instep (Performance Day) Posts

Insteps are performance-day rundowns, distinct from weekly updates. They follow the same general Slack formatting conventions above (preview + mrkdwn copy-paste block) but with Instep-specific rules.

## Instep Sections & Emojis

| Section | Emoji |
|---|---|
| Quick Details | `:pushpin:` |
| Schedule | `:clock9:` |
| Parent Info | `:car:` |
| Pick-Up Location | `:round_pushpin:` |

## Schedule Formatting

**Sequential events at the same time — use semicolons, not sub-items:**
When multiple things happen sequentially starting at the same time, consolidate into a single bullet separated by semicolons.

```
• 11:00 am — End Time; Eat Lunch; Bus to next location
```

NOT three separate lines without times.

**Don't double-signal uncertainty:**
If a description word already conveys approximation (e.g., "Tentative"), drop redundant markers like "~" or "-ish."

```
• 12:00 pm — Tentative Performance Time
```

NOT `~12:00 pm`.

## Links in Insteps

Provide links neutrally — never single out who might need them. Don't frame supplementary links (parade route, maps, etc.) as being for "rookie parents" or "first-timers."

```
Here's the **[parade route](URL)**.
```

NOT "Check the parade route if this is your first year."

## Sign-Off

Use the name as the author wrote it in the source document. If the Instep is signed "Dr. Longabaugh," use "Dr. Longabaugh" — not "Dr. L." No em dash before the name.

The "Dr. L" shorthand applies to weekly update body text where Derek is paraphrasing, not to direct sign-offs on authored Instep documents.

```
Thank you!
Dr. Longabaugh
```

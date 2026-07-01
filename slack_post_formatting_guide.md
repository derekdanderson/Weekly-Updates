# IHSMK Weekly Update — Slack Post Formatting Guide

## Overview

This guide covers formatting rules for converting the Irondale Marching Knights weekly update PDF into a Slack post. Two delivery methods are supported:

- **MCP tool** (`slack_send_message`) — uses standard markdown
- **Block Kit** (direct API via Python/curl) — uses Slack mrkdwn and JSON block structure

---

## Workflow

- Happens every Wednesday
- When a public PDF URL is shared, use WebFetch to extract content and hyperlinks automatically
- Download the PDF locally to `/Users/derekanderson/Documents/Band Boosters/Weekly Updates/` if not already there (use curl)
- Send the draft to Derek's DM (user ID: `U03FHQD6MBN`, channel: `D03FFDGPD6W`) — he handles posting to the real channel

---

## Post Structure

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
- The "Weekly Update – [Date]" line links to the PDF itself

**MCP syntax:**
```
:ihsmk_knight: **IRONDALE MARCHING KNIGHTS** :ihsmk_knight:
**[Weekly Update – May 20, 2026](PDF_URL)**
```

**Block Kit:**
- `header` block with `plain_text`: `:ihsmk_knight: IRONDALE MARCHING KNIGHTS :ihsmk_knight:` (`"emoji": true`)
- `section` block below it with mrkdwn link to the PDF

---

## Important Dates

Always placed directly under the header, before the first section. The label links to the Irondale Bands calendar.

**MCP syntax:**
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

**MCP syntax:**
```
:mega: **PARENT VOLUNTEERS FOR SPONSORSHIP DAY:**
Body text here...
```

**Block Kit:** Use `header` blocks (not bold mrkdwn) for section titles. Prefix with emoji. `plain_text` with `"emoji": true`.

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
| Key dates/deadlines inline in body text | **bold** |
| Bold all caps | ❌ Do not use |

**Examples:**
- `_Wear athletic clothes and close-toed athletic shoes._`
- `_Uniform Measurement Night is scheduled for **Thursday, May 21st from 5:30–7:00pm** at Irondale High School._`
- `YOU DO NOT NEED TO INCLUDE SPRING TRAINING CONFLICTS`

For dense sections with a distinct callout or warning, put it on its own line with a blank line before it.

---

## Links

- Always bold linked text
- Use descriptive link text — never generic "HERE"

**MCP syntax:** `**[link text](URL)**`

**Block Kit:** Attach each key document link as a `button` in the `"accessory"` field of a `section` block. Button text should be short and action-oriented (e.g. "Submit Health Form", "View Calendar"). Never put link buttons inside `actions` blocks — they are not clickable there.

For sections with multiple key links, create a separate `section` + `accessory` block per link button. Sections with no meaningful link get no accessory.

---

## Voice & Attribution

- Derek forwards these updates on behalf of Dr. Longabaugh
- Always refer to him as **Dr. L** — never "Dr. Longabaugh"
  - Exception: email addresses are fixed text (e.g. `cameron.longabaugh@moundsviewschools.org`)
- Replace all first-person references with "Dr. L"
  - "email me" → "email Dr. L"
  - "let me know" → "let Dr. L know"
- When the update asks readers to email Dr. L, always include his address as a clickable link:

**MCP syntax:** `[cameron.longabaugh@moundsviewschools.org](mailto:cameron.longabaugh@moundsviewschools.org)`

---

## Punctuation

- Always apply correct punctuation — the source PDF may contain typos
- Day of week always takes a comma: "Thursday, May 21st" not "Thursday May 21st"
- Correct typos in section headers (e.g. "VOLUTNEERS" → "VOLUNTEERS")

---

## Rehearsal Schedules (when present)

Add an "Upcoming Rehearsals & Events" section at the end of the post:

```
**Upcoming Rehearsals & Events:**
• _Thursday, May 22, 6–9pm_
• _**Saturday, May 30 — Sponsorship Day**_
```

- Regular rehearsals: italics only
- Special events (competitions, performances, fundraisers): bold + italics

---

## Markdown Syntax Reference

### MCP Tool (`slack_send_message`)
Uses **standard markdown** — not Slack mrkdwn:

| Effect | Syntax |
|---|---|
| Bold | `**text**` |
| Italic | `_text_` |
| Bold link | `**[text](URL)**` |
| Regular link | `[text](URL)` |
| Email link | `[email@domain.com](mailto:email@domain.com)` |

⚠️ Do NOT use single `*text*` — it renders as italic, not bold.

### Direct API / Block Kit (Python or curl)
Uses **Slack mrkdwn**:

| Effect | Syntax |
|---|---|
| Bold | `*text*` |
| Italic | `_text_` |
| Link | `<URL\|text>` |

### Block Kit Layout Rules
- Use `rich_text` blocks for structured lists (Important Dates, bullet lists) — supports proper bold and `rich_text_list` with `"style": "bullet"`
- Use spacer sections (`{"type": "section", "text": {"type": "mrkdwn", "text": " "}}`) between major sections
- Keep one divider only — after the subtitle and before content
- Do NOT add blank image placeholders to force consistent width (looks bad in dark mode)

---

# Instep (Performance Day) Posts

Insteps are performance-day rundowns, distinct from weekly updates. They follow the same general Slack formatting conventions above but with Instep-specific rules.

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

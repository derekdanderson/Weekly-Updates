# IHSMK Weekly Update — Slack Post Formatting Guide

## Overview

This guide covers formatting rules for converting the Irondale Marching Knights weekly update — published as a PDF at irondalebands.org, and archived as Markdown at `updates/YYYY-MM-DD.md` in the derekdanderson/Weekly-Updates repo — into a Slack post.

There is one delivery method: a single DM to Derek via the `slack_send_message` MCP tool, written in standard markdown (`**bold**`). Slack copy/paste preserves formatting within Slack, so Derek copies the rendered DM directly and pastes it into the Announcements channel — no separate mrkdwn version or code block is needed.

There is no automated posting step and no script — `send_update.py` has been removed.

---

## Workflow

- Happens every Wednesday (scheduled task "Irondale weekly update check" runs hourly on Wednesdays)
- Fetch the newest weekly update PDF from irondalebands.org and use WebFetch/the pdf skill to extract content and hyperlinks
- No local download needed — the scheduled task runs fully remotely. Dedupe and archival live in the derekdanderson/Weekly-Updates GitHub repo (`updates/YYYY-MM-DD.md`, Markdown)
- Build the post (see Post Structure below) and send it in one DM to Derek (user ID: `U03FHQD6MBN`, channel: `D03FFDGPD6W`) — he reviews it and copy/pastes it into the real channel himself

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
- The "Weekly Update – [Date]" line links to the original PDF on irondalebands.org (the public source)

**Syntax:**
```
:ihsmk_knight: **IRONDALE MARCHING KNIGHTS** :ihsmk_knight:
**[Weekly Update – May 20, 2026](PDF_URL)**
```

---

## Important Dates

Always placed directly under the header, before the first section. The label links to the Irondale Bands calendar.

**Syntax:**
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

**Syntax:**
```
:mega: **PARENT VOLUNTEERS FOR SPONSORSHIP DAY:**
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
| Generic "our website" reference | `https://www.irondalebands.org` |
| Weekly update posted/updated "on our website" | `https://www.irondalebands.org/weekly-updates.html` |
| Instep posted/updated "on our website" | `https://www.irondalebands.org/insteps.html` |

Match the link to what the sentence is actually about — a generic mention gets the homepage, but "the [weekly update/instep] has been posted on our website" gets the specific page, not the homepage.

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

**Syntax:** `**[link text](URL)**`

---

## Slack Channel & People References

- "Join the [x] channel in Slack" → look up the channel with `slack_search_channels` and link it as a real Slack channel mention, not plain text or an external URL:

**Syntax:** `<#CHANNELID|channel-name>` (e.g. `<#C05HXB0JWAU|first-aid>`)

- "Contact [Name] via Slack" → look up the person with `slack_search_users` and replace their name with a clickable @-mention, keeping "via Slack" in the sentence:

**Syntax:** `<@USERID>` (e.g. "contact `<@U08R4JJ2H60>` via Slack")

- Correct obvious name typos found during lookup (e.g. PDF's "Mellissa" → Slack profile's "Melissa") — same principle as other typo corrections
- When the update says "email Dr. L," always append his linked email address even in sections that don't otherwise mention email — don't assume it's already covered elsewhere in the post

---

## Voice & Attribution

- Derek forwards these updates on behalf of Dr. Longabaugh
- Always refer to him as **Dr. L** — never "Dr. Longabaugh"
  - Exception: email addresses are fixed text (e.g. `cameron.longabaugh@moundsviewschools.org`)
- Replace all first-person references with "Dr. L"
  - "email me" → "email Dr. L"
  - "let me know" → "let Dr. L know"
- When the update asks readers to email Dr. L, always include his address as a clickable link:

**Syntax:** `[cameron.longabaugh@moundsviewschools.org](mailto:cameron.longabaugh@moundsviewschools.org)`

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

## Syntax Reference

Standard markdown, rendered by the `slack_send_message` MCP tool:

| Effect | Syntax |
|---|---|
| Bold | `**text**` |
| Italic | `_text_` |
| Bold link | `**[text](URL)**` |
| Regular link | `[text](URL)` |
| Email link | `[email@domain.com](mailto:email@domain.com)` |

⚠️ Do NOT use single `*text*` — it renders as italic, not bold.

Sections separate with a blank line between them.

---

# Instep (Performance Day) Posts

Insteps are performance-day rundowns, distinct from weekly updates. They follow the same general Slack formatting conventions above but with Instep-specific rules.

## Intro Paragraph

Carry the source PDF's descriptive paragraph about the event (e.g. what Stockyard Days or the Mounds View Festival is) into the post as-is, right after the header/title line and before Quick Details. Don't skip it — it's the only context new parents get for an event they may not know.

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

**Addresses → clickable Google Maps links:**
Any street address (report locations, drop-off/pick-up points) should link to a Google Maps search.

```
https://www.google.com/maps/search/?api=1&query=<url-encoded address>
```
(spaces → `+`, commas → `%2C`). Wrap the location name in the link text and keep the plain address after it for reference, e.g.:
```
**[Long Lake Regional Park](https://www.google.com/maps/search/?api=1&query=1500+Old+Hwy+8%2C+New+Brighton%2C+MN+55112)** (1500 Old Hwy 8, New Brighton, MN 55112)
```

**Body images (e.g. a parade route map):**
The Slack MCP tool has no file/image upload capability — don't try to extract and host the image separately. Just link the relevant section to the source PDF, same as any other PDF reference:
```
Here's the **[parade route](PDF_URL)** if you'd like to find a good spot to watch.
```

## Sign-Off

Use the name as the author wrote it in the source document. If the Instep is signed "Dr. Longabaugh," use "Dr. Longabaugh" — not "Dr. L." No em dash before the name.

The "Dr. L" shorthand applies to weekly update body text where Derek is paraphrasing, not to direct sign-offs on authored Instep documents.

```
Thank you!
Dr. Longabaugh
```

# Qwava Question Writing Rules

The single source of truth for writing and editing Qwava conversation questions. Read this before writing or editing any question. `questions.json` (served from the CDN) is what the app and the widgets actually read; Raf applies edits to it manually. The Notion question pages have drifted from the JSON on several decks, so do not treat Notion as matching; the JSON is what counts.

## What a Qwava question is

A conversation prompt that has to work spoken out loud between two people. Many also have to fit on a small widget. Short, warm, and human beats clever or wordy every time.

## Length (the hard rule)

- Before writing anything, open the live `questions.json` and calculate the current global average character length with a script. It moves as the library changes (currently around 68 after the July 2026 shortening pass). Recompute it every session; do not assume.
- Every new question must be at or below that global average. No exceptions without flagging first. Shorter and punchier is always preferred.
- Measure by character count, not word count.
- Widget-eligible questions go shorter still: at or below the eligible average (around 59 to 60) and with no very long single words, which overflow the watch and widget display.
- Always verify with a script before presenting. For each question print: its length, whether it is over the average, a banned-word check, a dash check, and a duplicate check against the existing `questions.json`. Never eyeball it.

## Tone of voice (write for the ear, not the eye)

- Each question must sound like something a real person would actually say out loud to someone else. Read every one aloud in your head; if it trips, sounds stiff, or sounds written, rewrite it.
- Plain language only, easy for a non-native English speaker to read instantly. No clinical or academic phrasing.
- No therapy speak. Phrases like "sit with," "hold space," "show up for yourself" are red flags. Say it the way a friend would.
- Banned words, never use them: boundary, energy (in the wellness sense), behavior, behave, trait, consumptive, unearned. Some have turned up inside older questions, so watch for them when reviewing too.
- Avoid filler openers. "What's something that you..." and "What's something you..." are the most common source of bloat. Prefer the direct form: "What do you...", "What did you...", "What have you...", "What about your...". This alone often removes ten to twenty characters with zero loss of meaning.

## No dashes, anywhere

No hyphens and no em dashes in any question (or in any reply). Use commas, or reword. Dashes read as machine written.

## Depth and vibe balance

- Every question is tagged depth (light, medium, or deep) and vibe (fun or serious).
- When adding to a deck, first read the deck's existing questions and check its current depth and vibe mix, then fill the gaps rather than piling onto what it already has.

## Fixing existing questions that are too long

The July 2026 cleanup pass is done: bulk shortening applied, longest question now 86 characters, no dashes, banned words, or curly quotes left in the file. From here this is maintenance only, applied when a long question comes up anyway. Two approaches:

1. **Lossless filler removal first.** Strip "something that," hedges like "that you think" or "that you've," intensifiers like "actually," "really," "genuinely," and tails like "more than you'd expect." This usually saves ten to twenty-five percent and changes nothing. Only do this when meaning, depth, and vibe stay exactly the same.
2. **For genuinely long and complex questions, trim gently,** roughly fifteen to thirty percent, and keep them readable. Do not crush a deep question down to sixty characters just to hit a number. If a cut would change the nuance, leave it a little longer or rephrase more carefully. Meaning always wins over length.

## Delivery format

Deliver new questions as a CSV with these fields in this order:

`deck_key, deck_name, question_id, question, note, depth, vibe, widget_eligible`

- Number `question_id` continuing from the deck's current highest number.
- Leave `note` empty unless there is a reason.
- Set `widget_eligible` to FALSE by default; only TRUE for questions that pass the widget eligibility rules below.

## Widget eligibility (the daily question pool)

The daily question is a mindful pause: someone opening their phone in a free minute and reading one instead of doomscrolling. A question can be widget-eligible only if it is:

- **Standalone:** makes full sense read cold, no deck context, no partner needed, no setup.
- **Universal:** no job, career, startup, team, or networking framing (the user might be a student or not working).
- **Not place-bound:** no "this city," "here," "in Lisbon."
- **Not time-bound:** no "this weekend," "this week," "tonight," "this season." Evergreen "lately" or "recently" is fine.
- **Leaning medium or deep** for reflection, with a lighter layer mixed in for balance.
- **Short and display-safe:** at or below the eligible average, no long words.
- **Spread across decks** rather than concentrated. Skip inherently context-locked decks (Lisbon, Berlin, Local Secrets, Sibling Stories), work-framed decks (Networking, Team Sync, Between Meetings, Startup Talk, Career Journeys), and day or season specific decks (Weekend Debrief, Before the Weekend, The Long Days, The Quiet Season).

## Working style

- Give at most two options when a decision is needed, with a clear recommendation.
- Be direct and honest rather than hedged.
- Present questions in the chat first for approval, then deliver the CSV once agreed.

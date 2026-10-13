# Qwava Question Writing Rules

The single source of truth for writing and editing Qwava conversation questions and their follow ups. Read this before writing or editing any question. A chat that has read this file, `GERMAN_COPY_RULES.md` and `DECK_COPY_RULES.md` needs no handover.

## Where the content lives

- The Google Sheets `questions` and `follow_ups` are the working surface. Each holds English and German side by side.
- `questions.json` and `follow_ups.json` (plus their German files, served from the CDN) are exported from the sheets. They are what the app and the widgets read.
- Claude never edits the sheets. Raf attaches fresh CSV exports at the start of a session, Claude delivers CSV rows in the sheet's exact column order, Raf pastes them, then sends the export back for a check before any JSON export. Never work from an old copy; ask for a fresh export.
- The Notion question pages have drifted and do not count.

## What a Qwava question is

A conversation prompt that has to work spoken out loud between two people. Many also have to fit on a small widget. Short, warm, and human beats clever or wordy every time.

Every question must stand alone. It can reach the reader through Quick Mix, a widget, the watch, or a shared message, where the deck name is not visible. If a question only makes sense inside its deck, add the anchor to the text ("this weekend", "at work", "in summer").

One sentence, one question mark. Every question in the library has exactly one.

## Length (the hard rule)

- Before writing anything, calculate the current global average character length from the fresh export with a script. It moves as the library changes. In October 2026: 67.1 in English (median 67) and 60.2 in German, over 3,560 questions in 55 decks. Recompute it every session; do not assume, and do not trust an older number anywhere else.
- Every new question must be at or below that global average. No exceptions without flagging first. Shorter and punchier is always preferred.
- Hard ceiling: no question over 86 characters, in either language.
- Measure by character count, not word count.
- Widget eligible questions go shorter still: at or below the eligible average (57.6 in English in October 2026), never over 78, and with no very long single words, which overflow the watch and widget display.
- German has its own length rules. They are in `GERMAN_COPY_RULES.md` under "Length rules for questions and follow ups" and "Long words".
- Always verify with a script before presenting. See "The script check" below. Never eyeball it.

## Tone of voice (write for the ear, not the eye)

- Each question must sound like something a real person would actually say out loud to someone else. Read every one aloud in your head; if it trips, sounds stiff, or sounds written, rewrite it.
- Plain language only, easy for a non native English speaker to read instantly. No clinical or academic phrasing.
- No therapy speak. Phrases like "sit with," "hold space," "show up for yourself" are red flags. Say it the way a friend would.
- Banned words, never use them: boundary, energy (in the wellness sense), behavior, behave, trait, consumptive, unearned. Watch for them when reviewing too.
- Nothing that guilts or pressures. Qwava always supports; the user always decides.
- Avoid filler openers. "What's something that you..." and "What's something you..." are the most common source of bloat. Prefer the direct form: "What do you...", "What did you...", "What have you...", "What about your...". This alone often removes ten to twenty characters with zero loss of meaning.
- Vary the opener inside a deck. The library leans hard on three: "What's a" (983 questions), "What's something" (694, most of them older than the rule above) and "What's the" (376). Do not copy that habit into new decks. Mix in "What do", "If", "How", "When", "Who", "Which", and yes or no questions.
- Two part questions ("...and why?", "...or...?") are fine but cost length. Use them when the second half does real work.

## No dashes, anywhere

No hyphens and no em dashes in any question or follow up (or in any reply). Use commas, or reword. Dashes read as machine written. Apostrophes are straight (`'`), never curly.

## Depth and vibe balance

- Every question is tagged depth (light, medium, or deep) and vibe (fun or serious).
- When adding to a deck, first read the deck's existing questions and check its current depth and vibe mix, then fill the gaps rather than piling onto what it already has.
- A new deck has 60 questions. The depth targets come from the deck's `depth_default`: at least 15 questions per depth, and 20 or more for each depth in the default. See "Attributes" in `DECK_COPY_RULES.md`. The most common split is 25 light, 20 medium, 15 deep.
- Library mix in October 2026, as orientation: light 41 percent, medium 34, deep 25; fun 48 percent, serious 52. Light is mostly fun and deep is mostly serious. Deep and fun together is rare (61 questions) and worth adding where a deck allows it.

## Per question fields beyond depth and vibe

- `closeness`: empty by default, which means the deck's closeness applies. Fill it (`kind_of_familiar` or `close_friends`) only when one question needs a closer level than its deck. 23 questions have it.
- `group_only`: `TRUE` only when the question needs several people in the room ("Who here...", "Who at this table..."). Empty otherwise. 73 questions have it, 54 of them in Around the Table.
- `note`: leave empty unless there is a reason.

## German is written in the same step

A question or follow up without its German is not done. Write both languages together, set `de_status` to `done`, and follow `GERMAN_COPY_RULES.md` for everything German: `du`, gender neutral for the reader, settled vocabulary, long words, length.

## Fixing existing questions that are too long

The July 2026 cleanup pass is done: bulk shortening applied, longest question now 86 characters, no dashes, banned words, or curly quotes left in the file. From here this is maintenance only, applied when a long question comes up anyway. Two approaches:

1. **Lossless filler removal first.** Strip "something that," hedges like "that you think" or "that you've," intensifiers like "actually," "really," "genuinely," and tails like "more than you'd expect." This usually saves ten to twenty five percent and changes nothing. Only do this when meaning, depth, and vibe stay exactly the same.
2. **For genuinely long and complex questions, trim gently,** roughly fifteen to thirty percent, and keep them readable. Do not crush a deep question down to sixty characters just to hit a number. If a cut would change the nuance, leave it a little longer or rephrase more carefully. Meaning always wins over length.

## Delivery format for questions

Deliver new questions as a CSV with the columns of the `questions` sheet, in this order:

`deck_key, deck_name, question_id, question, note, depth, vibe, widget_eligible, question_de, de_status, closeness, group_only`

- `question_id` is `<deck_key>_<number>`, two digits (`career_01`), three from 100 on (`meetings_100`). Continue from the deck's current highest number. Never renumber or reuse an id.
- Set `widget_eligible` to FALSE by default; only TRUE for questions that pass the widget eligibility rules below.

## Widget eligibility (the daily question pool)

The daily question is a mindful pause: someone opening their phone in a free minute and reading one instead of doomscrolling. 377 questions are in the pool (October 2026). A question can be widget eligible only if it is:

- **Standalone:** makes full sense read cold, no deck context, no partner needed, no setup.
- **Universal:** no job, career, startup, team, or networking framing (the user might be a student or not working).
- **Not place bound:** no "this city," "here," "in Lisbon."
- **Not time bound:** no "this weekend," "this week," "tonight," "this season." Evergreen "lately" or "recently" is fine.
- **Short and display safe:** at or below the eligible average, never over 78, no long words.

The deck does not matter. Any question that passes every test above on its own can be eligible, whatever deck it comes from. City decks, work decks and day or season decks rarely qualify, only because most of their questions fail those tests. Prefer a spread across decks over many questions from one.

There is no depth rule for the pool for now. In October 2026 it is 58 percent light, 27 medium and 15 deep, and that balance is fine. The 377 questions are enough for about a year; the mix gets discussed again when the pool is extended.

## Follow ups

Every question has two follow ups of its own. A new question is not finished without them. After a send, the app offers the person's answer a next step: the first follow up, the second follow up, or one universal line.

### The four tiers

| Tier | Rows | Tied to | Id |
|---|---|---|---|
| `question` | one per question | its question | `fu_q_<question_id>` |
| `question_2` | one per question | its question | `fu_q2_<question_id>` |
| `universal` | 90 | no deck, fits any question | `fu_u_001` and up |
| `later` | 90 | no deck, for a send that is a week old | `fu_l_001` and up |

- Offer cycle in the apps: first follow up, second follow up, one universal on days 0 to 6 after the send; a `later` line instead of the universal on days 7 to 13; no offer from day 14. One follow up sent per question closes the card.
- `universal` and `later` are complete: 30 per depth, 18 fun and 12 serious in each. A new deck adds nothing to them.
- Ids must start with `fu_`. Never rename or reuse one; sent follow ups are stored by id.

### How a follow up is written

- **Every follow up must be interesting on its own (the most important rule here).** It adds a new angle the person would enjoy answering. A bare "Why?", "How did it start?", "What changed?", "Tell me more" or any other line that only asks to elaborate is never enough, and neither is a line that fits under any question in the library. Ways that work:
  - **Either/or:** "Are you fighting it or welcoming it back?", "Did you learn it the easy way or the hard way?"
  - **A twist on the answer:** "And what's the picture on the last page?", "What happened five minutes after it was taken?"
  - **Turn it to the other person:** "Did I know it mattered when I said it, you think?", "Is my version maybe better, though?"
  - **A concrete detail, time or place:** "What would it take to do that again next month?"
- Quality wins over length. A follow up may run longer than the average when its angle needs the words; never cut a line down to a generic one to save characters (see "Length of follow ups").
- It must work for ANY answer the other person could give. Never assume the answer. "Who gave it to you?" fails when nobody did; "Where did it come from?" works.
- One short spoken question. All voice rules for questions apply: for the ear, plain words, no therapy speak, no dashes, no banned words, nothing that guilts.
- It may lean on the question with "it", "that", "there". It is always read right under its question.
- A short lead in is allowed when it sounds like speech: "And...", "So...", "Consider it asked. What's the answer?" Use it sparingly.
- The two follow ups take different angles, because the user picks between them:
  - **First (`question`):** stays inside the answer and goes one step deeper. Why, how, what exactly, better or worse, what made it so.
  - **Second (`question_2`):** turns somewhere else. The people around it, before or after, the other side, how often, where it came from, what happens next. If the first is an open question, a closed one works well here, and the other way round.
- Example:
  - Question: "What does a really bad night look like for you and what usually causes it?"
  - First: "What helps most the morning after one?"
  - Second: "Who can tell the next day that you had one?"
- Keep the "who" questions in check. In the library 33 percent of the second follow ups start with "Who" and 40 percent ask about other people. That is too many. In a new deck, no more than a quarter of the second follow ups should be "who" questions.
- Questions marked `group_only` get follow ups written for the group ("Who here...", "Which story should we hear right now?").
- Sensitive questions stay gentle: never assume living parents, a partner, a job, or that things went well.
- German: the pronoun must match the gender of the noun in the German question (er, sie, es). Check each row against `question_de`, not against the English.

### Length of follow ups

- Hard ceiling: 67 characters, in either language.
- Averages in October 2026, as the guide for new rows (recompute with a script):

| Tier | English average | German average | Longest English |
|---|---|---|---|
| `question` | 41.9 | 34.4 | 66 |
| `question_2` | 33.7 | 29.4 | 47 |

- The averages are a guide, not a target to undercut: a new deck's follow ups should land near them (first about 42, second about 34), not far below. A deck whose follow ups average well under these is usually full of generic lines; rewrite those rather than celebrate the short count.
- Individual rows may go longer when the angle needs it, up to the 67 ceiling.
- Existing follow ups of low quality (generic, elaborate only) are to be reviewed in a later pass (October 2026).

### Delivery format for follow ups

Columns of the `follow_ups` sheet, in this order:

`tier, deck_key, question_id, followup_id, text, depth, vibe, text_de, de_status`

- `deck_key`, `question_id`, `depth` and `vibe` are copied from the question.
- One CSV per deck: the `question` block first, the `question_2` block directly under it, both in question order. That is how the sheet is laid out.

## The script check

Run it on every new question and follow up, English and German, before anything is shown or delivered. Print per row:

1. Length, and whether it is over the current average or a hard ceiling (question 86, widget 78, follow up 67).
2. Dash check, curly quote check, stray spaces, ends with a question mark.
3. Banned words in both languages. German needs a word boundary and the conjugated forms: `(?<![a-zäöüß])verhalten`, `verhält`, `verhielt`. Expect a false hit on `Verhältnis`.
4. Duplicate check against the WHOLE library in both languages, and inside the new batch. For follow ups that means all 7,300 existing rows. Short follow ups collide often, German more than English.
5. Ids: right format, continuing in order, one row per question, and for follow ups exactly one `question` and one `question_2` row per question with matching depth and vibe.
6. Depth and vibe counts against the deck's targets.
7. The widest German word, by the card width rule in `GERMAN_COPY_RULES.md`.

When Raf sends the export back after pasting, compare it row by row with what was delivered and with the previous export, so a shifted or half pasted block is caught before the JSON export.

## Working style

- Give at most two options when a decision is needed, with a clear recommendation.
- Be direct and honest rather than hedged.
- Present new questions in the chat first for approval, then deliver the CSV once agreed.
- Follow ups are not reviewed row by row. Deliver the CSV with the check result and raise only the lines that are risky or need a decision.
- Work deck by deck, so the voice stays consistent inside a deck.

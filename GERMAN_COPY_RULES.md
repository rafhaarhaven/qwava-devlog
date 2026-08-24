# Qwava German Copy Rules

The single source of truth for the German version of Qwava. Read this before translating any deck copy, question, follow up, or message line. It sits alongside `QUESTION_WRITING_RULES.md` and `DECK_COPY_RULES.md`, which still apply: this file only records what is different in German.

Written during the deck copy pass (55 decks, August 2026) and meant to grow as the questions and messages get translated.

## Register

**du, never Sie.** Qwava is a friend handing you a question, not an institution. This holds at every closeness level, including a person the user has just met.

**Write for the ear.** Same rule as English. Read every line aloud. If it sounds written rather than spoken, rewrite it. German drifts formal faster than English does, so this matters more here.

**Plain German.** No Behördendeutsch, no nominalisation stacks, no therapy register. A native speaker who is not a writer should be able to say the line out loud without stumbling.

## What gets translated

Only text a user reads. Everything else is machinery and stays English forever.

**Translate:** `title`, `subtitle`, `description`, `explanation`, `question`, follow up `text`, message `text`.

**Never translate:** `deck_key`, `question_id`, `followup_id`, `message_id`, and every attribute value (`depth`, `vibe`, `closeness`, `audience`, `category`, `component`, `recency`, `widget_eligible`). The app turns `fun` into a display label in code, so the German word for it is written once in the string table, not once per row.

The IDs are the link between the English and German rows. **Never renumber or reuse a retired ID.**

## Length

German runs 10 to 20 percent longer than English. The layouts were built for English, so the ceilings do not move.

**The rule: every German field must be at or under the English length for that same row, and never over the ceiling in `DECK_COPY_RULES.md`.** Where German cannot fit, cut an idea rather than shrink the type. A shorter German line that lands is better than a faithful one that truncates.

Ceilings that caught real errors during the deck pass: subtitle 27, description 65, explanation 120 to 160 and exactly two sentences.

Widget and watch text is the tightest constraint in the library. Widget eligible questions need their own German ceiling, measured once enough of them exist.

**Verify with a script before presenting anything.** Never eyeball a character count.

## Fixed formulas

English repeats a phrase on purpose; German has to repeat its own equivalent, not vary it.

- Deck explanation, second sentence: English "Great for ..." becomes **"Ideal, um ... zu ..."**. Every deck, no variation.

## Punctuation

- **Quotation marks: `„` and `“`.** German typography, not the English pair. `„Wie läuft die Arbeit?“`
- **Apostrophes: straight `'`.** The whole content library is straight. Do not let an editor autocorrect them into curly ones.
- **No dashes, ever.** No hyphens, no em dashes. Same as English. German compounds that want a hyphen get rewritten: `Lieblings-Apps` became `liebste Apps`.
- **The ellipsis character `…`** is fine and matches the English rows that use it.

## Loanwords

Keep the English word when Germans actually say it in speech: **Highlights, Startup, Podcast, Smalltalk, Looks, Apps, Team, Trips**.

Translate when a natural German word exists and is in everyday use. Reaching for English where German has a good word makes the app sound like a translation.

Sometimes the German word is better than the English original. `Smalltalk` in a deck description became **`Floskeln`**, which is sharper and more specific about what the deck is escaping.

## Banned words

The English list carries over through its German equivalents:

- **Verhalten** (behavior). Say what the person does, not what the behaviour does.
- **Energie** in the wellness sense. Use `Gesellschaft`, `Zeit für sich`, or name the actual thing.
- **Eigenschaft** (trait).
- **Grenze** in the boundary sense.

Also avoid: therapy register generally, and anything that implies the user has fallen behind. Nothing in Qwava guilts the user, in any language.

## Titles are read, not translated

A deck title has 17 characters and has to sound like something you would say handing the deck to a friend. A literal translation almost never survives that. Find the German idea instead.

Examples that worked:

| English | German | Why |
|---|---|---|
| Crossing Borders | `Grenzgänger` | One word, and it names the person rather than the act |
| Shared Struggles | `Geteiltes Leid` | Half of a saying every German completes silently |
| Hot Takes | `Klare Kante` | The German idiom for taking a firm position |
| Brain Food | `Kopffutter` | Same playful compound, same register |
| Game On | `Anpfiff` | The whistle, and exactly as short as the English |
| Make a Wish | `Wünsch dir was` | The phrase Germans actually say over a cake |
| Before Weekend | `Freitagsgefühl` | Names the feeling instead of the timing |
| Weeks Apart / Years Apart | `Wochen später` / `Jahre später` | The English pairs on "Apart", the German pairs on "später" |

The same applies to questions. Some will not survive a literal translation at all and need a German question that lands the same way.

## The card front

Title, subtitle and description appear together, so a repeated word is visible. The English breaks this rule in 18 of 55 decks, so it is not strictly enforced, but **do not introduce a repeat in German that the English does not have**. Five had to be fixed during the deck pass.

## Files

The spreadsheet holds every language side by side, one `_de` column per translatable field plus a `de_status` column. That is the working surface, and it means a changed English row shows immediately which German row went stale.

The export splits them. English users never download German text.

```
/app/v1/decks.json          English
/app/v1/de/decks.json       German
```

Untranslated fields fall back to the English rather than exporting empty, so a missing German title can never render as a blank card. The export script reports how many fields are still English; that number is the progress bar.

## Working style

- Give at most two options when a decision is needed, with a clear recommendation.
- Verify every character count with a script before presenting. Never eyeball it.
- Present copy in the chat for approval first, then hand over a paste ready file.
- Translate deck by deck, not in arbitrary blocks, so the voice stays consistent inside a deck.

# Qwava Deck Copy Rules

The single source of truth for writing deck titles, subtitles, descriptions, explanations, and personalization labels. Read this before writing or editing any deck-facing text. `decks.json` and `deck_labels.json` (served from the CDN) are what the app actually reads; Raf applies edits to them manually. For question writing, read `QUESTION_WRITING_RULES.md` instead.

## Where each text lives

The front of a deck card shows the title, subtitle, and description together on one screen. The back shows the explanation plus the attribute lines (audience, closeness, vibe, depth, categories). A personalization label is a small colored pill that can appear on the card at certain times or situations.

## Title

- 2 to 4 words, no punctuation.
- Character budget: most titles sit between 9 and 16 characters. 17 is the practical ceiling. Anything at 18 or more breaks layouts and gets renamed (this happened to "Unfinished Business", 19 characters, renamed to "Left Unfinished").
- Read it aloud. It should sound like something you would say when handing the deck to a friend.

## Subtitle

- One short sentence ending with a period.
- 22 to 25 characters. 27 is the hard ceiling.
- Sets the mood in one breath. Example: "Building it all alone."

## Description

- One sentence ending with a period.
- 57 to 62 characters. 65 is the hard ceiling.
- Use the comma list structure: "X, Y, and Z" with three concrete nouns or noun phrases. Example: "Cold drinks, slow plans, and everything the heat changes."
- Mobile line wrap: avoid a long word landing at the start of the second line. Check how it breaks on a narrow screen and reorder if needed.

## Explanation (back of card)

- Exactly two sentences, 120 to 160 characters total.
- First sentence frames the theme, second says who or what the deck is for.
- Example: "Some days are too hot for anything but good company. Easy questions for shade, cold drinks, and afternoons that move slowly."

## No repetition on the front

Title, subtitle, and description appear together, so no meaningful word may repeat across them. "Hot Day" with subtitle "For when it's really hot" fails; "Around the Table" with description "family tables" fails. The explanation is on the back, so it may reuse front words freely.

## No dashes, anywhere

No hyphens and no em dashes in any deck text or label. Use commas, or reword.

## Personalization labels (deck_labels.json)

- 2 to 3 words, short enough to sit next to the deck number without touching it. "Builder's Weekend" was too long on a two digit deck number and became "Build Mode".
- Title case for every significant word: "Treat Yourself", not "Treat yourself".
- Unique within a trigger group. If three decks can appear together on a Friday, only one may say "Friday Pick"; the others need their own labels. Generic "X Pick" is fine once per group, at most.
- Playful and inviting, never pushy or guilt based. Re-engagement labels especially: "Still Here" and "Getting Dusty" work because they are warm and a little funny, not nagging. Nothing in Qwava punishes the user.
- Priorities within a tag start at 1 and run consecutively with no gaps and no duplicates. Priority 1 wins the carousel slot.

## deck_key naming

One lowercase word, no separators of any kind: `localsecrets`, `firstdate`, `aroundthetable`. The key is permanent once shipped, so choose it to survive a title rename (the deck "Left Unfinished" still uses key `unfinished`).

## Attributes (deck_filters.csv)

- `audience`: pipe separated from `couple|small_group|large_group`.
- `closeness`: pipe separated from `just_met|kind_of_familiar|close_friends`. Think about the real situation: a deck for strangers who share a situation (solo founders at an event) can be `just_met` even if its questions go deep.
- `category`: 2 to 4 values from the 8 category codes.
- `depth_default`: which depth levels are on when the deck first opens. This drives question targets: at least 15 questions per depth level overall, and 20 or more for each level in the default. A 60 question deck with default `medium|deep` wants roughly 15 light, 25 medium, 20 deep.

## Working style

- Give at most two options when a decision is needed, with a clear recommendation.
- Verify every character count with a script before presenting. Never eyeball it.
- Present copy in the chat for approval first; Raf applies approved text to the JSON files manually.

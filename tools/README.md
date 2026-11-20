# Tools

## build_content.py: the content export

Turns the Google sheet exports into the content files the apps load, checks them first, and reports what changed compared to the live files. It never changes the sheets or the live files; it only writes into the output folder.

### What Raf exports

One CSV per sheet tab, exported as it is, with these names:

- `decks.csv`
- `deck_filters.csv`
- `deck_labels.csv`
- `questions.csv`
- `follow_ups.csv`
- `messages.csv`
- `decksfav.csv`

German lives in the same sheets, in the `_de` columns. Any column named `FIELD_de` is used for that field in the German file.

### How a chat runs it

1. Put the seven CSVs in one folder, for example `csv/`.
2. Have a read only clone of the iOS repo (`qwava-app`); the live files are in `Qwava/Qwava/`.
3. Run:

```
python3 -I tools/build_content.py csv out /path/to/qwava-app/Qwava/Qwava
```

4. Send Raf the printed report first, then the files from `out/`.

The live folder is the last state pushed to GitHub. If Raf has content in Xcode that is not pushed yet, the change report compares against the older state; say so.

### What it builds

`decks`, `decksfav`, `deck_filters`, `deck_labels`, `questions`, `follow_ups`, `messages`, and the `de_` twin of each except `deck_filters`. Same format as the live files: json, 1 space indent, UTF 8, trailing newline. On the November 2026 sheets it rebuilt all 13 live files byte for byte.

Not built here: `person_matching.json` (written by hand; the script only checks its deck keys).

### Blockers and warnings

Blockers stop the build and nothing is written. Fix them in the sheet and export again:

- colour codes that are not `#` plus six hex digits (decks and labels)
- missing ids, titles, question text or German text
- duplicate deck keys, question ids, follow up ids, message ids, or a tag twice on one deck
- a deck missing from deck_filters or deck_labels, or one there that is not in decks
- a question, follow up or person matching entry pointing to a deck or question that does not exist
- values outside the allowed lists (depth, vibe, audience, closeness, category, recommend, tier, message fields)
- follow up ids not starting with `fu_`
- dashes in questions, follow ups (English and German) and German messages

Warnings are listed, the build goes ahead, and Raf decides:

- new questions over the English or German average (computed from the sheet every run)
- widget eligible questions over 78 characters
- a question without both of its follow ups
- German status not `done`
- dashes in English share messages
- a decksfav colour that is not a code (it uses `white`)

### Change report

After the build it lists, per file, what is new, removed or edited compared to the live files, in English and German, with the old and new text for every edited field, and whether the order changed.

### Changing the script

New fields, sheets or rules go into the script in a Decks chat, tested against a fresh export: the build of an unchanged export must still match the live files byte for byte.

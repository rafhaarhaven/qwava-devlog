# Qwava German Copy Rules

The single source of truth for the German version of Qwava. Read this before translating any deck copy, question, follow up, or message line. It sits alongside `QUESTION_WRITING_RULES.md` and `DECK_COPY_RULES.md`, which still apply: this file only records what is different in German.

Written during the deck copy pass and extended after translating all 570 Natural Reach messages and all 3,560 questions across 55 decks (August 2026). Follow ups and UI strings are still to come.

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

## Every question must stand alone

**This is the most important rule in the file.** A question can reach the reader through Quick Mix, a widget, a watch complication, or a shared message. In none of those places is the deck name visible. The question has to carry its own context.

English usually carries the anchor in the text: "this weekend", "this week", "at work", "in winter". German is tempting to shorten by dropping it, because the deck name seems to do the work. It does not.

`Was hast du unbemerkt für dich selbst getan?` is a fine sentence and a broken question. It became `Was hast du am Wochenende unbemerkt für dich selbst getan?`

Anchors that were needed deck by deck: `Wochenende`, `Woche`, `Winter`, `Sommer`, `Morgen`, `Nacht`, `Hitze`, `bei der Arbeit`, `Lissabon`, `Berlin`, `deine Geschwister`, `dieser Tisch`. **Add the anchor even where the English lacks it**, if the question would otherwise be ambiguous on its own. Forty one rows had to be rewritten after this was caught late; check it while translating, not after.

Verify with a script per deck: every row should contain at least one anchor word for that deck's context.

## Gendered nouns

German forces a gender where English does not. **Never make the reader pick one about themselves.**

- `Hey stranger` cannot be `Hey Fremder` or `Hey Fremde`. It became `Lange nicht gesehen.`
- `like a local` cannot be `wie ein Einheimischer`. It became `wie jemand von hier`.
- `a director` cannot be `Regisseur`. It became `Regie`, the role rather than the person.
- `a manager` became `Führungskraft`, which is neutral as a role.
- `sibling` has no gender neutral singular at all. The whole Sibling Stories deck uses the plural `deine Geschwister`, which also gives `ihr` for free and shortens the deck.

**Third parties are different.** `Sportler`, `Fremden`, `Mitgründer` are acceptable where the question is about someone else, since nothing is being imposed on the person answering.

**Plurals are usually safe:** `Einheimische`, `Alteingesessene`, `Kollegen`, `Gäste`.

## The `Ich` compound trap

German wants to build `Kinder-Ich`, `Arbeits-Ich`, `Familien-Ich`, `Wochenend-Ich`. All of these need a hyphen, and hyphens are banned. This tripped three separate decks.

**The fix is a prepositional phrase, not a compound.**

- `Kinder-Ich` becomes **`das Kind in dir`**
- `Arbeits-Ich` becomes **`du bei der Arbeit`**
- `Familien-Ich` becomes **`du bei deiner Familie`**

`dein zukünftiges Ich`, `dein jüngeres Ich`, `dein bestes Ich` and `dein ideales Ich` are all fine, because an adjective carries them rather than a second noun.

Other hyphen traps caught: `Startup-Klischee`, `Startup-Leben`, `Dating-Regel`, `Lieblings-Apps`, `Winterabend-Look`, `Zwei-Fragen-Tag`, `Wikipedia-Strudel`. Each was rewritten as a phrase.

## Settled vocabulary

Words that recur across the library and must stay consistent.

**The self**
`dein bestes Ich`, `dein ideales Ich`, `dein zukünftiges Ich`, `dein jüngeres Ich`, `das Kind in dir`.

**Work**
`Berufsleben` and `beruflich` for everyday register. `Weg` where the sense is the path. `Werdegang` where the sense is the path in hindsight. `Karriere` only where ambition is the subject. `Beruf` only for the occupation itself. **Never `Laufbahn`**, which is stiff.
`Termin`, not `Meeting`. `Führungskraft`, not `Chef`. `Rückhalt`, not `Unterstützung`.

**Comfort splits three ways**
`Geborgenheit` for the feeling of being safely held. `Trost` for consolation, including comfort food. `Gemütlichkeit` for cosy warmth. **Never `Komfort`**, which means physical convenience.

**Home splits three ways**
`Wohnung` for the physical flat. `zu Hause` for living there. `Zuhause` as the noun for belonging.

**Time**
`zuletzt` for the most recent single instance. `gerade` for right now. `in letzter Zeit` for an ongoing stretch. These are not interchangeable and mixing them up is the classic tell of translated German.

**Small words that recur**
`ganz still` for "quietly". `auftanken` for "recharge". `auslaugen` and `Kraft kosten` for "drain". `runterkommen` for "wind down". `Song`, not `Lied`, except `Liedzeile` for a lyric.

## Constructions that save characters

German came in seven characters shorter than English on average across 3,560 questions. Almost all of it comes from four moves.

**Turn the noun phrase into a verb.** English needs `What's something you do that...`; German just says `Was machst du, das...`. Same for `What's a skill you have` becoming `Worin bist du gut` or `Was kannst du`. This is the single biggest saving in the project.

**Split long conditionals into a statement plus a question.** `If someone handed you a business and said build anything, what would it be?` becomes `Jemand gibt dir eine Firma und sagt: bau was. Was baust du?` Used in more than a dozen decks.

**Invert the verb instead of using `wenn`.** `Könntest du in einen wichtigen Moment zurück, würdest du gleich entscheiden?` is shorter and more spoken than the full conditional.

**Use a colon for a reported thought.** English embeds thoughts without punctuation; German cannot. `Bei welchem Moment dachtest du: krass, ist das wirklich mein Leben?`

## Coinages are allowed

Where English bends its grammar for a joke, German may bend its own. `Freitagigste` for "the most Friday thing", `überkleidet` for "overdressed". A German reader hears the joke even though the word is not in the dictionary. Use sparingly and only where the English is doing the same thing.

## Localize, do not translate

Questions that reference English or an English speaking context break for a German reader and must be rewritten.

- "a phrase you can't translate into English" became `ins Deutsche`
- "a word English really needs" became `dem Deutschen`
- "a German word you use when speaking English" became `Welches Berliner Wort benutzt du inzwischen ganz selbstverständlich?`
- `finsta` has no German equivalent and became `ein privates Konto`
- `MVP` became `die Sparversion`
- `rest with bad PR` became `Erholung mit schlechtem Ruf`

## The app_line register

The Natural Reach `app_line` messages name Qwava and explain what it is. **Keep these plainer and slightly more apologetic than the English.** English reads casual by default; the same enthusiasm in German reads like a press release.

`Not an ad, just seeing if it's useful` became `Keine Werbung, ich schaue nur, ob sie hilft.`

## Length rules for questions

- **Never over 86 characters.** That is the longest English question in the library and therefore proven to fit the card.
- **Never over 78 for the 377 widget eligible questions.** That is their proven maximum on the watch and home screen.
- **Each deck's German average must land at or under that deck's English average.** This catches drift that individual line checks miss. Founding Solo failed this on the first pass at 57.9 against 55.2 and needed thirty rows tightened.

Achieved across the full library: English average 67.1, German 60.2. Longest German question 82. Widget rows average 55.3, maximum 76.

## Check the whole library, not just the deck

Two errors were invisible at deck level and only appeared when all 3,560 rows were checked together.

- **Duplicates across decks.** Two questions with slightly different English collapsed to identical German. Check `Counter(all_values)` over the entire library before shipping.
- **False positives in the banned word check.** `verhalten` matched inside `Geschwisterverhältnis`, which is an ordinary word. Use a word boundary: `(?<![a-zäöüß])verhalten`.

Also check conjugated forms. `verhält` and `verhielt` do not contain the string `verhalten`.

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

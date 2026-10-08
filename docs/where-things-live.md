# Where things live

The map of documentation locations. This file lists locations only, never content, so it cannot go stale. The Notion pages are the single source of truth for product decisions; the code is the truth for constants; the devlog is the permanent dated record of what happened.

## Notion (private, fetch before every update)

- **Build Log**: session log, milestones, open tasks, and the working rules for every chat.
- **Qwava, What the App Does Today**: the authoritative description of current app behavior, live and unreleased.
- **Connection Rhythm, Evolution**: the relational layer: v1, v2, the person knowledge layer, the prompt slot, the v3 shelf, and every decision with its reasoning.
- **Your Space, Evolution**: the Your Space tab: sections, placeholder rules, recommendation engine, sync, guardrails.
- **Natural Reach, Evolution**: the sharing layer: the flow, what it writes, platform differences, expansion candidates.
- **Person Prompt Engine, What Shows When**: the operational record of every suggestion surface about a person: slot priority, ask rules, coordination duties for future surfaces.
- **Personalization Labels**: the tag system, per deck labels and priorities, and the advanced label wishlist.
- **Store Listings**: what the App Store and Google Play listings say right now, per platform and locale: name, subtitle, keywords, promotional text, descriptions, release notes, screenshot captions, feature graphic. Plus why each piece says what it says and what is still untested. Read before touching any store field.
- **No-Talk Growth Strategy**: Apple Search Ads and passive growth. Never mirrored here; this repo is public.
- **Social Media Strategy**: Instagram cadence and post log. Same rule.
- **Pitch Deck, read alone version**: the pitch content. Same rule.
- **Pitch Research & Data**: the sources behind the pitch's market and loneliness numbers. Same rule.
- **Next Level**: product evolution: the ten ideas by pillar and the Qwava Plus candidate list. The input for business model and pitch roadmap work. Same rule.
- **Business Plan**: the money logic: Qwava Plus pricing, free caps, revenue scenarios, costs and break even, later revenue, and the investor narrative. Same rule.

## Code (the truth for constants and behavior)

- Prompt slot rules and tunables: `PersonPromptEngine.swift` in the iOS repo.
- Personalization tag activation and tiers: `PersonalizationEngine.swift`; per deck labels in `deck_labels.json` (bundled fallback, cached, refreshed from the CDN like the other content stores; German at `de/deck_labels.json`).
- Deck recommendation logic: `RecommendationEngine.swift`.
- Question suggestions and the person recommendation: `SuggestedQuestionEngine.swift`, `PersonMatchingStore.swift`; the matching content in `person_matching.json` (bundle only for now). Birthday card facts (window, wish sent, headline inset) for the person page and Your Space: `BirthdayPicks.swift`.
- Recommendation rules per deck (never, birthday, quiet): the `recommend` and `quiet_days` columns in `deck_filters.json`, read by `DeckFilterStore.swift`; per question `closeness` and `group_only` in `questions.json`.
- Cloud sync, merges and tombstones: `CloudSync.swift` and the stores it feeds (`FavoritesStore`, `SavedQuestionsStore`, `SharedQuestionsStore`, `PeopleStore`, `FollowUpsStore` for dismissals).
- Follow up offer timing, language of the offer and dismissal stamps: `FollowUpsStore.swift`; content in `follow_ups.json` and `de_follow_ups.json` (tiers question, question_2, universal, later).
- Remote content and image loading: `RemoteContent.swift`, `RemoteDeckCover.swift`; the CDN manifest decides what is fetched remotely.
- Content cache headers: `.htaccess` in `/content/app/` on the Strato content server.
- Sharing: `QwavaShareSheet.swift` (one share sheet for every share, mail subject for mail apps); the Natural Reach flow in `NaturalReachView.swift`.
- App opens and deep sessions behind the behaviour labels: `AppOpenTracker.swift`, and the deep session count in `QuestionPlayerView.swift`.

## This repo

- `/devlog/`: one file per month, one entry per session, newest at the bottom. The permanent dated record.
- `QUESTION_WRITING_RULES.md`: the rules for writing and reviewing deck questions. Read before any Decks content session.
- `DECK_COPY_RULES.md`: the rules for deck copy. Read before Decks and Copy sessions.
- `GERMAN_COPY_RULES.md`: the rules for the German version, register, length, punctuation and what never gets translated. Read before any translation session.
- The README holds the devlog rules.


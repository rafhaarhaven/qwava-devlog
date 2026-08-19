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
- **No-Talk Growth Strategy**: Apple Search Ads and passive growth. Never mirrored here; this repo is public.
- **Social Media Strategy**: Instagram cadence and post log. Same rule.
- **Pitch Deck, read alone version**: the pitch content. Same rule.

## Code (the truth for constants and behavior)

- Prompt slot rules and tunables: `PersonPromptEngine.swift` in the iOS repo.
- Personalization tag activation and tiers: `PersonalizationEngine.swift`; per deck labels in `deck_labels.json` (bundle only, not fetched remotely).
- Deck recommendation logic: `RecommendationEngine.swift`.
- Question suggestions and the person recommendation: `SuggestedQuestionEngine.swift`, `PersonMatchingStore.swift`; the matching content in `person_matching.json` (bundle only for now).
- Follow up offer timing: `FollowUpsStore.swift`; content in `follow_ups.json`.
- Remote content and image loading: `RemoteContent.swift`, `RemoteDeckCover.swift`; the CDN manifest decides what is fetched remotely.

## This repo

- `/devlog/`: one file per month, one entry per session, newest at the bottom. The permanent dated record.
- The README holds the devlog rules.

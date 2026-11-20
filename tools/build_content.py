#!/usr/bin/env python3
"""Build the Qwava content files from the Google sheet CSV exports.

Usage: python3 build_content.py CSV_DIR OUT_DIR LIVE_DIR

CSV_DIR holds the seven sheet exports: decks, deck_filters, deck_labels,
questions, follow_ups, messages, decksfav (each NAME.csv).
OUT_DIR receives the English files and their de_ twins, in the exact format
the apps load (json, 1 space indent, UTF-8, trailing newline).
LIVE_DIR is the folder with the current live files (Qwava/Qwava in the iOS
repo). It is read only: the checks compare against it and read
person_matching.json from it.

The checks run first. Any blocker stops the build and nothing is written.
Warnings are printed and the build goes ahead.
After the build it reports what changed compared to the live files.
Nothing in CSV_DIR or LIVE_DIR is ever changed.
"""
import csv
import json
import os
import re
import statistics
import sys


def read_csv(csv_dir, name):
    with open(os.path.join(csv_dir, name + ".csv"), encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_json(out_dir, name, data):
    with open(os.path.join(out_dir, name + ".json"), "w", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=1) + "\n")


DECK_KEYS = ["deck_key", "number", "title", "subtitle", "description", "explanation", "image_base",
             "title_color", "subtitle_color", "credits_color", "description_color", "explanation_color",
             "explanation_spot_color", "explanation_background_color", "card_background_color",
             "card_outline_color", "credits_primary", "credits_secondary"]
FAV_KEYS = ["deck_key", "number", "title", "subtitle", "description", "explanation", "image_base",
            "credits_primary", "credits_secondary", "title_color", "subtitle_color", "description_color",
            "credits_color", "card_background_color", "card_outline_color"]
FILTER_KEYS = ["deck_key", "deck_name", "audience", "closeness", "category", "depth_default",
               "number", "recommend", "quiet_days"]
QUESTION_KEYS = ["deck_key", "deck_name", "question_id", "question", "note", "depth", "vibe",
                 "widget_eligible", "closeness", "group_only"]
FOLLOW_UP_KEYS = ["tier", "deck_key", "question_id", "followup_id", "text", "depth", "vibe"]
MESSAGE_KEYS = ["message_id", "recency", "closeness", "component", "text"]


def pick(row, keys):
    return {k: row[k] for k in keys}


def german(row, keys, text_map):
    """Same row with the German columns swapped in. text_map: json key -> German csv column."""
    out = pick(row, keys)
    for key, de_col in text_map.items():
        out[key] = row[de_col]
    return out


def build_decks(rows, keys):
    """Every field with a matching NAME_de column in the sheet takes its German text from there."""
    en = [pick(r, keys) for r in rows]
    de = [german(r, keys, {k: k + "_de" for k in keys if k + "_de" in r}) for r in rows]
    return en, de


def build_labels(rows):
    """One entry per deck in deck_order, with its tags; a row with no tag gives an empty list."""
    en, de, index = [], [], {}
    for r in rows:
        key = r["deck_key"]
        if key not in index:
            index[key] = len(en)
            base = {"_ref": r["_ref"], "deck_key": key,
                    "label_color": r["label_color"], "label_text_color": r["label_text_color"]}
            en.append(dict(base, highlight_tags=[]))
            de.append(dict(base, highlight_tags=[]))
        if not r["tag"]:
            continue
        i = index[key]
        for out, label in ((en, r["label"]), (de, r["label_de"])):
            tag = {"tag": r["tag"], "priority": int(r["priority"]), "label": label}
            if r["locale"]:
                tag["locale"] = r["locale"]
            out[i]["highlight_tags"].append(tag)
    return en, de


def build(csv_dir, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    decks = read_csv(csv_dir, "decks")
    de_names = {r["deck_key"]: r["title_de"] for r in decks}

    en, de = build_decks(decks, DECK_KEYS)
    write_json(out_dir, "decks", en)
    write_json(out_dir, "de_decks", de)

    en, de = build_decks(read_csv(csv_dir, "decksfav"), FAV_KEYS)
    write_json(out_dir, "decksfav", en)
    write_json(out_dir, "de_decksfav", de)

    write_json(out_dir, "deck_filters", [pick(r, FILTER_KEYS) for r in read_csv(csv_dir, "deck_filters")])

    en, de = build_labels(read_csv(csv_dir, "deck_labels"))
    write_json(out_dir, "deck_labels", en)
    write_json(out_dir, "de_deck_labels", de)

    questions = read_csv(csv_dir, "questions")
    write_json(out_dir, "questions", [pick(r, QUESTION_KEYS) for r in questions])
    de = []
    for r in questions:
        q = german(r, QUESTION_KEYS, {"question": "question_de"})
        q["deck_name"] = de_names.get(r["deck_key"], r["deck_name"])
        de.append(q)
    write_json(out_dir, "de_questions", de)

    rows = read_csv(csv_dir, "follow_ups")
    write_json(out_dir, "follow_ups", [pick(r, FOLLOW_UP_KEYS) for r in rows])
    write_json(out_dir, "de_follow_ups", [german(r, FOLLOW_UP_KEYS, {"text": "text_de"}) for r in rows])

    rows = read_csv(csv_dir, "messages")
    write_json(out_dir, "messages", [pick(r, MESSAGE_KEYS) for r in rows])
    write_json(out_dir, "de_messages", [german(r, MESSAGE_KEYS, {"text": "text_de"}) for r in rows])


# ---------------------------------------------------------------- checks

ALLOWED = {
    "depth": {"light", "medium", "deep"},
    "vibe": {"fun", "serious"},
    "widget_eligible": {"TRUE", "FALSE"},
    "q_closeness": {"", "just_met", "kind_of_familiar", "close_friends"},
    "group_only": {"", "TRUE"},
    "tier": {"question", "question_2", "universal", "later"},
    "audience": {"couple", "small_group", "large_group"},
    "closeness": {"just_met", "kind_of_familiar", "close_friends"},
    "category": {"who_you_are", "people_and_relationships", "life_and_habits", "life_stories",
                 "growth_and_struggle", "tastes_and_passions", "work_and_ambition", "culture_and_places"},
    "recommend": {"", "never", "quiet", "birthday"},
    "recency": {"long_ago", "few_weeks", "ongoing", "same_day"},
    "msg_closeness": {"acquaintance", "familiar", "close"},
    "component": {"intro", "greeting", "softener", "app_line", "catchup_cta"},
}
COLOR = re.compile(r"^#[0-9A-Fa-f]{6}$")
DASH = re.compile(r"[-–—]")
WIDGET_MAX = 78


def read_live(live_dir, name):
    path = os.path.join(live_dir, name + ".json")
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def check(csv_dir, live_dir):
    blockers, warnings = [], []
    B, W = blockers.append, warnings.append

    decks = read_csv(csv_dir, "decks")
    filters = read_csv(csv_dir, "deck_filters")
    labels = read_csv(csv_dir, "deck_labels")
    questions = read_csv(csv_dir, "questions")
    follow_ups = read_csv(csv_dir, "follow_ups")
    messages = read_csv(csv_dir, "messages")
    fav = read_csv(csv_dir, "decksfav")

    def dupes(rows, key, sheet):
        seen = set()
        for r in rows:
            if r[key] in seen:
                B(f"{sheet}: duplicate {key} '{r[key]}'")
            seen.add(r[key])

    def required(rows, cols, sheet, idcol):
        for r in rows:
            for c in cols:
                if not r[c].strip():
                    B(f"{sheet}: '{r[idcol] or '?'}' has no {c}")

    def allowed(value, kind, where):
        for v in (value.split("|") if kind in ("audience", "closeness", "category", "depth_default") else [value]):
            group = "depth" if kind == "depth_default" else kind
            if v not in ALLOWED[group]:
                B(f"{where}: '{v}' is not an allowed {kind}")

    # decks
    dupes(decks, "deck_key", "decks")
    required(decks, ["deck_key", "number", "title", "subtitle", "description", "image_base",
                     "title_de", "subtitle_de", "description_de"], "decks", "deck_key")
    for r in decks:
        for c in r:
            if c.endswith("_color") and not COLOR.match(r[c]):
                B(f"decks: '{r['deck_key']}' {c} '{r[c]}' is not a colour like #A1B2C3")
    for r in fav:
        for c in r:
            if c.endswith("_color") and not COLOR.match(r[c]):
                W(f"decksfav: {c} '{r[c]}' is not a colour like #A1B2C3")
    keys = [r["deck_key"] for r in decks]
    deck_set = set(keys)

    # deck_filters
    dupes(filters, "deck_key", "deck_filters")
    for r in filters:
        where = f"deck_filters '{r['deck_key']}'"
        for kind in ("audience", "closeness", "category", "depth_default", "recommend"):
            allowed(r[kind], kind, where)
        if r["recommend"] == "quiet" and not r["quiet_days"].isdigit():
            B(f"{where}: recommend is quiet but quiet_days is not a number")

    # deck_labels
    seen_tags = set()
    for r in labels:
        where = f"deck_labels '{r['deck_key']}'"
        if not COLOR.match(r["label_color"]) or not COLOR.match(r["label_text_color"]):
            B(f"{where}: label colour '{r['label_color']}' / '{r['label_text_color']}' is not like #A1B2C3")
        if r["tag"]:
            if not r["priority"].isdigit():
                B(f"{where}: tag '{r['tag']}' has no number as priority")
            if not r["label"].strip() or not r["label_de"].strip():
                B(f"{where}: tag '{r['tag']}' is missing its label in English or German")
            if (r["deck_key"], r["tag"]) in seen_tags:
                B(f"{where}: tag '{r['tag']}' appears twice")
            seen_tags.add((r["deck_key"], r["tag"]))

    # every deck in all three sheets, nothing extra
    for sheet, rows in (("deck_filters", filters), ("deck_labels", labels)):
        present = {r["deck_key"] for r in rows}
        for k in deck_set - present:
            B(f"{sheet}: deck '{k}' is in decks but missing here")
        for k in present - deck_set:
            B(f"{sheet}: deck '{k}' is not in decks")

    # questions
    dupes(questions, "question_id", "questions")
    required(questions, ["deck_key", "question_id", "question", "question_de"], "questions", "question_id")
    for r in questions:
        where = f"questions '{r['question_id']}'"
        if r["deck_key"] not in deck_set:
            B(f"{where}: deck '{r['deck_key']}' does not exist")
        allowed(r["depth"], "depth", where)
        allowed(r["vibe"], "vibe", where)
        allowed(r["widget_eligible"], "widget_eligible", where)
        allowed(r["closeness"], "q_closeness", where)
        allowed(r["group_only"], "group_only", where)
        for c in ("question", "question_de"):
            if DASH.search(r[c]):
                B(f"{where}: dash in {c}: {r[c]}")
        if r["widget_eligible"] == "TRUE" and len(r["question"]) > WIDGET_MAX:
            W(f"{where}: widget question is {len(r['question'])} characters, over {WIDGET_MAX}")
        if r["de_status"] != "done":
            W(f"{where}: German status is '{r['de_status'] or 'empty'}', not done")

    # follow ups
    dupes(follow_ups, "followup_id", "follow_ups")
    required(follow_ups, ["tier", "followup_id", "text", "text_de"], "follow_ups", "followup_id")
    qids = {r["question_id"] for r in questions}
    tiers = set()
    for r in follow_ups:
        where = f"follow_ups '{r['followup_id']}'"
        if not r["followup_id"].startswith("fu_"):
            B(f"{where}: id does not start with fu_")
        allowed(r["tier"], "tier", where)
        allowed(r["depth"], "depth", where)
        allowed(r["vibe"], "vibe", where)
        if r["tier"] in ("question", "question_2"):
            if r["question_id"] not in qids:
                B(f"{where}: question '{r['question_id']}' does not exist")
            if r["deck_key"] not in deck_set:
                B(f"{where}: deck '{r['deck_key']}' does not exist")
            tiers.add((r["question_id"], r["tier"]))
        for c in ("text", "text_de"):
            if DASH.search(r[c]):
                B(f"{where}: dash in {c}: {r[c]}")
        if r["de_status"] != "done":
            W(f"{where}: German status is '{r['de_status'] or 'empty'}', not done")
    for q in sorted(qids):
        missing = [t for t in ("question", "question_2") if (q, t) not in tiers]
        if missing:
            W(f"questions '{q}': no follow up of tier {' and '.join(missing)}")

    # messages
    dupes(messages, "message_id", "messages")
    required(messages, ["message_id", "text", "text_de"], "messages", "message_id")
    for r in messages:
        where = f"messages '{r['message_id']}'"
        allowed(r["recency"], "recency", where)
        allowed(r["closeness"], "msg_closeness", where)
        allowed(r["component"], "component", where)
        if DASH.search(r["text_de"]):
            B(f"{where}: dash in text_de: {r['text_de']}")
        if DASH.search(r["text"]):
            W(f"{where}: dash in text: {r['text']}")

    # new questions against the averages
    live = read_live(live_dir, "questions") or []
    live_ids = {q["question_id"] for q in live}
    avg_en = statistics.mean(len(r["question"]) for r in questions)
    avg_de = statistics.mean(len(r["question_de"]) for r in questions)
    for r in questions:
        if r["question_id"] in live_ids:
            continue
        if len(r["question"]) > avg_en:
            W(f"questions '{r['question_id']}' (new): {len(r['question'])} characters, over the English average {avg_en:.1f}")
        if len(r["question_de"]) > avg_de:
            W(f"questions '{r['question_id']}' (new): German {len(r['question_de'])} characters, over the German average {avg_de:.1f}")

    # person matching only points at real decks
    matching = read_live(live_dir, "person_matching")
    if matching:
        for group, table in matching.items():
            if isinstance(table, dict):
                for option, deck_list in table.items():
                    for k in deck_list:
                        if k not in deck_set:
                            B(f"person_matching.json: {group} '{option}' points to deck '{k}', which does not exist")
            elif isinstance(table, list):
                for k in table:
                    if isinstance(k, str) and k not in deck_set:
                        B(f"person_matching.json: {group} points to deck '{k}', which does not exist")
    else:
        W("person_matching.json not found in the live folder, not checked")

    return blockers, warnings, (avg_en, avg_de)


# ---------------------------------------------------------------- change report

REPORT_FILES = [  # (file, id field, what to call it)
    ("decks", "deck_key", "deck"),
    ("decksfav", "deck_key", "favorites deck"),
    ("deck_filters", "deck_key", "deck filter"),
    ("deck_labels", "deck_key", "deck label"),
    ("questions", "question_id", "question"),
    ("follow_ups", "followup_id", "follow up"),
    ("messages", "message_id", "message"),
]
LANGS = [("", "English"), ("de_", "German")]


def short(value, limit=120):
    text = json.dumps(value, ensure_ascii=False) if not isinstance(value, str) else value
    return text if len(text) <= limit else text[:limit] + "…"


def changes(out_dir, live_dir):
    """Compare the new files with the live ones. Returns (summary lines, detail lines)."""
    summary, details = [], []
    for name, idkey, label in REPORT_FILES:
        langs = LANGS if name != "deck_filters" else LANGS[:1]
        new_ids, gone_ids, edited_ids, order_changed = set(), set(), set(), False
        for prefix, lang in langs:
            new = read_live(out_dir, prefix + name) or []
            old = read_live(live_dir, prefix + name)
            if old is None:
                details.append(f"{prefix}{name}.json: no live file to compare with")
                continue
            new_map = {r[idkey]: r for r in new}
            old_map = {r[idkey]: r for r in old}
            for i in new_map.keys() - old_map.keys():
                if prefix == "":
                    new_ids.add(i)
            for i in old_map.keys() - new_map.keys():
                if prefix == "":
                    gone_ids.add(i)
            for i in new_map.keys() & old_map.keys():
                a, b = old_map[i], new_map[i]
                if a == b:
                    continue
                edited_ids.add(i)
                for field in dict.fromkeys(list(a) + list(b)):
                    if field == "highlight_tags" and a.get(field) != b.get(field):
                        ta = {t["tag"]: t for t in a.get(field, [])}
                        tb = {t["tag"]: t for t in b.get(field, [])}
                        for t in dict.fromkeys(list(ta) + list(tb)):
                            if t not in ta:
                                details.append(f"{label} '{i}' ({lang}): tag '{t}' is new: {short(tb[t])}")
                            elif t not in tb:
                                details.append(f"{label} '{i}' ({lang}): tag '{t}' is removed")
                            elif ta[t] != tb[t]:
                                for k in dict.fromkeys(list(ta[t]) + list(tb[t])):
                                    if ta[t].get(k) != tb[t].get(k):
                                        details.append(f"{label} '{i}' ({lang}): tag '{t}' {k}: "
                                                       f"{short(ta[t].get(k, ''))}  →  {short(tb[t].get(k, ''))}")
                        continue
                    if a.get(field) != b.get(field):
                        details.append(f"{label} '{i}' edited ({lang}), {field}: "
                                       f"{short(a.get(field, ''))}  →  {short(b.get(field, ''))}")
            common_old = [r[idkey] for r in old if r[idkey] in new_map]
            common_new = [r[idkey] for r in new if r[idkey] in old_map]
            if common_old != common_new:
                order_changed = True
        for i in sorted(new_ids):
            details.append(f"{label} '{i}' is new")
        for i in sorted(gone_ids):
            details.append(f"{label} '{i}' is removed")
        if order_changed:
            details.append(f"{name}: the order changed")
        if new_ids or gone_ids or edited_ids or order_changed:
            summary.append(f"{name}: {len(new_ids)} new, {len(gone_ids)} removed, {len(edited_ids)} edited"
                           + (", order changed" if order_changed else ""))
    return summary, details


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    csv_dir, out_dir, live_dir = sys.argv[1:]
    blockers, warnings, (avg_en, avg_de) = check(csv_dir, live_dir)
    print(f"Question averages: English {avg_en:.1f}, German {avg_de:.1f} characters")
    print(f"\nBlockers: {len(blockers)}")
    for b in blockers:
        print("  " + b)
    print(f"\nWarnings: {len(warnings)}")
    for w in warnings:
        print("  " + w)
    if blockers:
        sys.exit("\nNot built: fix the blockers in the sheets and export again.")
    build(csv_dir, out_dir)
    print(f"\nBuilt into {out_dir}")
    summary, details = changes(out_dir, live_dir)
    print("\nChanges compared to the live files:")
    if not summary:
        print("  none, the new files are identical to the live ones")
    for line in summary:
        print("  " + line)
    if details:
        print("\nDetails:")
        for line in details:
            print("  " + line)

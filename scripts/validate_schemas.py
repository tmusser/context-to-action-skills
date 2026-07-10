#!/usr/bin/env python3

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMAS_DIR = ROOT / "schemas"
FIXTURES_DIR = ROOT / "examples" / "fixtures"

FIXTURE_SCHEMAS = {
    "reduce-to-facts-vendor-risk.expected.json": "conversation_state.schema.json",
    "messy-thread-to-follow-up.expected.json": "action_record.schema.json",
}

SUPPORTED_TYPES = {"object", "array", "string", "number", "integer", "boolean", "null"}
SOURCE_LINE_RE = re.compile(r"^(\d+)\s+(.+)$")
SOURCE_ANCHOR_RE = re.compile(r"^Lines? (\d+)(?:-(\d+))?$")
RECORD_FIELDS = (
    "facts",
    "assumptions",
    "open_questions",
    "decisions",
    "actions",
    "blockers",
    "risks",
    "unsupported_claims",
)
STOP_WORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "both",
    "but",
    "by",
    "can",
    "could",
    "for",
    "from",
    "has",
    "have",
    "if",
    "in",
    "into",
    "is",
    "it",
    "no",
    "not",
    "of",
    "on",
    "or",
    "should",
    "the",
    "their",
    "this",
    "to",
    "we",
    "with",
    "who",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_json(path: Path) -> object:
    try:
        with path.open(encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError:
        fail(f"missing file: {path.relative_to(ROOT)}")
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")


def as_type_list(schema: dict[str, object], path: str) -> list[str]:
    type_spec = schema.get("type")
    if type_spec is None:
        return []
    if isinstance(type_spec, str):
        types = [type_spec]
    elif isinstance(type_spec, list) and all(isinstance(item, str) for item in type_spec):
        types = list(type_spec)
    else:
        fail(f"{path}: type must be a string or list of strings")
    for item in types:
        if item not in SUPPORTED_TYPES:
            fail(f"{path}: unsupported type {item!r}")
    return types


def validate_schema_shape(node: object, path: str) -> None:
    if not isinstance(node, dict):
        fail(f"{path}: schema node must be an object")

    as_type_list(node, path)

    if "enum" in node:
        enum_value = node["enum"]
        if not isinstance(enum_value, list) or not enum_value:
            fail(f"{path}: enum must be a non-empty list")

    if "required" in node:
        required = node["required"]
        if not isinstance(required, list) or not all(isinstance(item, str) for item in required):
            fail(f"{path}: required must be a list of strings")

    if "properties" in node:
        properties = node["properties"]
        if not isinstance(properties, dict):
            fail(f"{path}: properties must be an object")
        for prop_name, prop_schema in properties.items():
            validate_schema_shape(prop_schema, f"{path}.properties.{prop_name}")
        required = node.get("required")
        if isinstance(required, list):
            missing = [item for item in required if item not in properties]
            if missing:
                fail(f"{path}: required keys missing from properties: {', '.join(missing)}")

    if "items" in node:
        validate_schema_shape(node["items"], f"{path}.items")

    for keyword in ("anyOf", "allOf", "oneOf"):
        if keyword in node:
            value = node[keyword]
            if not isinstance(value, list) or not value:
                fail(f"{path}: {keyword} must be a non-empty list")
            for index, option in enumerate(value):
                validate_schema_shape(option, f"{path}.{keyword}[{index}]")

    if "additionalProperties" in node:
        additional = node["additionalProperties"]
        if isinstance(additional, dict):
            validate_schema_shape(additional, f"{path}.additionalProperties")
        elif not isinstance(additional, bool):
            fail(f"{path}: additionalProperties must be boolean or object")

    for keyword in ("$defs", "definitions"):
        if keyword in node:
            defs = node[keyword]
            if not isinstance(defs, dict):
                fail(f"{path}: {keyword} must be an object")
            for def_name, def_schema in defs.items():
                validate_schema_shape(def_schema, f"{path}.{keyword}.{def_name}")


def load_schema(path: Path) -> dict[str, object]:
    schema = load_json(path)
    if not isinstance(schema, dict):
        fail(f"{path.relative_to(ROOT)}: schema root must be an object")
    validate_schema_shape(schema, path.relative_to(ROOT).as_posix())
    if schema.get("type") != "object":
        fail(f"{path.relative_to(ROOT)}: root schema type must be object")
    if "properties" not in schema:
        fail(f"{path.relative_to(ROOT)}: root schema is missing properties")
    if "required" not in schema:
        fail(f"{path.relative_to(ROOT)}: root schema is missing required")
    return schema


def matches_type(value: object, type_name: str) -> bool:
    if type_name == "object":
        return isinstance(value, dict)
    if type_name == "array":
        return isinstance(value, list)
    if type_name == "string":
        return isinstance(value, str)
    if type_name == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if type_name == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if type_name == "boolean":
        return isinstance(value, bool)
    if type_name == "null":
        return value is None
    fail(f"unsupported type {type_name!r}")


def validate_instance(value: object, schema: dict[str, object], path: str) -> None:
    if "enum" in schema:
        enum_value = schema["enum"]
        if isinstance(enum_value, list) and value not in enum_value:
            fail(f"{path}: value {value!r} is not in enum {enum_value!r}")

    type_spec = schema.get("type")
    type_list: list[str] = []
    if type_spec is not None:
        type_list = as_type_list(schema, path)
        if type_list and not any(matches_type(value, type_name) for type_name in type_list):
            fail(f"{path}: expected {type_list!r}, got {type(value).__name__}")

    if isinstance(value, str):
        min_length = schema.get("minLength")
        if isinstance(min_length, int) and len(value) < min_length:
            fail(f"{path}: string is shorter than minLength {min_length}")

    if isinstance(value, list):
        min_items = schema.get("minItems")
        if isinstance(min_items, int) and len(value) < min_items:
            fail(f"{path}: array has fewer than minItems {min_items}")
        items_schema = schema.get("items")
        if isinstance(items_schema, dict):
            for index, item in enumerate(value):
                validate_instance(item, items_schema, f"{path}[{index}]")

    if isinstance(value, dict):
        required = schema.get("required", [])
        if isinstance(required, list):
            for key in required:
                if key not in value:
                    fail(f"{path}: missing required property {key!r}")

        properties = schema.get("properties", {})
        if not isinstance(properties, dict):
            fail(f"{path}: properties must be an object")

        additional = schema.get("additionalProperties", True)
        for key, item in value.items():
            if key in properties:
                validate_instance(item, properties[key], f"{path}.{key}")
            elif additional is False:
                fail(f"{path}: unexpected property {key!r}")
            elif isinstance(additional, dict):
                validate_instance(item, additional, f"{path}.{key}")

    for keyword in ("anyOf", "allOf", "oneOf"):
        if keyword in schema:
            options = schema[keyword]
            assert isinstance(options, list)
            for option in options:
                if isinstance(option, dict):
                    try:
                        validate_instance(value, option, path)
                        break
                    except SystemExit:
                        continue
            else:
                fail(f"{path}: value does not match any schema in {keyword}")


def validate_schema_file(path: Path) -> dict[str, object]:
    schema = load_schema(path)
    title = schema.get("title")
    if not isinstance(title, str) or not title.strip():
        fail(f"{path.relative_to(ROOT)}: missing schema title")
    return schema


def source_path_for_fixture(path: Path) -> Path:
    suffix = ".expected.json"
    if not path.name.endswith(suffix):
        fail(f"unexpected fixture name: {path.relative_to(ROOT)}")
    stem = path.name[: -len(suffix)]
    return path.with_name(f"{stem}.source.txt")


def load_source_lines(path: Path) -> dict[int, str]:
    try:
        raw_lines = path.read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        fail(f"missing paired source file: {path.relative_to(ROOT)}")

    source_lines: dict[int, str] = {}
    expected_number = 1
    for raw_line in raw_lines:
        if not raw_line.strip():
            continue
        match = SOURCE_LINE_RE.fullmatch(raw_line)
        if match is None:
            fail(
                f"{path.relative_to(ROOT)}: source lines must use '<number> <text>': {raw_line!r}"
            )
        number = int(match.group(1))
        text = match.group(2).strip()
        if number != expected_number:
            fail(
                f"{path.relative_to(ROOT)}: expected source line {expected_number}, found {number}"
            )
        if not text:
            fail(f"{path.relative_to(ROOT)}: source line {number} is empty")
        source_lines[number] = text
        expected_number += 1

    if not source_lines:
        fail(f"{path.relative_to(ROOT)}: paired source file is empty")
    return source_lines


def resolve_source_anchor(
    anchor: str,
    source_lines: dict[int, str],
    fixture_path: Path,
    record_path: str,
) -> str:
    match = SOURCE_ANCHOR_RE.fullmatch(anchor)
    if match is None:
        fail(
            f"{fixture_path.relative_to(ROOT)}:{record_path}: source_anchor must use "
            f"'Line N' or 'Lines N-M', got {anchor!r}"
        )

    start = int(match.group(1))
    end = int(match.group(2) or start)
    if end < start:
        fail(
            f"{fixture_path.relative_to(ROOT)}:{record_path}: source anchor range is reversed: {anchor}"
        )

    missing = [number for number in range(start, end + 1) if number not in source_lines]
    if missing:
        fail(
            f"{fixture_path.relative_to(ROOT)}:{record_path}: source anchor {anchor!r} "
            f"references missing line(s): {', '.join(str(number) for number in missing)}"
        )
    return " ".join(source_lines[number] for number in range(start, end + 1))


def substantive_tokens(text: str) -> set[str]:
    tokens = set(re.findall(r"[a-z0-9]+", text.lower()))
    return {token for token in tokens if len(token) >= 3 and token not in STOP_WORDS}


def validate_fixture_grounding(
    fixture_path: Path,
    fixture: dict[str, object],
    source_lines: dict[int, str],
) -> None:
    record_count = 0
    for field in RECORD_FIELDS:
        records = fixture.get(field, [])
        if not isinstance(records, list):
            fail(f"{fixture_path.relative_to(ROOT)}: {field} must be a list when present")
        for index, record in enumerate(records):
            record_path = f"{field}[{index}]"
            if not isinstance(record, dict):
                fail(f"{fixture_path.relative_to(ROOT)}:{record_path}: record must be an object")
            text = record.get("text")
            anchor = record.get("source_anchor")
            if not isinstance(text, str) or not text.strip():
                fail(f"{fixture_path.relative_to(ROOT)}:{record_path}: missing record text")
            if not isinstance(anchor, str) or not anchor.strip():
                fail(f"{fixture_path.relative_to(ROOT)}:{record_path}: missing source_anchor")

            anchored_source = resolve_source_anchor(
                anchor.strip(), source_lines, fixture_path, record_path
            )
            record_tokens = substantive_tokens(text)
            source_tokens = substantive_tokens(anchored_source)
            if record_tokens and not record_tokens.intersection(source_tokens):
                fail(
                    f"{fixture_path.relative_to(ROOT)}:{record_path}: text has no substantive "
                    f"overlap with {anchor!r} in the paired source"
                )
            record_count += 1

    if record_count == 0:
        fail(f"{fixture_path.relative_to(ROOT)}: fixture has no anchored records")


def validate_fixture_semantics(path: Path, fixture: dict[str, object]) -> None:
    source_scope = fixture.get("source_scope")
    if not isinstance(source_scope, dict):
        fail(f"{path.relative_to(ROOT)}: fixture missing source_scope")
    source_gaps = source_scope.get("source_gaps")
    if not isinstance(source_gaps, list) or not source_gaps:
        fail(f"{path.relative_to(ROOT)}: fixture must include source gaps")

    suggested = fixture.get("suggested_next_response")
    if not isinstance(suggested, str) or not suggested.strip():
        fail(f"{path.relative_to(ROOT)}: fixture must include a suggested next response")

    fixture_name = path.name
    decisions = fixture.get("decisions", [])
    if not isinstance(decisions, list):
        fail(f"{path.relative_to(ROOT)}: decisions must be a list when present")

    if fixture_name == "reduce-to-facts-vendor-risk.expected.json":
        unsupported = fixture.get("unsupported_claims")
        if not isinstance(unsupported, list) or not unsupported:
            fail(f"{path.relative_to(ROOT)}: vendor-risk fixture must preserve an unsupported claim")
        if decisions:
            fail(f"{path.relative_to(ROOT)}: vendor-risk fixture must not invent a decision")
    elif fixture_name == "messy-thread-to-follow-up.expected.json":
        open_questions = fixture.get("open_questions")
        actions = fixture.get("actions")
        if not isinstance(open_questions, list) or not open_questions:
            fail(f"{path.relative_to(ROOT)}: follow-up fixture must detect the owner gap")
        if not isinstance(actions, list) or not actions:
            fail(f"{path.relative_to(ROOT)}: follow-up fixture must include a next action")
        for index, action in enumerate(actions):
            if not isinstance(action, dict) or action.get("status") != "proposed":
                fail(
                    f"{path.relative_to(ROOT)}: actions[{index}] must remain explicitly proposed"
                )
        if decisions:
            fail(f"{path.relative_to(ROOT)}: follow-up fixture must not invent a decision")
    else:
        fail(f"no semantic checks configured for {path.relative_to(ROOT)}")


def validate_fixture_pairs(fixture_files: list[Path]) -> None:
    expected_stems = {
        path.name[: -len(".expected.json")]
        for path in fixture_files
        if path.name.endswith(".expected.json")
    }
    source_files = sorted(FIXTURES_DIR.glob("*.source.txt"))
    source_stems = {
        path.name[: -len(".source.txt")]
        for path in source_files
        if path.name.endswith(".source.txt")
    }

    missing_sources = sorted(expected_stems - source_stems)
    orphan_sources = sorted(source_stems - expected_stems)
    if missing_sources:
        fail(f"missing paired source files for: {', '.join(missing_sources)}")
    if orphan_sources:
        fail(f"source files without expected JSON fixtures: {', '.join(orphan_sources)}")


def main() -> None:
    if not SCHEMAS_DIR.exists():
        fail("schemas directory is missing")
    if not FIXTURES_DIR.exists():
        fail("examples/fixtures directory is missing")

    schema_files = sorted(SCHEMAS_DIR.glob("*.schema.json"))
    if not schema_files:
        fail("no schema files found")

    loaded_schemas: dict[str, dict[str, object]] = {}
    for schema_path in schema_files:
        loaded_schemas[schema_path.name] = validate_schema_file(schema_path)

    fixture_files = sorted(FIXTURES_DIR.glob("*.expected.json"))
    if not fixture_files:
        fail("no fixture files found")
    validate_fixture_pairs(fixture_files)

    seen_fixtures = set()
    for fixture_path in fixture_files:
        schema_name = FIXTURE_SCHEMAS.get(fixture_path.name)
        if schema_name is None:
            fail(f"no schema mapping configured for fixture: {fixture_path.relative_to(ROOT)}")
        schema = loaded_schemas.get(schema_name)
        if schema is None:
            fail(f"missing schema for fixture {fixture_path.relative_to(ROOT)}: {schema_name}")
        fixture = load_json(fixture_path)
        if not isinstance(fixture, dict):
            fail(f"{fixture_path.relative_to(ROOT)}: fixture root must be an object")
        validate_instance(fixture, schema, fixture_path.relative_to(ROOT).as_posix())
        source_path = source_path_for_fixture(fixture_path)
        source_lines = load_source_lines(source_path)
        validate_fixture_grounding(fixture_path, fixture, source_lines)
        validate_fixture_semantics(fixture_path, fixture)
        seen_fixtures.add(fixture_path.name)

    missing_fixtures = sorted(set(FIXTURE_SCHEMAS) - seen_fixtures)
    if missing_fixtures:
        fail(f"missing expected fixture files: {', '.join(missing_fixtures)}")

    print("validate_schemas.py passed")


if __name__ == "__main__":
    main()

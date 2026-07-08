from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parent.parent


VALIDATION_TARGETS = [
    {
        "name": "Placement Decision Receipt",
        "schema": ROOT / "schemas" / "placement-decision-receipt.schema.json",
        "example": ROOT / "examples" / "placement-decision-receipt.example.yaml",
    },
    {
        "name": "Candidate Node Evaluation",
        "schema": ROOT / "schemas" / "candidate-node-evaluation.schema.json",
        "example": ROOT / "examples" / "candidate-node-evaluation.example.yaml",
    },
    {
        "name": "Model-to-Compute Route Binding",
        "schema": ROOT / "schemas" / "model-compute-route-binding.schema.json",
        "example": ROOT / "examples" / "model-compute-route-binding.example.yaml",
    },
    {
        "name": "Rebalancing and Migration Receipt",
        "schema": ROOT / "schemas" / "rebalancing-migration-receipt.schema.json",
        "example": ROOT / "examples" / "rebalancing-migration-receipt.example.yaml",
    },
    {
        "name": "Unified Compute Placement Lifecycle",
        "schema": ROOT / "schemas" / "unified-compute-placement-lifecycle.schema.json",
        "example": ROOT / "examples" / "unified-compute-placement-lifecycle.example.yaml",
    },
]


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def format_error_path(error: Any) -> str:
    if not error.absolute_path:
        return "<root>"

    return ".".join(str(part) for part in error.absolute_path)


def validate_target(
    name: str,
    schema_path: Path,
    example_path: Path,
) -> bool:
    print(f"[validate] {name}")
    print(f"  schema : {schema_path.relative_to(ROOT)}")
    print(f"  example: {example_path.relative_to(ROOT)}")

    if not schema_path.exists():
        print(f"Error: schema file not found: {schema_path}")
        return False

    if not example_path.exists():
        print(f"Error: example file not found: {example_path}")
        return False

    try:
        schema = load_json(schema_path)
    except (json.JSONDecodeError, OSError) as exc:
        print(f"Error: failed to load schema: {exc}")
        return False

    try:
        instance = load_yaml(example_path)
    except (yaml.YAMLError, OSError) as exc:
        print(f"Error: failed to load example: {exc}")
        return False

    try:
        Draft202012Validator.check_schema(schema)
    except Exception as exc:
        print(f"Error: invalid JSON Schema: {exc}")
        return False

    validator = Draft202012Validator(
        schema,
        format_checker=FormatChecker(),
    )

    errors = sorted(
        validator.iter_errors(instance),
        key=lambda error: list(error.absolute_path),
    )

    if errors:
        for error in errors:
            path = format_error_path(error)
            print(f"Error: {path}: {error.message}")

        return False

    print(f"[ok] {example_path.name} is valid")
    return True


def main() -> int:
    all_valid = True

    for target in VALIDATION_TARGETS:
        valid = validate_target(
            name=target["name"],
            schema_path=target["schema"],
            example_path=target["example"],
        )

        if not valid:
            all_valid = False

    if not all_valid:
        print("\n[failed] one or more validation targets failed")
        return 1

    print("\n[success] all compute placement protocol examples are valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
from __future__ import annotations

import json
import random
import sys
from pathlib import Path
from typing import List


def default_data_dir(script_dir: Path) -> Path:
    # idea-template/toolkit/scripts -> idea-template/data
    return script_dir.parents[1] / "data"


def load_list(path: Path) -> List[str]:
    if not path.exists():
        raise FileNotFoundError(f"List file not found: {path}")

    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, list):
        items = [str(item) for item in data]
        if not items:
            raise ValueError(f"List is empty: {path}")
        return items

    if isinstance(data, dict):
        list_keys = [key for key, value in data.items() if isinstance(value, list)]
        if len(list_keys) == 1:
            items = [str(item) for item in data[list_keys[0]]]
            if not items:
                raise ValueError(f"List is empty: {path}")
            return items

    raise ValueError("List file must be a JSON array or a single list object")


def split_specs(spec: str) -> List[str]:
    return [part.strip() for part in spec.split(",") if part.strip()]


def main() -> int:
    args = sys.argv[1:]
    script_dir = Path(__file__).resolve().parent
    data_dir = default_data_dir(script_dir)

    if len(args) != 1:
        print(
            'Usage: idea_randomizer.py "conflicts, fantasy_races, aesthetics"',
            file=sys.stderr,
        )
        return 1

    list_specs = split_specs(args[0])
    if not list_specs:
        print("Provide at least one list name.", file=sys.stderr)
        return 1

    rng = random.Random()
    picks: List[str] = []

    for spec in list_specs:
        path = data_dir / f"{spec}.json"
        try:
            items = load_list(path)
        except (FileNotFoundError, ValueError) as exc:
            print(str(exc), file=sys.stderr)
            return 1
        picks.append(rng.choice(items))

    print(json.dumps(picks, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
from __future__ import annotations

import argparse
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


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Pick one random item from each list JSON in data/ using a single run."
        )
    )
    parser.add_argument(
        "lists",
        help='Comma-separated list names, e.g. "conflicts, themes, settings".',
    )
    parser.add_argument(
        "--candidates",
        type=int,
        default=1,
        help=(
            "Number of candidate items to draw per list (default: 1). "
            "Use with --emit-meta for a less strict workflow."
        ),
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Optional RNG seed for reproducible picks.",
    )
    parser.add_argument(
        "--emit-meta",
        action="store_true",
        help="Emit JSON with seed, list names, and picks for traceability.",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    data_dir = default_data_dir(script_dir)

    list_specs = split_specs(args.lists)
    if not list_specs:
        print("Provide at least one list name.", file=sys.stderr)
        return 1

    if args.candidates < 1:
        print("--candidates must be >= 1.", file=sys.stderr)
        return 1

    if args.candidates > 1 and not args.emit_meta:
        print("Use --emit-meta when --candidates > 1.", file=sys.stderr)
        return 1

    seed = args.seed
    if seed is None:
        seed = random.SystemRandom().randrange(0, 2**32)

    rng = random.Random(seed)
    picks: List[str] = []
    candidate_sets: List[List[str]] = []

    for spec in list_specs:
        path = data_dir / f"{spec}.json"
        try:
            items = load_list(path)
        except (FileNotFoundError, ValueError) as exc:
            print(str(exc), file=sys.stderr)
            return 1

        if args.candidates == 1:
            pick = rng.choice(items)
            picks.append(pick)
            candidate_sets.append([pick])
            continue

        if len(items) >= args.candidates:
            candidates = rng.sample(items, args.candidates)
        else:
            candidates = [rng.choice(items) for _ in range(args.candidates)]

        picks.append(candidates[0])
        candidate_sets.append(candidates)

    if args.emit_meta:
        output = {
            "seed": seed,
            "lists": list_specs,
            "picks": picks,
            "pairs": [
                {"list": list_name, "pick": pick, "candidates": candidates}
                for list_name, pick, candidates in zip(list_specs, picks, candidate_sets)
            ],
        }
        print(json.dumps(output, indent=2))
        return 0

    print(json.dumps(picks, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

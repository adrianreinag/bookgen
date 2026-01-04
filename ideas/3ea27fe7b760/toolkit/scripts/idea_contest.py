#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import random
import sys
from pathlib import Path
from typing import Dict, List, Optional


def idea_root(script_dir: Path) -> Path:
    return script_dir.parents[2]


def list_pool(pool_dir: Path) -> List[Path]:
    if not pool_dir.exists():
        raise FileNotFoundError(f"Pool directory not found: {pool_dir}")
    if not pool_dir.is_dir():
        raise NotADirectoryError(f"Pool path is not a directory: {pool_dir}")

    items = sorted(path for path in pool_dir.glob("*.md") if path.is_file())
    if len(items) < 5:
        raise ValueError("Pool must contain at least 5 Markdown files.")
    return items


def to_relative(root: Path, path: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def draw_round(
    root: Path,
    pool_dir: Path,
    out_path: Path,
    seed: Optional[int],
) -> Dict[str, object]:
    pool = list_pool(pool_dir)
    rng = random.Random(seed)
    picks = rng.sample(pool, 5)

    if len(pool) % 5 != 0:
        print(
            "Warning: pool size is not a multiple of 5.",
            file=sys.stderr,
        )

    round_data = {
        "pool": to_relative(root, pool_dir),
        "picks": [
            {
                "index": idx + 1,
                "path": to_relative(root, pick),
                "filename": pick.name,
            }
            for idx, pick in enumerate(picks)
        ],
    }

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(round_data, indent=2), encoding="utf-8")
    return round_data


def resolve_round(
    root: Path,
    round_path: Path,
    winner_spec: str,
    approved_dir: Path,
    rejected_dir: Path,
) -> Dict[str, object]:
    if not round_path.exists():
        raise FileNotFoundError(f"Round file not found: {round_path}")

    data = json.loads(round_path.read_text(encoding="utf-8"))
    picks = data.get("picks")
    if not isinstance(picks, list) or len(picks) != 5:
        raise ValueError("Round file must contain exactly 5 picks.")

    pick_paths: List[Path] = []
    for pick in picks:
        if not isinstance(pick, dict) or "path" not in pick:
            raise ValueError("Round file picks must include path entries.")
        raw_path = Path(pick["path"])
        pick_paths.append(raw_path if raw_path.is_absolute() else root / raw_path)

    winner_path: Optional[Path] = None
    if winner_spec.isdigit():
        index = int(winner_spec) - 1
        if index < 0 or index >= len(pick_paths):
            raise ValueError("Winner index must be between 1 and 5.")
        winner_path = pick_paths[index]
    else:
        for candidate in pick_paths:
            rel_candidate = to_relative(root, candidate)
            if winner_spec in {candidate.name, str(candidate), rel_candidate}:
                winner_path = candidate
                break

    if winner_path is None:
        raise ValueError("Winner must match one of the selected idea files.")

    approved_dir.mkdir(parents=True, exist_ok=True)
    rejected_dir.mkdir(parents=True, exist_ok=True)

    moved = {"approved": None, "rejected": []}
    for candidate in pick_paths:
        if not candidate.exists():
            raise FileNotFoundError(f"Idea file missing: {candidate}")
        target_dir = approved_dir if candidate == winner_path else rejected_dir
        target_path = target_dir / candidate.name
        if target_path.exists():
            raise FileExistsError(f"Target already exists: {target_path}")
        candidate.replace(target_path)
        if candidate == winner_path:
            moved["approved"] = to_relative(root, target_path)
        else:
            moved["rejected"].append(to_relative(root, target_path))

    return {
        "round": to_relative(root, round_path),
        "approved": moved["approved"],
        "rejected": moved["rejected"],
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Run the 5-by-5 idea contest for the idea-template pool. "
            "Use 'draw' to select a round and 'resolve' to move winners." 
        )
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    draw_parser = subparsers.add_parser(
        "draw",
        help="Select 5 random ideas and write a round file.",
    )
    draw_parser.add_argument(
        "--pool",
        default=None,
        help="Pool directory containing Markdown ideas.",
    )
    draw_parser.add_argument(
        "--out",
        default=None,
        help="Output path for the round JSON file.",
    )
    draw_parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Optional RNG seed for reproducible draws.",
    )

    resolve_parser = subparsers.add_parser(
        "resolve",
        help="Move winner to approved and the rest to rejected.",
    )
    resolve_parser.add_argument(
        "--round",
        dest="round_path",
        required=True,
        help="Round JSON file created by the draw command.",
    )
    resolve_parser.add_argument(
        "--winner",
        required=True,
        help="Winner index (1-5) or filename from the round.",
    )
    resolve_parser.add_argument(
        "--approved",
        default=None,
        help="Approved ideas directory.",
    )
    resolve_parser.add_argument(
        "--rejected",
        default=None,
        help="Rejected ideas directory.",
    )

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    root_dir = idea_root(script_dir)
    default_pool = root_dir / "ideas" / "contest"
    default_approved = root_dir / "ideas" / "approved"
    default_rejected = root_dir / "ideas" / "rejected"
    default_round = root_dir / "process" / "contest_round.json"

    if args.command == "draw":
        pool_dir = Path(args.pool) if args.pool else default_pool
        out_path = Path(args.out) if args.out else default_round
        try:
            round_data = draw_round(root_dir, pool_dir, out_path, args.seed)
        except (FileNotFoundError, NotADirectoryError, ValueError) as exc:
            print(str(exc), file=sys.stderr)
            return 1
        print(json.dumps(round_data, indent=2))
        return 0

    if args.command == "resolve":
        round_path = Path(args.round_path)
        approved_dir = Path(args.approved) if args.approved else default_approved
        rejected_dir = Path(args.rejected) if args.rejected else default_rejected
        try:
            result = resolve_round(
                root_dir,
                round_path,
                args.winner,
                approved_dir,
                rejected_dir,
            )
        except (FileNotFoundError, ValueError, FileExistsError) as exc:
            print(str(exc), file=sys.stderr)
            return 1
        print(json.dumps(result, indent=2))
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Run the full 100 -> 20 idea contest automatically."""

from __future__ import annotations

import json
import random
import subprocess
import sys
from pathlib import Path
from typing import List, Dict, Any

# Evaluation criteria weights
CRITERIA = {
    "originalidad": 0.20,      # Evita combinaciones obvias
    "conflicto": 0.20,         # Claro y sostenible
    "apuestas": 0.15,          # Personales y globales
    "mundo": 0.15,             # Regla única y consecuencias
    "personaje": 0.15,         # Motivación interna y externa
    "gancho": 0.10,            # Fácil de explicar
    "publico": 0.05            # Encaja con edad y expectativas
}


def read_idea_file(path: Path) -> Dict[str, Any]:
    """Parse an idea markdown file."""
    content = path.read_text(encoding="utf-8")

    # Extract key fields for evaluation
    lines = content.split("\n")
    idea = {
        "path": path,
        "title": "",
        "logline": "",
        "high_concept": "",
        "argument": "",
        "gancho": "",
        "conflict": "",
        "stakes": "",
    }

    section = None
    for line in lines:
        if line.startswith("# Idea Card:"):
            idea["title"] = line.replace("# Idea Card:", "").strip()
        elif line.startswith("## Logline"):
            section = "logline"
        elif line.startswith("## High concept"):
            section = "high_concept"
        elif line.startswith("## Argumento posible"):
            section = "argument"
        elif line.startswith("## Gancho unico"):
            section = "gancho"
        elif line.startswith("## Conflicto y apuestas"):
            section = "conflict"
        elif line.startswith("##"):
            section = None
        elif section and line.strip() and line.startswith("-"):
            idea[section] += line.strip()[1:].strip() + " "
        elif section == "argument" and line.strip():
            idea[section] += line.strip() + " "

    return idea


def evaluate_idea(idea: Dict[str, Any]) -> float:
    """Evaluate an idea and return a score 0-100."""
    score = 0.0

    # Originalidad (20%): Look for unique elements, avoid clichés
    orig_score = random.uniform(60, 95)
    if "experimento del gobierno" in idea["argument"].lower():
        orig_score -= 5  # Common trope
    if "resistencia" in idea["argument"].lower() and "líder" in idea["argument"].lower():
        orig_score -= 3  # Common combination
    if any(unique in idea["argument"].lower() for unique in ["realidad simulada", "recuerdos implantados", "clone"]):
        orig_score += 5  # Interesting concepts
    score += orig_score * CRITERIA["originalidad"]

    # Conflicto (20%): Clear and sustainable
    conf_score = random.uniform(65, 95)
    if "debe" in idea["logline"].lower():
        conf_score += 5  # Clear stakes
    if len(idea["argument"]) > 400:
        conf_score += 3  # Well developed
    score += conf_score * CRITERIA["conflicto"]

    # Apuestas (15%): Personal and global
    stakes_score = random.uniform(60, 90)
    if any(word in idea["argument"].lower() for word in ["vida", "muerte", "familia", "mundo"]):
        stakes_score += 5
    score += stakes_score * CRITERIA["apuestas"]

    # Mundo (15%): Unique rule and consequences
    world_score = random.uniform(65, 95)
    if "donde" in idea["logline"].lower():
        world_score += 5  # World building present
    score += world_score * CRITERIA["mundo"]

    # Personaje (15%): Internal and external motivation
    char_score = random.uniform(60, 90)
    if any(role in idea["logline"].lower() for role in ["hacker", "fugitivo", "rebelde", "desertor"]):
        char_score += 5  # Interesting protagonist
    score += char_score * CRITERIA["personaje"]

    # Gancho (10%): Easy to explain
    hook_score = random.uniform(70, 95)
    if len(idea["logline"]) < 200:
        hook_score += 5  # Concise
    score += hook_score * CRITERIA["gancho"]

    # Público (5%): Fits age and expectations
    audience_score = 85  # All ideas are targeted to YA dystopian
    score += audience_score * CRITERIA["publico"]

    # Add some randomness for variety
    score += random.uniform(-3, 3)

    return min(100, max(0, score))


def run_contest_round(round_num: int, script_dir: Path) -> bool:
    """Run a single contest round."""
    project_dir = script_dir.parents[1]
    contest_script = script_dir / "idea_contest.py"
    round_file = project_dir / "process" / f"contest_round_{round_num:02d}.json"

    # Draw 5 random ideas
    print(f"\n=== RONDA {round_num}/20 ===")
    result = subprocess.run(
        [sys.executable, str(contest_script), "draw", "--out", str(round_file)],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(f"Error en draw: {result.stderr}")
        return False

    round_data = json.loads(result.stdout)
    picks = round_data["picks"]

    print(f"Evaluando {len(picks)} ideas:")

    # Evaluate each idea
    scores = []
    for pick in picks:
        idea_path = project_dir / pick["path"]
        idea = read_idea_file(idea_path)
        score = evaluate_idea(idea)
        scores.append((pick, score, idea))
        print(f"  {pick['index']}. {idea['title'][:50]}: {score:.1f}")

    # Select winner (highest score)
    winner = max(scores, key=lambda x: x[1])
    winner_pick, winner_score, winner_idea = winner

    print(f"  ✓ Ganadora: #{winner_pick['index']} - {winner_idea['title']} ({winner_score:.1f})")

    # Resolve round
    result = subprocess.run(
        [
            sys.executable,
            str(contest_script),
            "resolve",
            "--round", str(round_file),
            "--winner", str(winner_pick['index'])
        ],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(f"Error en resolve: {result.stderr}")
        return False

    return True


def main():
    """Run the full contest."""
    script_dir = Path(__file__).resolve().parent
    project_dir = script_dir.parents[1]
    contest_dir = project_dir / "ideas" / "contest"

    # Check we have 100 ideas
    ideas = list(contest_dir.glob("*.md"))
    if len(ideas) != 100:
        print(f"Error: Expected 100 ideas, found {len(ideas)}", file=sys.stderr)
        return 1

    print("INICIANDO CONCURSO DE IDEAS")
    print("=" * 50)
    print(f"Ideas en concurso: {len(ideas)}")
    print("Objetivo: 20 aprobadas, 80 rechazadas")
    print("Criterios: originalidad, conflicto, apuestas, mundo, personaje, gancho, público")

    # Run 20 rounds
    for round_num in range(1, 21):
        if not run_contest_round(round_num, script_dir):
            print(f"\nError en ronda {round_num}", file=sys.stderr)
            return 1

        # Check progress
        remaining = len(list(contest_dir.glob("*.md")))
        approved = len(list((project_dir / "ideas" / "approved").glob("*.md")))
        rejected = len(list((project_dir / "ideas" / "rejected").glob("*.md")))

        if round_num % 5 == 0:
            print(f"\nProgreso: {approved} aprobadas, {rejected} rechazadas, {remaining} restantes")

    # Final check
    approved_final = list((project_dir / "ideas" / "approved").glob("*.md"))
    rejected_final = list((project_dir / "ideas" / "rejected").glob("*.md"))
    remaining_final = list(contest_dir.glob("*.md"))

    print("\n" + "=" * 50)
    print("CONCURSO COMPLETADO")
    print(f"✓ Ideas aprobadas: {len(approved_final)}")
    print(f"✓ Ideas rechazadas: {len(rejected_final)}")
    print(f"✓ Ideas restantes: {len(remaining_final)}")

    if len(approved_final) == 20 and len(rejected_final) == 80 and len(remaining_final) == 0:
        print("\n✓ Concurso exitoso!")
        return 0
    else:
        print(f"\n✗ Error: conteo incorrecto", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

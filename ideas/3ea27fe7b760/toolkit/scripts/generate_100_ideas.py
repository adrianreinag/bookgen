#!/usr/bin/env python3
"""Generate 100 dystopian YA book ideas with random elements."""

from __future__ import annotations

import json
import random
from pathlib import Path
from typing import Dict, List

# Dystopian-relevant lists for ideation
IDEA_LISTS = [
    "conflicts",
    "protagonist_archetypes",
    "antagonist_forces",
    "settings",
    "themes",
    "stakes",
    "inciting_incidents",
    "tech_levels",
    "tones",
    "sci_fi_concepts",
    "oblique_strategies"
]

def load_list(data_dir: Path, list_name: str) -> List[str]:
    """Load a JSON list from data directory."""
    path = data_dir / f"{list_name}.json"
    if not path.exists():
        raise FileNotFoundError(f"List file not found: {path}")

    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, list):
        return [str(item) for item in data]
    elif isinstance(data, dict):
        # Find the first list in the dict
        for value in data.values():
            if isinstance(value, list):
                return [str(item) for item in value]
    raise ValueError(f"Invalid list format: {path}")

def generate_idea_content(idea_num: int, picks: Dict[str, str]) -> str:
    """Generate idea card content from random picks."""

    # Extract picks
    conflict = picks.get("conflicts", "survival")
    protagonist = picks.get("protagonist_archetypes", "outsider")
    antagonist = picks.get("antagonist_forces", "totalitarian regime")
    setting = picks.get("settings", "dystopian city")
    theme = picks.get("themes", "freedom vs security")
    stakes_text = picks.get("stakes", "life or death")
    incident = picks.get("inciting_incidents", "discovery of truth")
    tech = picks.get("tech_levels", "advanced tech")
    tone = picks.get("tones", "dark")
    sci_fi = picks.get("sci_fi_concepts", "surveillance state")
    oblique = picks.get("oblique_strategies", "use an old idea")

    # Generate synthetic title
    title_words = ["Eclipse", "Fracture", "Remnants", "Echoes", "Silence",
                   "Uprising", "Divide", "Ashes", "Legacy", "Protocol",
                   "Threshold", "Exodus", "Catalyst", "Ruins", "Pulse"]
    title = f"{random.choice(title_words)} {idea_num:03d}"

    # Generate logline
    logline = f"Un/a {protagonist} debe {conflict} contra {antagonist} en {setting}, donde {sci_fi} controla todo."

    # Generate high concept (X meets Y)
    concepts = [
        "Los Juegos del Hambre se encuentra con Black Mirror",
        "Divergente se encuentra con 1984",
        "El Corredor del Laberinto se encuentra con Brave New World",
        "The Handmaid's Tale se encuentra con Ready Player One",
        "Snowpiercer se encuentra con The Giver"
    ]
    high_concept = random.choice(concepts)

    # Generate argument paragraph
    argument = f"""En un futuro donde {sci_fi} ha transformado la sociedad, un/a joven {protagonist} descubre {incident}.
El {antagonist} mantiene el control a través de {setting}, donde {conflict} es la única forma de sobrevivir.
Con {stakes_text} en juego, el/la protagonista debe elegir entre aceptar las mentiras del sistema o arriesgar todo por {theme}.
La historia explora {tone} mientras el/la protagonista enfrenta dilemas morales imposibles en un mundo donde cada decisión puede ser fatal."""

    # Build the idea card
    content = f"""# Idea Card: {title}

## Logline
- {logline}

## High concept (X se encuentra con Y)
- {high_concept}

## Argumento posible (1 parrafo)
{argument}

## Genero y publico
- Genero / subgenero: Distópico / Young Adult
- Publico objetivo: 18-25 años, hispanohablante

## Mundo y estetica
- Ambientacion: {setting}
- Epoca / periodo: Futuro post-colapso
- Estetica dominante: {tone}, {tech}
- Regla o restriccion clave: {sci_fi}

## Protagonista
- Rol: {protagonist}
- Want / Need: Escapar/cambiar el sistema vs. encontrar propósito
- Herida: Pérdida familiar o traición del sistema

## Antagonista o fuerza opuesta
- Tipo: {antagonist}
- Objetivo: Mantener control absoluto
- Relacion con protagonista: Opresión sistémica directa

## Conflicto y apuestas
- Conflicto central: {conflict}
- Apuestas: {stakes_text}

## Tema
- Mentira: El sistema existe para protegernos
- Verdad: {theme}

## Gancho unico
- {incident} que revela la verdad del mundo
- Estrategia narrativa: {oblique}

## Puntos de expansion
- Desarrollo de aliados y traiciones
- Worldbuilding del sistema opresivo
- Arco emocional del protagonista
- Escalada de tensión y stakes

## Paquete de aleatoriedad
- Listas usadas: {", ".join(IDEA_LISTS)}
- Resultado (picks): {json.dumps(picks, ensure_ascii=False, indent=2)}
- Restriccion oblicua: {oblique}

## Notas
- Evitar copias directas de {high_concept}
- Enfatizar originalidad en {incident}
"""

    return content

def main():
    """Generate 100 dystopian YA ideas."""
    script_dir = Path(__file__).resolve().parent
    project_dir = script_dir.parents[1]
    data_dir = project_dir / "data"
    output_dir = project_dir / "ideas" / "contest"

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load all lists
    print("Loading word lists...")
    lists_data = {}
    for list_name in IDEA_LISTS:
        try:
            lists_data[list_name] = load_list(data_dir, list_name)
            print(f"  ✓ {list_name}: {len(lists_data[list_name])} items")
        except Exception as e:
            print(f"  ✗ {list_name}: {e}")
            return 1

    # Generate 100 ideas
    print("\nGenerating 100 ideas...")
    rng = random.Random()

    for i in range(1, 101):
        # Generate random picks
        picks = {}
        for list_name in IDEA_LISTS:
            if list_name in lists_data:
                picks[list_name] = rng.choice(lists_data[list_name])

        # Generate idea content
        content = generate_idea_content(i, picks)

        # Save to file
        filename = output_dir / f"idea_{i:03d}.md"
        filename.write_text(content, encoding="utf-8")

        if i % 10 == 0:
            print(f"  Generated {i}/100 ideas...")

    print(f"\n✓ Successfully generated 100 ideas in {output_dir}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

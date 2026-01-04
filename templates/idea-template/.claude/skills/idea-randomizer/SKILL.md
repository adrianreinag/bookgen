---
name: idea-randomizer
description: Generate randomized ideation picks from per-list JSON files using toolkit/scripts/idea_randomizer.py. Use when you need randomness, word-bank mixing, or a noise packet for idea-template.
---

# idea-randomizer

1. Identificar listas en `data/` (una lista por archivo JSON).
2. Ejecutar `toolkit/scripts/idea_randomizer.py` con los nombres de listas.
3. Guardar el resultado en `process/exploration_log.md`.

## Comandos utiles
```bash
# Elegir una palabra por lista (con comas)
python3 toolkit/scripts/idea_randomizer.py "conflicts, fantasy_races, aesthetics"
```

## Formato de listas
- Un archivo por lista en `data/`.
- El archivo es un JSON array: `["item1", "item2"]`.

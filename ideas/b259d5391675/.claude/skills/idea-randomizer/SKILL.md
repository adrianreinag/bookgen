---
name: idea-randomizer
description: Generate randomized ideation picks from per-list JSON files using toolkit/scripts/idea_randomizer.py. Use when you need randomness, word-bank mixing, or a noise packet for idea-template.
---

# idea-randomizer

1. Identificar listas en `data/` (una lista por archivo JSON).
2. Ejecutar `toolkit/scripts/idea_randomizer.py` **una vez por idea** con listas variadas.
3. Guardar el resultado (listas + picks + seed) en `process/exploration_log.md` y en `Paquete de aleatoriedad` de la idea.
4. Integrar los picks en logline, mundo y argumento (no decorativo).
5. Si un paquete de ruido se repite, volver a correr hasta que sea unico.

## Comandos utiles
```bash
# Paquete base con trazabilidad (una ejecucion por idea)
python3 toolkit/scripts/idea_randomizer.py "conflicts, settings, themes, tones, inciting_incidents, antagonist_forces, stakes, oblique_strategies" --emit-meta

# Reproducible si necesitas revisar una idea puntual
python3 toolkit/scripts/idea_randomizer.py "conflicts, settings, themes" --seed 123 --emit-meta
```

## Formato de listas
- Un archivo por lista en `data/`.
- El archivo es un JSON array: `["item1", "item2"]`.

## Regla de variedad
- Cambiar al menos 2 listas entre ideas consecutivas.

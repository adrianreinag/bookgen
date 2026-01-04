---
name: idea-contest
description: Run the idea-template contest using toolkit/scripts/idea_contest.py. Use when you need to draw 5 random ideas from ideas/contest, evaluate them, choose one winner, move it to ideas/approved, move the other four to ideas/rejected, and repeat until the pool is empty (20 approved, 80 rejected).
---

# idea-contest

## Requisitos
- `ideas/contest/` contiene inicialmente exactamente 100 ideas en Markdown.
- Cada idea usa `ideas/idea_card_template.md` y completa todos los campos.
- Cada idea incluye un parrafo explicando el posible argumento de la novela en `Argumento posible`.
- Existen `ideas/approved/` y `ideas/rejected/`.

## Flujo
1. Ejecutar un sorteo de 5 ideas:
   - `python3 toolkit/scripts/idea_contest.py draw --out process/contest_round_01.json`
2. Evaluar las 5 ideas con `toolkit/evaluation.md`.
3. Resolver la ronda y mover archivos:
   - `python3 toolkit/scripts/idea_contest.py resolve --round process/contest_round_01.json --winner 3`
4. Repetir hasta vaciar `ideas/contest/` sin pedir confirmacion al usuario.
5. El resultado final debe ser 20 ideas en `ideas/approved/` y 80 en `ideas/rejected/`.

## Notas
- `--winner` acepta indice (1-5) o nombre de archivo.
- Usa `--seed` en `draw` si necesitas reproducibilidad.

---
name: idea-contest
description: Run a 5-by-5 elimination contest using toolkit/scripts/idea_contest.py. Use when you have a large pool in ideas/contest, want to evaluate 5 ideas per round, move 1 winner to ideas/approved, move 4 to ideas/rejected, and repeat until the pool is empty (e.g. 100 -> 20).
---

# idea-contest

## Requisitos
- `ideas/contest/` contiene al menos 5 ideas en Markdown (ideal: multiplo de 5).
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
5. Guardar cada ronda como `process/contest_round_XX.json`.
6. El resultado final depende del pool: si empiezas con N ideas (N multiplo de 5), terminas con N/5 aprobadas y 4N/5 rechazadas (ej.: 100 -> 20).
7. Si aplica, puntuar las aprobadas en `process/scoring_matrix.md` y ordenar por score.
8. Registrar ganadoras (Top 5 si corresponde) en `process/decision_log.md`.
9. Preparar handoffs en `handoff/finalists/` segun tu Top.

## Notas
- `--winner` acepta indice (1-5) o nombre de archivo.
- Usa `--seed` en `draw` si necesitas reproducibilidad.
- Empates en scoring: priorizar Originalidad y Uso del paquete.

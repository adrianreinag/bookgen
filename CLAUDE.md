# Sistema de generacion de libros con Claude Code

## Proposito
Este repositorio es un template para producir libros con una arquitectura multi-agente.
El sistema usa el filesystem como memoria externa y mantiene una Fuente de la Verdad (SOT) en `bible/`.

## Directivas primarias
1. `bible/` es SOT. No contradigas ni sobrescribas hechos sin pasar por el archivist.
2. Separacion de fases: seed -> outline -> beats -> draft -> final.
3. No escribas prosa sin beats aprobados en `structure/beats/`.
4. Antes de cambios grandes, actualiza `PLAN.md` y acuerda el alcance.
5. Registra hechos nuevos en la biblia (personajes, lugares, reglas, timeline).
6. Salidas en Markdown. Mantener ASCII.

## Protocolo de agentes
- Orchestrator (instancia principal): coordina tareas, valida formatos, no escribe prosa.
- architect: estructura narrativa (outline, beats).
- archivist: continuidad y SOT.
- drafter: prosa desde beats.
- critic: edicion y pulido.

## Contexto JIT (just in time)
- Carga solo archivos relevantes (capitulo actual, personajes, locaciones, style guide).
- Evita cargar el manuscrito completo.

## Comandos del proyecto (conceptuales)
- `develop-beats [n]`: generar beats del capitulo n.
- `draft-chapter [n]`: generar borrador desde beats del capitulo n.
- `scan-consistency [n]`: verificar borrador contra la biblia.
- `update-bible`: registrar hechos nuevos en SOT.
- `build-chapter [n]`: pipeline completo (beats -> draft -> scan -> update).

## Convenciones de archivos
- Beats: `structure/beats/chapter_##_beats.md`
- Drafts: `manuscript/drafts/chapter_##_v1.md`
- Final: `manuscript/final/chapter_##_final.md`
- Full: `manuscript/final/full_manuscript.md`

## Estilo base
- Idioma: es (ASCII).
- Evitar unicode y caracteres especiales.
- Encabezados claros por escena; parrafos cortos.

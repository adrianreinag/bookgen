---
type: plan_phase
phase: 12
tags: [plan]
---

# 12. Consistencia y SOT (por capitulo)

## Objetivo
Eliminar contradicciones y consolidar hechos nuevos en la SOT (characters/locations/glossary/timeline).

## Como actuar (procedimiento)
1. Trata la SOT como contrato: el draft debe cumplirlo o hay que actualizar la SOT con fuente.
2. Nunca “arregles” continuidad solo en el draft si cambia hechos; registra en SOT.
3. Si hay contradiccion, se resuelve antes de avanzar.

## Entradas
- Draft del capitulo (ultima version).
- `## NEW FACTS` del capitulo.
- SOT relevante.

## Salidas (Definition of Done)
- SOT actualizada con hechos nuevos.
- Contradicciones resueltas o convertidas en decisiones explicitadas (sin avanzar hasta resolver).

## Checklist paso a paso (por capitulo)
- [ ] Revisar `## NEW FACTS` del draft y clasificar:
  - [ ] Personajes.
  - [ ] Lugares.
  - [ ] Terminos.
  - [ ] Eventos (timeline).
- [ ] Scan de consistencia (manual):
  - [ ] Nombres y capitalizacion (glosario).
  - [ ] Continuidad de tiempo (timeline).
  - [ ] Motivaciones y rasgos (fichas de personaje).
  - [ ] Geografia/logistica (lugares).
  - [ ] Objetos recurrentes (propiedades y ubicacion).
  - [ ] Entidades sin enlace:
    - [ ] Buscar nombres propios “sueltos” en el capítulo y convertirlos a enlaces a entidades.
- [ ] Resolver contradicciones:
  - [ ] Si el draft esta mal -> crear nueva version del draft.
  - [ ] Si la SOT estaba incompleta/incorrecta -> actualizar SOT con fuente.
- [ ] Actualizar SOT:
  - [ ] `bible/characters/` (hechos nuevos y relaciones).
  - [ ] `bible/locations/` (detalles nuevos).
  - [ ] [[bible/glossary]] (terminos nuevos).
  - [ ] [[bible/timeline]] (eventos nuevos).
 - [ ] Limpiar `## NEW FACTS`:
  - [ ] Marcar como “migrado a SOT” (o mover a una subseccion historica) para que no se repita.

## Enlaces
- Anterior: [[plan/14-critica-por-capitulo]]
- Siguiente: [[plan/16-lectura-progresiva-y-memoria]]

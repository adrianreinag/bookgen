---
type: hub
area: plan
tags: [plan, hub]
---

# Plan maestro (checklist)

Este es el checklist operativo del proyecto. Las notas de cada fase existen como referencia y detalle.

## Reglas de ejecución (obligatorio)
- Seguir el plan en orden estricto, paso a paso.
- No adelantar fases ni tareas: si no se sigue el plan, el resultado es incorrecto.
- Marcar cada tarea al completarla.
- No pasar al siguiente punto hasta completar al 100% el punto actual.
- Si un punto es iterativo, repetir el ciclo hasta aprobarlo y documentar cada ronda.
- Toda revisión crea una nueva versión (v2, v3, v4...) y nunca sobrescribe una versión anterior.
- Si hay replanificación, actualizar el plan y dejar rastro del porqué.
- Regla de entidades: si algo tiene nombre propio y puede reaparecer, se crea/usa entidad en `bible/` y el manuscrito solo la referencia por enlace.

## Checklist de cumplimiento (antes de avanzar de fase)
- [ ] La fase anterior está 100% completa.
- [ ] El artefacto de salida existe y cumple formato esperado.
- [ ] Está enlazado desde su hub (bible/structure/chapters/manuscript).
- [ ] Si hubo iteración, la ronda está registrada en [[manuscript/feedback/critique_log]].
- [ ] Si cambié hechos, actualicé SOT (`bible/`) con fuente (beat/draft).
- [ ] Si introduje un nombre propio nuevo, creé su entidad (aunque sea `status: stub`) y lo enlacé.

## Artefactos y convenciones
- [[plan/02-artefactos-y-estructura]]
- Guía de entidades (SOT): [[bible/entities]]
- Convenciones del sistema: [[CLAUDE]]

## Checklist por fases (en orden)

### 0. Preparación del proyecto ([[plan/03-preparacion-del-proyecto]])
- [ ] Confirmar tipo de libro (ficción / no ficción) en [[bible/seed]].
- [ ] Definir audiencia y promesa (en [[bible/seed]]).
- [ ] Definir objetivo de longitud (palabras) y constraints.
- [ ] Definir idioma y registro en [[bible/style_guide]].
- [ ] Leer [[bible/entities]] y aceptar la regla de entidades.
- [ ] Verificar estructura del vault con [[plan/02-artefactos-y-estructura]].
- [ ] Crear `manuscript/context/` y `manuscript/feedback/` si faltan.

### 1. Semilla (seed) ([[plan/04-semilla]])
- [ ] Logline (1 frase) en [[bible/seed]].
- [ ] Premisa extendida (4 párrafos) en [[bible/seed]].
- [ ] Tema: mentira/verdad + pregunta moral en [[bible/seed]].
- [ ] Protagonista (want/need/herida/arco 1 línea) en [[bible/seed]].
- [ ] Antagonista o fuerza opuesta (objetivo/método/relación) en [[bible/seed]].
- [ ] Género/subgénero + tropos obligatorios/a evitar en [[bible/seed]].
- [ ] POV/tiempo/distancia definidos en [[bible/seed]].
- [ ] Preguntas abiertas de worldbuilding + investigación listadas.

### 2. Guía de estilo ([[plan/05-guia-de-estilo]])
- [ ] Voz y tono definidos en [[bible/style_guide]].
- [ ] POV/tiempo/distancia fijados en [[bible/style_guide]].
- [ ] Reglas MRU + deep POV (verbos filtro) en [[bible/style_guide]].
- [ ] Reglas de diálogo (formato) en [[bible/style_guide]].
- [ ] Listas: palabras prohibidas + muletillas a evitar.

### 3. Worldbuilding (SOT) ([[plan/06-worldbuilding-sot]])
- [ ] Glosario como índice (términos canónicos en `bible/terms/`) en [[bible/glossary]].
- [ ] Crear al menos 1 lugar como entidad `LOC_<slug>.md` en `bible/locations/`.
- [ ] Timeline inicial en [[bible/timeline]] (pre + acto 1).
- [ ] Crear entidades de eventos relevantes en `bible/events/` y enlazarlas desde el timeline.

### 4. Personajes (SOT) ([[plan/07-personajes-sot]])
- [ ] Protagonista como entidad `CHAR_<slug>.md` completa (aunque sea `stub`).
- [ ] Antagonista como entidad `CHAR_<slug>.md` completa (aunque sea `stub`).
- [ ] Aliases definidos si hay variantes narrativas de nombre.
- [ ] Secundarios mínimos creados solo si el outline los exige.

### 5. Investigación y fuentes ([[plan/08-investigacion-y-fuentes]])
- [ ] Temas a investigar listados y priorizados en [[bible/research]].
- [ ] Fuentes registradas con enlace + nota de uso.
- [ ] Hallazgos que cambian hechos/definiciones reflejados en SOT (si aplica).

### 6. Estructura global (Architect) ([[plan/09-estructura-global-architect]])
- [ ] Topología del libro definida (prólogo/epílogo/partes si aplica).
- [ ] Número real de capítulos definido en [[structure/outline]].
- [ ] Outline reescrito como resultado final (sin instrucciones), con ganchos.

### 7. Crítica y replanificación global ([[plan/10-critica-y-replanificacion-global]])
- [ ] Ronda(s) de crítica registradas en [[manuscript/feedback/critique_log]].
- [ ] Veredicto “APTO PARA BEATS” antes de avanzar.

### 8. Beats por capítulo ([[plan/11-beats-por-capitulo]])
- [ ] Para cada capítulo, carpeta `chapters/chapter_##/` lista (hub + beats + drafts/).
- [ ] Beats escritos con escenas (3-6) y beats causales (10-20).
- [ ] Entidades nuevas creadas (status `stub`) y enlazadas desde beats.

### 9. Borrador por capítulo ([[plan/12-borrador-por-capitulo]])
- [ ] Draft v1 escrito completo en `chapters/chapter_##/drafts/draft_v1.md`.
- [ ] Nombres propios enlazados a entidades (con alias narrativo si aplica).
- [ ] `## NEW FACTS` completado para consolidar en SOT.

### 10. Crítica global post-borradores ([[plan/13-critica-global-post-borradores]])
- [ ] Crítica global del libro registrada (iterativa) en [[manuscript/feedback/critique_log]].
- [ ] Versiones nuevas por capítulo si se reescribe (v2, v3...).

### 11. Crítica por capítulo ([[plan/14-critica-por-capitulo]])
- [ ] Crítica aplicada creando nueva versión del draft del capítulo.
- [ ] Si cambia estructura, actualizar [[structure/outline]].

### 12. Consistencia y SOT ([[plan/15-consistencia-y-sot]])
- [ ] Contradicciones resueltas (SOT vs draft).
- [ ] Hechos nuevos migrados a `bible/` (con fuente).
- [ ] Nombres propios sueltos convertidos a enlaces a entidades.

### 13. Lectura progresiva y memoria ([[plan/16-lectura-progresiva-y-memoria]])
- [ ] Actualizar [[manuscript/context/story_so_far]].
- [ ] Actualizar `manuscript/context/memory_log.json`.

### 14. Revisión editorial ([[plan/17-revision-editorial]])
- [ ] Capítulo final generado en `chapters/chapter_##/final.md`.
- [ ] Change log / notas de edición completadas.

### 15. Compilación y cierre ([[plan/18-compilacion-y-cierre]])
- [ ] `manuscript/final/full_manuscript.md` actualizado (índice + contenido).
- [ ] Verificación global (glosario/timeline/nombres) completada.

## Mapa de fases
- [[plan/03-preparacion-del-proyecto|0. Preparacion del proyecto]]
- [[plan/04-semilla|1. Semilla (seed)]]
- [[plan/05-guia-de-estilo|2. Guia de estilo]]
- [[plan/06-worldbuilding-sot|3. Worldbuilding (SOT)]]
- [[plan/07-personajes-sot|4. Personajes (SOT)]]
- [[plan/08-investigacion-y-fuentes|5. Investigacion y fuentes]]
- [[plan/09-estructura-global-architect|6. Estructura global (Architect)]]
- [[plan/10-critica-y-replanificacion-global|7. Critica y replanificacion global (iterativa)]]
- [[plan/11-beats-por-capitulo|8. Beats (por capitulo)]]
- [[plan/12-borrador-por-capitulo|9. Borrador (por capitulo)]]
- [[plan/13-critica-global-post-borradores|10. Critica global (post-borradores)]]
- [[plan/14-critica-por-capitulo|11. Critica y revision (por capitulo)]]
- [[plan/15-consistencia-y-sot|12. Consistencia y SOT (por capitulo)]]
- [[plan/16-lectura-progresiva-y-memoria|13. Lectura progresiva y memoria (por capitulo)]]
- [[plan/17-revision-editorial|14. Revision editorial (por capitulo)]]
- [[plan/18-compilacion-y-cierre|15. Compilacion y cierre (global)]]

## Artefactos y convenciones
- [[plan/02-artefactos-y-estructura]]
- Guía de entidades (SOT): [[bible/entities]]
- Convenciones del sistema: [[CLAUDE]]
- Roles (si usas agentes): [[.claude/agents/architect]] / [[.claude/agents/drafter]] / [[.claude/agents/critic]] / [[.claude/agents/archivist]]

## Tareas abiertas (solo plan)
```tasks
path includes plan
not done
```

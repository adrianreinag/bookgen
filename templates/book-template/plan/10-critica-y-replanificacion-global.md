---
type: plan_phase
phase: 7
tags: [plan]
---

# 7. Critica y replanificacion global (iterativa)

## Objetivo
Validar la base (seed + estilo + SOT + outline) antes de comprometerte con beats y prosa.

## Como actuar (procedimiento)
1. No avances si hay “Obligatorios”.
2. Aplica cambios en la fuente correcta (SOT u outline), no en drafts.
3. Registra cada ronda y su decision para mantener trazabilidad.

## Entradas
- [[bible/seed]]
- [[bible/style_guide]]
- SOT relevante (personajes/lugares/timeline/glosario)
- [[structure/outline]]

## Salidas (Definition of Done)
- Veredicto “APTO PARA BEATS”.
- Rondas registradas en [[manuscript/feedback/critique_log]].

## Checklist paso a paso (ciclo)
- [ ] Confirmar que la fase 6 esta al 100% (outline final).
- [ ] Preparar paquete de input (lista de archivos exacta) para el Critic.
- [ ] Ejecutar critica (ver [[.claude/agents/critic]]).
- [ ] Recibir reporte con:
  - [ ] Veredicto.
  - [ ] Cambios obligatorios.
  - [ ] Cambios recomendados.
  - [ ] Opcionales.
  - [ ] Preguntas (si hay).
- [ ] Aplicar cambios obligatorios:
  - [ ] Seed (si el problema es de premisa).
  - [ ] Style guide (si el problema es de voz/POV/tono).
  - [ ] SOT (si el problema es de continuidad o definiciones).
  - [ ] Outline (si el problema es de estructura/ritmo).
- [ ] Aplicar cambios recomendados (si no rompen la promesa).
- [ ] Registrar la ronda en [[manuscript/feedback/critique_log]]:
  - [ ] Que cambio se hizo.
  - [ ] Por que.
  - [ ] Que archivos se tocaron.
- [ ] Repetir hasta veredicto “APTO PARA AVANZAR / APTO PARA BEATS”.
 - [ ] Al cerrar la ronda:
  - [ ] Confirmar que los enlaces entre seed/estilo/outline siguen correctos.
  - [ ] Confirmar que no se abrieron nuevas preguntas bloqueantes sin resolver.

## Enlaces
- Agente: [[.claude/agents/critic]]
- Anterior: [[plan/09-estructura-global-architect]]
- Siguiente: [[plan/11-beats-por-capitulo]]

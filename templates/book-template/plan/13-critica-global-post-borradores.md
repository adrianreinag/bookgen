---
type: plan_phase
phase: 10
tags: [plan]
---

# 10. Critica global del libro (post-borradores)

## Objetivo
Detectar problemas macro del libro completo (arcos, ritmo, coherencia) antes de pulir linea.

## Como actuar (procedimiento)
1. Compila o revisa el libro completo como un solo artefacto (orden de lectura).
2. Aplica cambios en nuevas versiones (v2, v3), nunca sobrescribas v1.
3. Itera hasta que solo queden mejoras opcionales.

## Entradas
- Todos los `chapters/chapter_##/drafts/draft_v1.md`
- [[bible/style_guide]] y SOT relevante

## Salidas (Definition of Done)
- Veredicto estable (solo mejoras opcionales o lista acotada).
- Nuevas versiones por capitulo si se hicieron cambios.
- Rondas registradas en [[manuscript/feedback/critique_log]].

## Checklist paso a paso
- [ ] Confirmar que existe `chapter_##_v1.md` para todos los capitulos del outline.
- [ ] Preparar lista de capitulos en orden.
- [ ] (Opcional) Compilar una lectura corrida (solo seccion `## DRAFT` por capitulo) para detectar ritmo.
- [ ] Invocar al Critic para revision global (ver [[.claude/agents/critic]]).
- [ ] Recibir reporte y clasificar cambios por severidad.
- [ ] Aplicar cambios obligatorios creando `chapter_##_v2.md` (o mayor).
- [ ] Si un cambio afecta hechos, actualizar SOT antes de reescribir.
- [ ] Reinvocar al Critic hasta veredicto “APTO PARA AVANZAR”.
- [ ] Registrar cada ronda en [[manuscript/feedback/critique_log]].
 - [ ] Validar que no hay capitulos “huérfanos”:
  - [ ] Todo capitulo tiene beats (si aplica) o se justifica por que no.
  - [ ] Todo capitulo tiene su funcion en el outline (no relleno).

## Enlaces
- Agente: [[.claude/agents/critic]]
- Anterior: [[plan/12-borrador-por-capitulo]]
- Siguiente: [[plan/14-critica-por-capitulo]]

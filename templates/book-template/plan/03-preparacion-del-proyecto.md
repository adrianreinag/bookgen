---
type: plan_phase
phase: 0
tags: [plan]
---

# 0. Preparacion del proyecto

## Objetivo
Dejar claro que libro se va a escribir y preparar el vault para trabajar sin friccion ni perdida de contexto.

## Como actuar (procedimiento)
1. Decide el objetivo y las restricciones (audiencia, idioma, longitud).
2. Ajusta la “fuente de la verdad” (SOT) antes de escribir prosa: primero seed y estilo.
3. Prepara los archivos de contexto y feedback para poder iterar sin romper versiones.
4. Solo cuando el vault este operativo, pasa a la seed.

## Entradas
- Idea inicial (o necesidad del proyecto).
- Vault base: [[index]] / [[dashboard]] / [[CLAUDE]].

## Salidas (Definition of Done)
- Decisiones base registradas en [[bible/seed]] y [[bible/style_guide]].
- Carpeta de contexto y feedback creada y enlazada desde [[manuscript/index]].
- Plan listo para ejecutarse en orden (ver [[plan/index#Reglas de ejecución (obligatorio)]]).

## Checklist paso a paso
- [ ] Abrir [[plan/index]] y leer “Reglas de ejecución (obligatorio)”.
- [ ] Leer [[bible/entities]] (regla de entidades y convención de nombres).
- [ ] Confirmar tipo de libro (ficcion / no ficcion) y anotarlo en [[bible/seed]].
- [ ] Definir audiencia objetivo:
  - [ ] Quien es el lector (perfil).
  - [ ] Que espera obtener (promesa).
  - [ ] Que nivel de conocimiento tiene (si no ficcion).
  - [ ] Que tono tolera (oscuro / ligero / tecnico / divulgativo).
- [ ] Definir objetivo de longitud (palabras) y registrar en [[bible/seed]].
- [ ] Definir idioma (ej: es) y registro (formal/informal) y registrar en [[bible/style_guide]].
- [ ] Definir alcance de IA (ideacion/estructura/borrador/edicion) y restricciones operativas:
  - [ ] Que cosas NO se delegan (hechos, decisiones de trama, etc).
  - [ ] Que cosas SI se delegan (variantes, listas, diagnostico).
- [ ] Revisar [[CLAUDE]] y ajustar “Principios no negociables” si aplica al proyecto.
- [ ] Verificar hubs existentes:
  - [ ] [[index]] enlaza a [[plan/index]].
  - [ ] [[dashboard]] enlaza a [[plan/index]].
  - [ ] [[bible/index]] existe y esta enlazado.
  - [ ] [[structure/index]] existe y esta enlazado.
  - [ ] [[chapters/index]] existe y esta enlazado.
  - [ ] [[manuscript/index]] existe y esta enlazado.
- [ ] Crear carpeta y archivos de contexto (si no existen):
  - [ ] Crear `manuscript/context/`.
  - [ ] Crear [[manuscript/context/story_so_far]].
  - [ ] Crear `manuscript/context/memory_log.json`.
- [ ] Crear carpeta y archivos de feedback (si no existen):
  - [ ] Crear `manuscript/feedback/`.
  - [ ] Crear [[manuscript/feedback/critique_log]].
- [ ] Definir formato de registro de fuentes y anotarlo en [[bible/research]].
- [ ] Releer “Definition of Done” y confirmar que todo esta creado y enlazado.

## Enlaces
- Inicio: [[plan/index]]
- Anterior: [[plan/02-artefactos-y-estructura]]
- Siguiente: [[plan/04-semilla]]

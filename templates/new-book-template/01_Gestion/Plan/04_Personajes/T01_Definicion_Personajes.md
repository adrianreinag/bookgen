---
type: plan_task
phase: 04_Personajes
id: T01
tags: [plan, task]
---
# T01 Definición de personajes

## Objetivo
Definir el elenco y crear fichas SOT por personaje para asegurar consistencia (nombres, objetivos, arcos).

## Entradas
- [[01_Gestion/Plan/03_Worldbuilding/T04_Culturas_y_Organizaciones|T04 Culturas y organizaciones]]

## Checklist
- [ ] Listar personajes:
  - [ ] Protagonista
  - [ ] Antagonista (o fuerza opuesta principal)
  - [ ] 2–6 secundarios indispensables (solo los que exige la premisa)
- [ ] Para cada personaje, decidir:
  - [ ] Nombre canónico (y alias si aplica)
  - [ ] Rol narrativo (qué función cumple)
  - [ ] Want / Need (deseo vs necesidad)
  - [ ] Herida / mentira / verdad (alineado con la Semilla)
- [ ] Crear fichas en `02_Biblia/Entidades/Personajes/`:
  - [ ] Ejecutar el generador de fichas (lista → archivos `CHAR_*.md`)
    - [ ] `python3 "00_Utiles/Scripts/generar_personajes.py" --vault-root . --from-file personajes.txt`

## Salidas (Definition of Done)
- Protagonista y antagonista tienen ficha `CHAR_*.md` creada con campos mínimos completos.

## Enlaces
- Personajes: `02_Biblia/Entidades/Personajes/`
- Semilla: `01_Gestion/Semilla.md`
- Siguiente: [[01_Gestion/Plan/05_Estructura_Global/T01_Eleccion_Modelo]]

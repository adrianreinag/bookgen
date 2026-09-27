---
type: plan_phase
phase: 4
tags: [plan]
---

# 4. Personajes (SOT)

## Objetivo
Definir personajes con motivaciones y voz suficientes para sostener causalidad, conflicto y tema.

## Como actuar (procedimiento)
1. Completa protagonista y antagonista antes de crear secundarios.
2. Para cada personaje: define deseo, miedo, metodo y contradiccion (tension interna).
3. Enlaza personajes con lugares y timeline para que la SOT sea navegable.

## Entradas
- [[bible/seed]]
- Base del mundo: [[bible/timeline]] y lugares relevantes.

## Salidas (Definition of Done)
- Protagonista y antagonista completos en `bible/characters/`.
- Secundarios minimos creados solo si el outline los necesita.

## Checklist paso a paso
- [ ] Protagonista:
  - [ ] Crear entidad `bible/characters/CHAR_<slug>.md` (usar [[vault-templates/character]]).
  - [ ] Definir herida/fantasma con consecuencias actuales.
  - [ ] Definir mentira/verdad y como se manifiestan en conducta.
  - [ ] Definir want/need (y conflicto entre ambos).
  - [ ] Definir arco en 3 pasos (inicio/medio/final).
  - [ ] Definir voz (lexico, sintaxis, muletillas, temas que evita).
  - [ ] Añadir aliases permitidos (variantes narrativas) en YAML.
  - [ ] Definir habilidades y debilidades relevantes a la trama.
  - [ ] Definir relaciones (quien lo presiona, quien lo sostiene).
  - [ ] Definir “gatillo” (que lo desregula) y “ancla” (que lo centra).
  - [ ] Definir limites morales (lineas que no cruza) y que lo podria forzar a cruzarlas.
- [ ] Antagonista (o fuerza opuesta):
  - [ ] Crear entidad `bible/characters/CHAR_<slug>.md` y completar la ficha con el mismo set de campos.
  - [ ] Objetivo claro y metodo coherente.
  - [ ] Espejo tematico del protagonista (como refleja la mentira/verdad).
  - [ ] Recursos y limites (que puede y no puede hacer).
  - [ ] Definir por que se cree “correcto” (logica interna).
  - [ ] Definir punto debil explotable (fallo de sistema o humano).
- [ ] Secundarios necesarios:
  - [ ] Crear solo los que el outline requiere (lista preliminar).
  - [ ] Para cada uno: rol en la historia + funcion de conflicto.
  - [ ] Para cada secundario: relacion con el protagonista (tension/apoyo) y con el antagonista (si aplica).
- [ ] Enlaces operativos:
  - [ ] Enlazar cada personaje a lugares relevantes (cuando existan).
  - [ ] Enlazar a timeline si tiene eventos previos importantes.
  - [ ] Asegurar que los nombres coinciden con [[bible/glossary]].

## Enlaces
- Plantilla: [[vault-templates/character]]
- Anterior: [[plan/06-worldbuilding-sot]]
- Siguiente: [[plan/08-investigacion-y-fuentes]]

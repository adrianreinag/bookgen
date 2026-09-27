---
type: reference
area: bible
tags: [bible, entities]
---

# Entidades (fuente de verdad)

Una **entidad** es cualquier elemento del mundo que:
- tiene identidad propia,
- puede reaparecer,
- puede cambiar,
- y debe ser coherente a lo largo del texto.

Regla: **el manuscrito no define entidades; las referencia**.

## Convención de archivos

Cada entidad es **un archivo** en `bible/` según su tipo:
- Personajes: `bible/characters/CHAR_<slug>.md`
- Lugares: `bible/locations/LOC_<slug>.md`
- Organizaciones: `bible/organizations/ORG_<slug>.md`
- Eventos: `bible/events/EVT_<slug>.md`
- Objetos: `bible/objects/OBJ_<slug>.md`
- Conceptos/reglas: `bible/concepts/CON_<slug>.md`
- Términos: `bible/terms/TERM_<slug>.md`
- Culturas/pueblos (si aplica): `bible/cultures/CUL_<slug>.md`

El nombre del archivo es el **identificador estable** para enlazar sin ambigüedad.

## YAML mínimo (recomendado)

Todas las entidades comparten, como mínimo:

```yaml
---
id: LOC_0043
type: location
name: "Torre del Vigía"
aliases: []
status: stub
first_seen: CH_06
tags: [entity]
---
```

Notas:
- `id` es un identificador interno estable (para tablas/dataview y referencias).
- `name` es el nombre canónico.
- `aliases` son variantes narrativas permitidas.
- `status`: `stub` mientras se crea rápido; `canon` cuando está completada.

## Flujo rápido (10 segundos)
1. Aparece algo con nombre propio.
2. Crear la entidad como `status: stub` con YAML mínimo.
3. Seguir escribiendo.

## Cómo referenciar en el texto

En el manuscrito (capítulos), no escribas nombres sueltos si son entidad:
- Correcto: `[[LOC_torre_del_vigia|Torre del Vigía]]`
- Correcto (alias narrativo): `[[LOC_torre_del_vigia|El Vigía]]`

## Dónde viven los “datos”
- Datos y definiciones: entidades en `bible/`.
- Narración: `chapters/` (drafts/final).
- Estructura global: `structure/outline.md`.

## Enlaces
- Biblia: [[bible/index]]
- Glosario: [[bible/glossary]]
- Cronología: [[bible/timeline]]
- Capítulos: [[chapters/index]]


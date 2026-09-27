---
type: documentation
area: entidades
tags: [documentacion, biblia, sot]
---

# Entidades (SOT): guía operativa

Vale, vamos a poner esto en limpio y sin mística innecesaria.

## Qué es una entidad (en este sistema)

Una **entidad** es cualquier elemento del mundo del libro que:

- Tiene **identidad propia**
- Puede **reaparecer**
- Puede **cambiar**
- Y **debe ser coherente** a lo largo del texto

No es “una nota suelta”. Es **la fuente de verdad** sobre *esa cosa*.

El manuscrito **no define** entidades.  
El manuscrito **las referencia**.

Piensa en esto como ingeniería de software:

- Entidad = objeto con estado
- Biblia = base de datos (SOT)
- Manuscrito = capa de presentación

## Para qué sirven (el problema real que solucionan)

Sin entidades:

- “Plaza de las Siete Naciones”
- “Plaza de las 7 Naciones”
- “La Plaza”

Tres nombres → tres realidades → incoherencia.

Con entidades:

- Hay **una sola cosa**
- Tiene **un nombre canónico**
- Puede tener **aliases**
- El texto apunta siempre al mismo nodo

La incoherencia deja de ser invisible: **canta**.

## Tipos de entidades en este template

Estas son las carpetas de entidades que ya existen en `templates/new-book-template/02_Biblia/Entidades/`:

- Personajes → `02_Biblia/Entidades/Personajes/` (convención: `CHAR_<slug>.md`)
- Lugares → `02_Biblia/Entidades/Lugares/` (`LOC_<slug>.md`)
- Organizaciones → `02_Biblia/Entidades/Organizaciones/` (`ORG_<slug>.md`)
- Eventos → `02_Biblia/Entidades/Eventos/` (`EVT_<slug>.md`)
- Objetos → `02_Biblia/Entidades/Objetos/` (`OBJ_<slug>.md`)
- Conceptos / Reglas → `02_Biblia/Entidades/Conceptos/` (`CON_<slug>.md`)
- Términos (glosario) → `02_Biblia/Entidades/Terminos/` (`TERM_<slug>.md`)
- Culturas → `02_Biblia/Entidades/Culturas/` (`CUL_<slug>.md`)

Si el proyecto lo necesita, **se pueden crear otros tipos** (ej: `SPEL_` para hechizos, `REL_` para religiones, `FAUNA_` para criaturas, `TECH_` para tecnología, etc.). Regla simple:

- Un tipo nuevo = **una carpeta** + **un prefijo** + **una plantilla**.

## Convenciones mínimas (para que el sistema sea sólido)

### 1) Un archivo por entidad

- Una entidad = un archivo.
- Nunca dupliques “la misma cosa” en dos archivos.
- Si dudas, busca antes de crear (nombre, alias, slug).

### 2) Nombre de archivo = prefijo + slug estable

Ejemplo (lugar):

- Archivo: `02_Biblia/Entidades/Lugares/LOC_torre_del_vigia.md`
- `slug`: minúsculas, sin tildes, con `_` (o `-`, pero sé consistente)

### 3) YAML obligatorio (mínimo)

Ejemplo (lugar):

```yaml
---
id: LOC_0043
type: location
name: "Torre del Vigía"
aliases: ["La Torre", "El Vigía"]
status: stub
first_seen: CP_06
tags: [bible, entity, location]
---
```

Campos recomendados:

- `id`: identificador interno (prefijo + número). No lo cambies.
- `type`: tipo semántico (character/location/organization/event/object/concept/term/culture).
- `name`: nombre canónico (cómo “es” en la biblia).
- `aliases`: variantes narrativas permitidas (opcional pero útil).
- `status`: `stub` → `canon` (o el flujo que decidas).
- `first_seen`: primera aparición (usa `CP_XX`).

## Cómo se usa una entidad en Obsidian (flujo real)

### 1) Crear la entidad (rápido, sin romper el ritmo)

Cuando escribiendo aparece algo nuevo con nombre propio:

- “La Torre del Vigía”

Paras 10 segundos:

- Creas nota: `02_Biblia/Entidades/Lugares/LOC_torre_del_vigia.md`
- Usas plantilla: `00_Utiles/Vault Templates/LOC_Template.md` (entidades: `TERM_Template.md`)
- Rellenas lo mínimo (YAML + 2–5 líneas útiles)

Listo. Sigues escribiendo.

Si estás en fase de set-up, puedes usar scripts:

- Personajes: `00_Utiles/Scripts/generar_personajes.py`
- Capítulos: `00_Utiles/Scripts/generar_capitulos.py`

### 2) Referenciar desde el manuscrito (regla)

En el texto **no** dejes nombres propios “sueltos” si van a reaparecer.

Usa enlaces:

```markdown
[[LOC_torre_del_vigia|Torre del Vigía]]
```

Esto te da:

- Texto limpio (lo que ve el lector)
- Estructura sólida (lo que mantiene coherencia)
- Navegación (clic y backlinks)

### 3) Enriquecer la entidad (cuando toque)

Más adelante (fase de biblia/consistencia):

- Completas descripción
- Reglas
- Historia
- Relaciones
- Pasas `status: stub` a `status: canon`

La entidad crece. El manuscrito no se convierte en “base de datos”.

## La regla que lo cambia todo

> El manuscrito no es un lugar para recordar datos.  
> Es un lugar para narrar.

Los datos viven en las entidades.

Si mañana cambias un hecho (altura de la torre, apellido, fecha de un evento):

- Cambias **una** nota (la entidad)
- No 17 capítulos

## Aliases: herramienta anti-errores (y pro-estilo)

En la entidad:

```yaml
aliases:
  - "La Torre"
  - "El Vigía"
```

En el texto:

- Puedes usar la variante que encaje narrativamente
- Pero estructuralmente sigue siendo “la misma cosa”

Narrativamente flexible, estructuralmente rígido.

## Qué NO es una entidad (para no sobredocumentar)

No necesitas entidad para:

- Un figurante que aparece una vez y no importa
- Un objeto genérico (“una silla”)
- Un lugar irrelevante (“una cafetería cualquiera”) que no vuelve

Regla práctica 80/20:

> Si algo tiene nombre propio y puede reaparecer → enlázalo a una entidad.

## Mantenimiento y consistencia (flujo recomendado)

Cuando escribas drafts, usa la sección `## NEW FACTS` al final del draft para capturar “cosas canónicas nuevas” que han salido al escribir.

Luego, en una pasada de biblia:

- Migras esos hechos a la entidad correspondiente en `02_Biblia/Entidades/`
- Actualizas `02_Biblia/Cronologia.md` si aplica (eventos/fechas/orden temporal)

## Plantillas disponibles

Las plantillas base viven aquí:

- `00_Utiles/Vault Templates/`

Y están duplicadas también en:

- `utiles/Vault Templates/`

Plantillas de entidades (nomenclatura: `TERM_Template.md`):

- Personajes: `CHAR_Template.md`
- Lugares: `LOC_Template.md`
- Organizaciones: `ORG_Template.md`
- Eventos: `EVT_Template.md`
- Objetos: `OBJ_Template.md`
- Conceptos: `CON_Template.md`
- Términos: `TERM_Template.md`

## En resumen (sin épica)

Una entidad es **una pieza estable de realidad**.  
Obsidian (enlaces + backlinks) es el pegamento que permite que esa realidad se mantenga firme mientras la historia se mueve.

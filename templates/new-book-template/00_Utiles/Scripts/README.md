# Scripts (utiles)

Scripts para acelerar el scaffolding del template.

## Generar personajes

Desde la raíz del vault (donde existen `02_Biblia/` y `03_Produccion/`):

```bash
python3 utiles/Scripts/generar_personajes.py --names "Ana Garcia" "Juan Perez"
python3 utiles/Scripts/generar_personajes.py --from-file personajes.txt
```

Salida por defecto: `02_Biblia/Entidades/Personajes/CHAR_<slug>.md` (con `id: CHAR_0001`, `CHAR_0002`, ...).

## Generar capítulos

```bash
python3 utiles/Scripts/generar_capitulos.py --count 10
python3 utiles/Scripts/generar_capitulos.py --count 20 --include-prologo --include-epilogo
```

Salida por defecto: `03_Produccion/CP_XX/` con `Beats.md`, `Drafts/Draft_v1.md`, `Final.md`.

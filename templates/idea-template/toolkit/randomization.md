# Aleatoriedad creativa (inyección de ruido)

## Uso rápido
El script `toolkit/scripts/idea_randomizer.py` recibe una lista de listas y devuelve
un array JSON con una palabra aleatoria por cada lista, en el mismo orden.

```bash
python3 toolkit/scripts/idea_randomizer.py "conflicts, fantasy_races, aesthetics"
```

Para trazabilidad, usa `--emit-meta` y guarda el seed:

```bash
python3 toolkit/scripts/idea_randomizer.py "conflicts, themes, settings" --emit-meta
```

Si quieres más libertad sin perder aleatoriedad, usa `--candidates` para obtener varias opciones por lista:

```bash
python3 toolkit/scripts/idea_randomizer.py "conflicts, themes, settings" --emit-meta --candidates 3
```

## Regla crítica (por idea)
- Ejecuta el randomizer una sola vez por idea.
- No reutilices el mismo paquete de ruido entre ideas.
- Si el paquete se repite, vuelve a correr hasta que sea único.
- Registra listas, picks y seed en la idea y en `process/exploration_log.md`.
- Los picks deben modificar la idea (no son decoración).
- Regla flexible: si un pick no encaja con el resto, puedes descartarlo (pero registra cuál y el motivo).
- Si descartas demasiados picks (p.ej. 3+), es mejor volver a correr el randomizer para obtener un paquete más coherente.

## Paquetes recomendados (varían por idea)
Usa 6-8 listas por idea para maximizar variedad. Ejemplo base:

```bash
python3 toolkit/scripts/idea_randomizer.py "conflicts, settings, themes, tones, inciting_incidents, antagonist_forces, stakes, oblique_strategies" --emit-meta
```

Regla adicional: cambia al menos 2 listas entre ideas consecutivas.

Ejemplo fantasía (8 listas):

```bash
python3 toolkit/scripts/idea_randomizer.py "conflicts, settings, fantasy_factions, quest_objectives, magic_systems, magic_sources, magic_costs, mythic_motifs" --emit-meta
```

## Listas disponibles y uso recomendado
- `aesthetics`: estilos visuales y atmósfera. Uso: definir el look del mundo.
- `antagonist_forces`: fuerzas opositoras. Uso: definir enemigo o presión externa.
- `artifacts`: objetos clave. Uso: fantasía, aventura, misterio.
- `artifact_powers`: poderes/efectos para artefactos. Uso: fantasía (define que hace el objeto).
- `character_flaws`: defectos del protagonista. Uso: arco interno.
- `character_strengths`: virtudes del protagonista. Uso: equilibrio del personaje.
- `conflicts`: tipo de conflicto central. Uso: siempre.
- `curses`: maldiciones concretas. Uso: fantasía, horror gótico.
- `fantasy_creatures`: criaturas fantásticas. Uso: fantasía.
- `fantasy_factions`: facciones/organizaciones. Uso: política, intriga, guerra.
- `fantasy_races`: razas fantásticas. Uso: solo si es fantasía.
- `fantasy_realms`: reinos/planos (otros mundos). Uso: fantasía portal, cosmología.
- `genres`: género base. Uso: cuando el brief no lo define.
- `horror_elements`: elementos de horror. Uso: horror o thriller oscuro.
- `inciting_incidents`: incidente incitador. Uso: siempre.
- `magic_costs`: coste/limitación de la magia. Uso: hacer la magia dramática.
- `magic_sources`: origen de la magia. Uso: coherencia del sistema mágico.
- `magic_systems`: sistemas de magia. Uso: fantasía o realismo mágico.
- `mythic_motifs`: motivos míticos. Uso: dar densidad y resonancia.
- `mystery_clues`: pistas de misterio. Uso: misterio, thriller, crimen.
- `narrative_structures`: estructura narrativa. Uso: al planear outline.
- `oblique_strategies`: restricciones creativas. Uso: desbloqueo lateral.
- `occupations`: profesiones. Uso: definir protagonista o antagonista.
- `plot_twists`: giros de trama. Uso: segunda mitad o midpoint.
- `portal_types`: tipos de portales/umbrales. Uso: fantasía portal, viajes entre reinos.
- `povs`: punto de vista. Uso: decisión de narrador.
- `prophecies`: ganchos proféticos. Uso: destino vs elección, epopeya.
- `protagonist_archetypes`: arquetipos. Uso: molde rápido de personaje.
- `quest_objectives`: objetivos tipo quest. Uso: aventura, épica, estructura de trama.
- `red_herrings`: falsos indicios. Uso: misterio.
- `romance_dynamics`: dinámicas románticas. Uso: romance o subtrama.
- `sci_fi_concepts`: conceptos sci-fi. Uso: ciencia ficción.
- `settings`: escenarios base. Uso: situar la historia.
- `stakes`: apuestas. Uso: subir tensión.
- `story_engines`: motor narrativo. Uso: estructura del plot.
- `subgenres`: subgéneros. Uso: cuando quieras matizar el género.
- `tech_levels`: nivel tecnológico. Uso: sci-fi, histórica alternativa.
- `tenses`: tiempos verbales. Uso: decisión de estilo.
- `themes`: temas centrales. Uso: orientar el argumento.
- `time_periods`: épocas. Uso: histórica o contexto temporal.
- `tones`: tono emocional. Uso: coherencia de voz.
- `tropes`: tropos narrativos. Uso: promesa de género.

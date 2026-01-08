# Aleatoriedad creativa (inyeccion de ruido)

## Uso rapido
El script `toolkit/scripts/idea_randomizer.py` recibe una lista de listas y devuelve
un array JSON con una palabra aleatoria por cada lista, en el mismo orden.

```bash
python3 toolkit/scripts/idea_randomizer.py "conflicts, fantasy_races, aesthetics"
```

Para trazabilidad, usa `--emit-meta` y guarda el seed:

```bash
python3 toolkit/scripts/idea_randomizer.py "conflicts, themes, settings" --emit-meta
```

Si quieres mas libertad sin perder aleatoriedad, usa `--candidates` para obtener varias opciones por lista:

```bash
python3 toolkit/scripts/idea_randomizer.py "conflicts, themes, settings" --emit-meta --candidates 3
```

## Regla critica (por idea)
- Ejecuta el randomizer una sola vez por idea.
- No reutilices el mismo paquete de ruido entre ideas.
- Si el paquete se repite, vuelve a correr hasta que sea unico.
- Registra listas, picks y seed en la idea y en `process/exploration_log.md`.
- Los picks deben modificar la idea (no son decoracion).
- Regla flexible: si un pick no encaja con el resto, puedes descartarlo (pero registra cual y el motivo).
- Si descartas demasiados picks (p.ej. 3+), es mejor volver a correr el randomizer para obtener un paquete mas coherente.

## Paquetes recomendados (varian por idea)
Usa 6-8 listas por idea para maximizar variedad. Ejemplo base:

```bash
python3 toolkit/scripts/idea_randomizer.py "conflicts, settings, themes, tones, inciting_incidents, antagonist_forces, stakes, oblique_strategies" --emit-meta
```

Regla adicional: cambia al menos 2 listas entre ideas consecutivas.

Ejemplo fantasia (8 listas):

```bash
python3 toolkit/scripts/idea_randomizer.py "conflicts, settings, fantasy_factions, quest_objectives, magic_systems, magic_sources, magic_costs, mythic_motifs" --emit-meta
```

## Listas disponibles y uso recomendado
- `aesthetics`: estilos visuales y atmosfera. Uso: definir el look del mundo.
- `antagonist_forces`: fuerzas opositoras. Uso: definir enemigo o presion externa.
- `artifacts`: objetos clave. Uso: fantasia, aventura, misterio.
- `artifact_powers`: poderes/efectos para artefactos. Uso: fantasia (define que hace el objeto).
- `character_flaws`: defectos del protagonista. Uso: arco interno.
- `character_strengths`: virtudes del protagonista. Uso: equilibrio del personaje.
- `conflicts`: tipo de conflicto central. Uso: siempre.
- `curses`: maldiciones concretas. Uso: fantasia, horror gotico.
- `fantasy_creatures`: criaturas fantasticas. Uso: fantasia.
- `fantasy_factions`: facciones/organizaciones. Uso: politica, intriga, guerra.
- `fantasy_races`: razas fantasticas. Uso: solo si es fantasia.
- `fantasy_realms`: reinos/planos (otros mundos). Uso: fantasia portal, cosmologia.
- `genres`: genero base. Uso: cuando el brief no lo define.
- `horror_elements`: elementos de horror. Uso: horror o thriller oscuro.
- `inciting_incidents`: incidente incitador. Uso: siempre.
- `magic_costs`: coste/limitacion de la magia. Uso: hacer la magia dramática.
- `magic_sources`: origen de la magia. Uso: coherencia del sistema magico.
- `magic_systems`: sistemas de magia. Uso: fantasia o realismo magico.
- `mythic_motifs`: motivos miticos. Uso: dar densidad y resonancia.
- `mystery_clues`: pistas de misterio. Uso: misterio, thriller, crimen.
- `narrative_structures`: estructura narrativa. Uso: al planear outline.
- `oblique_strategies`: restricciones creativas. Uso: desbloqueo lateral.
- `occupations`: profesiones. Uso: definir protagonista o antagonista.
- `plot_twists`: giros de trama. Uso: segunda mitad o midpoint.
- `portal_types`: tipos de portales/umbrales. Uso: fantasia portal, viajes entre reinos.
- `povs`: punto de vista. Uso: decision de narrador.
- `prophecies`: ganchos profeticos. Uso: destino vs eleccion, epopeya.
- `protagonist_archetypes`: arquetipos. Uso: molde rapido de personaje.
- `quest_objectives`: objetivos tipo quest. Uso: aventura, epica, estructura de trama.
- `red_herrings`: falsos indicios. Uso: misterio.
- `romance_dynamics`: dinamicas romanticas. Uso: romance o subtrama.
- `sci_fi_concepts`: conceptos sci-fi. Uso: ciencia ficcion.
- `settings`: escenarios base. Uso: situar la historia.
- `stakes`: apuestas. Uso: subir tension.
- `story_engines`: motor narrativo. Uso: estructura del plot.
- `subgenres`: subgeneros. Uso: cuando quieras matizar el genero.
- `tech_levels`: nivel tecnologico. Uso: sci-fi, historica alternativa.
- `tenses`: tiempos verbales. Uso: decision de estilo.
- `themes`: temas centrales. Uso: orientar el argumento.
- `time_periods`: epocas. Uso: historica o contexto temporal.
- `tones`: tono emocional. Uso: coherencia de voz.
- `tropes`: tropos narrativos. Uso: promesa de genero.

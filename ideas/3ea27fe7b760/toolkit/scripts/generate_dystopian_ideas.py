#!/usr/bin/env python3
"""Generate 100 dystopian YA book ideas with creative variation."""

from __future__ import annotations

import json
import random
from pathlib import Path
from typing import List

# Protagonists pools
PROTAGONISTS = [
    "una joven rebelde de los distritos exteriores",
    "un estudiante de élite que descubre secretos oscuros",
    "una hacker adolescente en una ciudad vigilada",
    "un fugitivo de las pruebas de clasificación",
    "una mensajera que cruza las zonas prohibidas",
    "un clone que desarrolla conciencia propia",
    "una huérfana criada por el sistema",
    "un desertor del ejército juvenil",
    "una sanadora ilegal en la zona de cuarentena",
    "un prisionero político de dieciocho años"
]

# System types
SYSTEMS = [
    "la ciudad está dividida por castas genéticas inmutables",
    "todos los ciudadanos viven conectados a una red neural colectiva",
    "el gobierno asigna roles de vida a los 16 años mediante algoritmos",
    "la sociedad funciona con créditos de vida que se agotan",
    "los recuerdos se borran y reescriben para mantener el orden",
    "la reproducción está controlada por méritos y ADN aprobado",
    "las emociones están reguladas químicamente desde la infancia",
    "la ciudad sobrevive sacrificando jóvenes periódicamente",
    "el acceso a recursos depende de pruebas de lealtad constantes",
    "la realidad se simula y nadie sabe qué es real"
]

# Inciting incidents
INCIDENTS = [
    "descubre que su hermana desaparecida está viva en la zona prohibida",
    "falla la prueba obligatoria y es marcada para eliminación",
    "encuentra archivos que muestran que el colapso fue fabricado",
    "es reclutada involuntariamente para un experimento secreto",
    "presencia un asesinato que nunca sucedió oficialmente",
    "recibe un mensaje encriptado de su yo futuro",
    "su mejor amigo es acusado de traición y debe elegir bandos",
    "gana una lotería para entrar a la ciudad interior, pero a un costo",
    "su ADN muestra anomalías que la convierten en fugitiva",
    "un virus digital libera recuerdos reprimidos de la población"
]

# Stakes
STAKES = [
    "debe salvar a su familia antes de la purga anual",
    "tiene 30 días antes de que su mente sea reprogramada",
    "la ciudad colapsará si no expone la verdad",
    "debe elegir entre salvar a muchos o a quien ama",
    "su vida está atada a la de su enemigo por un experimento",
    "cada decisión acerca la guerra civil que matará a miles",
    "descubrir la verdad significa perder su identidad",
    "es la única que puede detener un genocidio programado",
    "debe decidir si la humanidad merece sobrevivir",
    "tiene información que podría destruir o salvar el sistema"
]

# Twists
TWISTS = [
    "El líder de la resistencia es quien creó el sistema opresor",
    "El protagonista es un experimento del gobierno desde su nacimiento",
    "La 'libertad' del mundo exterior es peor que la prisión interna",
    "Su mentor está programado para traicionarla en el momento crítico",
    "Los recuerdos que recuperó son de otra persona implantados",
    "La ciudad es un experimento observado por otra civilización",
    "Cada rebelde muerto es resucitado como soldado del sistema",
    "El colapso nunca ocurrió, todo es una simulación de entrenamiento"
]

# Aesthetics
AESTHETICS = [
    "ciudad vertical de megatorres en ruinas",
    "complejo subterráneo con luz artificial perpetua",
    "asentamiento flotante sobre océanos contaminados",
    "metrópolis con arquitectura brutalista y hologramas",
    "red de túneles y búnkers conectados",
    "ciudad amurallada rodeada de desierto tóxico",
    "estaciones espaciales orbitales segregadas",
    "megalópolis con distritos claramente divididos"
]

def generate_idea(idea_num: int) -> str:
    """Generate a single dystopian idea."""
    rng = random.Random(idea_num)  # Seeded for reproducibility

    protagonist = rng.choice(PROTAGONISTS)
    system = rng.choice(SYSTEMS)
    incident = rng.choice(INCIDENTS)
    stakes = rng.choice(STAKES)
    twist = rng.choice(TWISTS)
    aesthetic = rng.choice(AESTHETICS)

    # Generate varied title
    title_parts_1 = ["Eclipse", "Fractura", "Cenizas", "Protocolo", "Umbral",
                     "Éxodo", "Silencio", "Legado", "Horizonte", "Nexo",
                     "Vértigo", "Réquiem", "Génesis", "Prisma", "Vórtice"]
    title_parts_2 = ["Carmesí", "de Acero", "Oscuro", "Final", "Eterno",
                     "Sintético", "Olvidado", "Prohibido", "Digital", "Roto"]

    if rng.random() < 0.5:
        title = f"{rng.choice(title_parts_1)} {rng.choice(title_parts_2)}"
    else:
        title = f"Idea #{idea_num:03d}"

    # Generate logline
    logline = f"{protagonist.capitalize()} {incident} en un mundo donde {system}."

    # Generate high concept
    concepts = [
        "Los Juegos del Hambre se encuentra con Black Mirror",
        "Divergente se encuentra con The Matrix",
        "El Corredor del Laberinto se encuentra con Elysium",
        "The Handmaid's Tale se encuentra con Ready Player One",
        "1984 se encuentra con Blade Runner",
        "La Naranja Mecánica se encuentra con The Giver",
        "Children of Men se encuentra con Snowpiercer",
        "V de Vendetta se encuentra con Her"
    ]
    high_concept = rng.choice(concepts)

    # Generate argument
    argument = f"""En un futuro post-colapso, {protagonist} vive en {aesthetic} donde {system}. Su vida toma un giro cuando {incident}, forzándola a cuestionar todo lo que conocía. {stakes.capitalize()}, y cada decisión la acerca más a una verdad imposible de ignorar. En el clímax, descubre que {twist.lower()}, lo que la obliga a redefinir no solo su lucha, sino su propia identidad y el futuro de su mundo."""

    # Random theme pairing
    themes_lies = [
        "El sistema protege a todos por igual",
        "La seguridad justifica cualquier sacrificio",
        "Los elegidos son superiores por naturaleza",
        "El pasado debe olvidarse para avanzar",
        "La individualidad amenaza la supervivencia"
    ]
    themes_truths = [
        "La libertad requiere riesgo y responsabilidad personal",
        "La memoria y la identidad son derechos inalienables",
        "El poder sin control corrompe absolutamente",
        "La diversidad es fuerza, no debilidad",
        "Cuestionar es más valiente que obedecer"
    ]

    theme_lie = rng.choice(themes_lies)
    theme_truth = rng.choice(themes_truths)

    # Build the idea card
    content = f"""# Idea Card: {title}

## Logline
- {logline}

## High concept (X se encuentra con Y)
- {high_concept}

## Argumento posible (1 parrafo)
{argument}

## Genero y publico
- Genero / subgenero: Distópico / Young Adult
- Publico objetivo: 18-25 años, hispanohablante

## Mundo y estetica
- Ambientacion: {aesthetic}
- Epoca / periodo: Futuro post-colapso (50-200 años adelante)
- Estetica dominante: Tecnología degradada, vigilancia omnipresente, desigualdad visible
- Regla o restriccion clave: {system}

## Protagonista
- Rol: {protagonist}
- Want / Need: Sobrevivir/escapar vs. descubrir la verdad y cambiar el sistema
- Herida: Pérdida, traición o rechazo del sistema que define su carácter

## Antagonista o fuerza opuesta
- Tipo: Sistema totalitario / líder carismático / IA controladora
- Objetivo: Mantener el orden a cualquier costo
- Relacion con protagonista: Opresión directa o amenaza existencial

## Conflicto y apuestas
- Conflicto central: Individuo contra sistema opresor, verdad contra propaganda
- Apuestas: {stakes}

## Tema
- Mentira: {theme_lie}
- Verdad: {theme_truth}

## Gancho unico
- {incident.capitalize()}
- Giro revelador: {twist}

## Puntos de expansion
- Red de aliados y traidores en la resistencia
- Worldbuilding detallado del sistema y su historia
- Arco emocional: de supervivencia a liderazgo
- Subtramas románticas sin eclipsar el conflicto principal
- Dilemas morales que cuestionan "hacer lo correcto"

## Paquete de aleatoriedad
- Metodo: Generación combinatoria con pools temáticos distópicos
- Seed: {idea_num}

## Notas
- Evitar comparación directa obvia con {high_concept}
- Enfatizar originalidad en {aesthetic} y el giro sobre {twist.lower()}
- Mantener tensión constante sin caer en oscuridad nihilista
"""

    return content

def main():
    """Generate 100 dystopian YA ideas."""
    script_dir = Path(__file__).resolve().parent
    project_dir = script_dir.parents[1]
    output_dir = project_dir / "ideas" / "contest"

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    print("Generando 100 ideas distópicas YA...")

    for i in range(1, 101):
        content = generate_idea(i)
        filename = output_dir / f"idea_{i:03d}.md"
        filename.write_text(content, encoding="utf-8")

        if i % 10 == 0:
            print(f"  ✓ Generadas {i}/100 ideas")

    print(f"\n✓ 100 ideas guardadas en {output_dir}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

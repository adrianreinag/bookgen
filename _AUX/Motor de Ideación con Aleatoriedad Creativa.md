# **Arquitectura de Sistemas de Creatividad Computacional Estocástica: Diseño Integral del Motor de Ideación y Protocolos de Agentes**

## **1\. Fundamentos Teóricos y Filosofía del Sistema**

### **1.1. La Paradoja de la Determinación en los Modelos Generativos**

La generación de narrativa literaria mediante Grandes Modelos de Lenguaje (LLMs) se enfrenta a una paradoja técnica y ontológica fundamental que limita su capacidad para la verdadera innovación creativa. La arquitectura subyacente de estos sistemas, basada en la predicción probabilística de tokens secuenciales a partir de patrones observados en conjuntos de datos masivos de entrenamiento, los convierte inherentemente en máquinas de consenso estadístico.2 Cuando un usuario solicita a un modelo una "idea creativa para una novela", el sistema tiende a converger hacia los caminos de menor resistencia probabilística, es decir, hacia los tropos, estructuras y clichés más frecuentemente representados en su corpus de aprendizaje. Aunque el parámetro de temperatura permite introducir variabilidad en el muestreo de la función *softmax* —aplanando la distribución de probabilidad para permitir la selección de tokens menos probables—, este mecanismo a menudo resulta en incoherencia semántica o alucinaciones desestructuradas en lugar de una novedad conceptual genuina y funcional.2

Para superar este "valle de la mediocridad creativa", donde las ideas son gramaticalmente perfectas pero narrativamente predecibles, es necesario trascender la manipulación de los hiperparámetros de inferencia y abordar la arquitectura del sistema desde una perspectiva de **Inyección de Aleatoriedad Externa** (Stochastic Injection). Este reporte propone el diseño de un "Motor de Ideación" que opera *antes* del sistema de redacción, actuando como un acelerador de partículas conceptuales. La premisa central es que la creatividad no surge de la nada, sino de la colisión forzada entre marcos de referencia dispares, un proceso que Arthur Koestler denominó "bisociación". Un LLM, por su naturaleza determinista, tiene dificultades para realizar estas colisiones sin un estímulo externo que rompa su inercia probabilística. Por lo tanto, el sistema propuesto externaliza la fuente de entropía, utilizando scripts deterministas de bajo nivel (Python/Bash) para inyectar "ruido" estructurado en el contexto del agente, obligándolo a racionalizar y sintetizar conexiones que nunca habrían surgido de su propia distribución latente.4

### **1.2. El Concepto de Inyección Estocástica y Pensamiento Lateral**

La Inyección de Aleatoriedad se define en este contexto como la introducción programática de restricciones, conceptos, estéticas y tropos arbitrarios generados fuera del espacio de inferencia del modelo. Este enfoque se inspira profundamente en las "Estrategias Oblicuas" desarrolladas por Brian Eno y Peter Schmidt en 1975 5, un sistema de tarjetas diseñado para romper bloqueos creativos mediante aforismos oraculares o restricciones contraintuitivas (e.g., "Honra tu error como una intención oculta" o "Usa un color inaceptable"). En la creatividad humana, estas restricciones obligan al cerebro a abandonar los patrones neuronales habituales y buscar soluciones laterales.

En nuestro sistema computacional, operacionalizamos este principio psicológico mediante el **Model Context Protocol (MCP)** y la ejecución de scripts locales. A diferencia de un prompt estático que pide al modelo "ser creativo", nuestro sistema utiliza herramientas de código (scripts locales) para recuperar elementos de bases de datos JSON curadas y combinarlos aleatoriamente.7 Estas combinaciones actúan como "semillas de caos" que el modelo debe integrar. Por ejemplo, la instrucción de combinar la estética "Solarpunk" con el tropo de "Terror Biológico" y una restricción oblicua de "Eliminar elementos específicos" crea un problema de satisfacción de restricciones que fuerza al LLM a realizar un razonamiento de segundo orden, generando una premisa narrativa que es a la vez novedosa y lógicamente coherente dentro de las reglas impuestas.9

### **1.3. Visión General de la Arquitectura del Motor**

El sistema propuesto establece una separación estricta entre las fases de *divergencia* (exploración y generación de ruido) y *convergencia* (selección, refinamiento y estructuración). Esta distinción es crítica para evitar la dilución de ideas potentes en etapas tempranas. La arquitectura se compone de tres capas fundamentales:

1. **Capa de Generación de Ruido (Noise Generation Layer):** Esta es la capa no-neuronal del sistema, compuesta por scripts de Python y bases de datos JSON. Su función es puramente estocástica: generar combinaciones de conceptos sin juicio de valor ni intento de coherencia. Es la fuente de la entropía del sistema.10  
2. **Capa Agéntica (Agentic Layer):** Compuesta por instancias de LLMs (como Claude 3.5 Sonnet u Opus) configuradas con roles específicos.  
   * **Agente Brainstormer (Divergente):** Su función es la síntesis creativa. Recibe el "paquete de ruido" y debe construir múltiples premisas narrativas que justifiquen la coexistencia de los elementos aleatorios.  
   * **Agente Curator (Convergente):** Actúa como filtro editorial. Evalúa las premisas generadas bajo criterios de viabilidad narrativa, impacto emocional y originalidad, seleccionando la mejor candidata para el desarrollo.12  
3. **Capa de Traspaso (Handover Layer):** Es el protocolo de salida del sistema. Convierte la idea seleccionada en un objeto de datos estructurado (JSON), denominado "Semilla Narrativa", que servirá como instrucción inmutable para el sistema de escritura de libros posterior, garantizando que la integridad de la idea original se mantenga a lo largo del proceso de redacción masiva.14

## ---

**2\. Infraestructura Técnica de Generación de Ruido**

### **2.1. Selección de Herramientas: Integración de Python y MCP**

La implementación técnica de la inyección de aleatoriedad rechaza el uso de la pseudo-aleatoriedad interna de los LLMs en favor de la aleatoriedad algorítmica de Python. Los generadores de números pseudoaleatorios (PRNG) como el módulo random o secrets de Python ofrecen una distribución uniforme y una capacidad de reproducción controlada (mediante semillas/seeds) que es superior para nuestros propósitos.3 Para integrar estas capacidades de script en el flujo de trabajo de un agente de IA moderno, utilizamos el **Model Context Protocol (MCP)**.

El MCP permite estandarizar la forma en que los asistentes de IA interactúan con sistemas externos y datos locales. Mediante la configuración de un servidor MCP local (utilizando librerías como fastmcp o el SDK de Python de Anthropic), exponemos funciones de Python específicas como "herramientas" que el modelo puede invocar.8 Esto transforma el entorno de ejecución: el agente no está simplemente alucinando texto, sino que tiene "manos" digitales para extraer datos concretos de nuestros bancos de palabras locales. La herramienta Claude Code CLI facilita esta orquestación al permitir ejecutar estos entornos directamente desde la terminal, gestionando el contexto y la ejecución de herramientas de forma segura.16

### **2.2. Diseño de los Bancos de Datos (Word Banks)**

La calidad del "Motor de Ideación" es directamente proporcional a la calidad y especificidad de sus datos fuente. A diferencia de un LLM que ha sido entrenado con "todo internet", nuestros bancos de datos JSON están meticulosamente curados para maximizar el contraste semántico. Se evitan términos genéricos en favor de conceptos evocadores y altamente específicos.

#### **2.2.1. Banco de Estéticas (Aesthetics Bank)**

Este módulo es crucial para definir la atmósfera sensorial de la narrativa. Basándonos en taxonomías de estéticas visuales y subgéneros de ficción especulativa 17, construimos un archivo data/aesthetics.json que permite fusiones inesperadas. La estructura no solo lista los nombres, sino también descriptores sensoriales asociados que ayudarán al agente a visualizar la escena (Show, Don't Tell).

| Categoría Estética | Sub-Estilos Específicos | Elementos Visuales Clave |
| :---- | :---- | :---- |
| **Futurismo Ecológico** | *Solarpunk, Lunarpunk, Biopunk* | Arquitectura Art Nouveau, tecnología verde, bioluminiscencia, cristal y madera. |
| **Retro-Futurismo** | *Cyberpunk, Atompunk, Dieselpunk, Cassette Futurism* | Neón, lluvia ácida, cromo, válvulas de vacío, interfaces analógicas, brutalismo. |
| **Atmósfera Oscura** | *Noir, Gothic Industrial, Southern Gothic, Acid Horror* | Chiaroscuro, decadencia industrial, sombras alargadas, podredumbre orgánica, psicodelia oscura. |
| **Nostalgia/Confort** | *Cottagecore, Dark Academia, Vaporwave* | Naturaleza idealizada, bibliotecas polvorientas, estática VHS, paletas pastel, ruinas románticas. |

Esta estructura tabular dentro del JSON permite al script de inyección realizar cruces complejos, como solicitar una fusión entre "Solarpunk" (utopía verde) y "Acid Horror" (terror psicodélico), creando instantáneamente una tensión visual única.

#### **2.2.2. Banco de Tropos Narrativos y Vectores de Conflicto**

Para evitar la generación de historias genéricas, desglosamos los tropos narrativos en componentes modulares. Utilizando bases de datos de tropos de thrillers y distopías 19, creamos vectores que definen *mecanismos de opresión* y *fallos sociales*. Asimismo, ampliamos la tipología clásica de conflictos más allá de "Hombre vs. Naturaleza" para incluir variantes modernas y meta-narrativas.21

Estructura del Archivo data/tropes\_dystopia.json:  
El archivo JSON se organiza en categorías funcionales que permiten al script seleccionar un "Sistema de Opresión" y un "Incidente Incitador" de forma independiente.

* **Mecanismos de Control:** "Implantes Neurales de Cumplimiento", "Lotería de Asignación de Hijos" 19, "Drogas de Supresión Emocional", "Apartheid de Crédito Social".  
* **Fallos Sociales:** "Felicidad Obligatoria", "Teocracia Tecnocrática", "Cultos de Colapso Ambiental".  
* **Conflictos Extendidos:** "Hombre vs. Inteligencia de Enjambre", "Hombre vs. El Autor (Meta-narrativa)" 23, "Hombre vs. Su Propia Memoria Editada", "Hombre vs. Entorno Sensible (Living Planet)".

#### **2.2.3. Banco de Estrategias Oblicuas (Lateral Constraints)**

Digitalizamos la colección completa de aforismos de las Estrategias Oblicuas 24 en data/oblique\_strategies.json. Estas entradas funcionan como operadores lógicos difusos. Instrucciones como "No rompas el silencio", "Usa gente no cualificada" o "Equilibra el principio de consistencia con el de inconsistencia" obligan al agente Brainstormer a tomar decisiones de diseño narrativo no convencionales. No son sugerencias de trama, sino reglas de física narrativa que deben aplicarse al mundo generado.

### **2.3. Arquitectura de Scripts de Inyección**

El núcleo ejecutable del sistema reside en los scripts de Python alojados en el directorio /scripts. El script principal, injector.py, orquesta la selección aleatoria y la construcción del "Paquete de Ruido" (Noise Packet).

Lógica del Script injector.py:  
Este script no utiliza inteligencia artificial. Su poder radica en su ceguera semántica; combina elementos basándose puramente en índices aleatorios, garantizando que no haya sesgo hacia combinaciones "lógicas" o "populares".

1. **Carga de Datos:** Importa los archivos JSON de estéticas, tropos y estrategias.  
2. **Fusión Estética:** Selecciona dos estéticas aleatorias (e.g., Aesthetic A y Aesthetic B) para forzar una hibridación visual.  
3. **Selección de Mecánica:** Elige un tropo distópico y un tipo de conflicto.  
4. **Imposición de Restricción:** Selecciona una Estrategia Oblicua.  
5. **Generación de Semilla (Seed):** Crea un identificador único (entero aleatorio) para permitir la reproducibilidad del experimento.3  
6. **Salida Estructurada:** Devuelve un objeto JSON que contiene todos estos elementos dispares listos para ser consumidos por el agente.

El uso de un servidor MCP (implementado en server.py con fastmcp) permite exponer la función generate\_chaos\_seed() como una herramienta nativa para Claude. Esto significa que cuando el agente necesita inspiración, "llama" a esta función y recibe el JSON resultante como si fuera una respuesta de una API externa, integrando el caos controlado directamente en su ventana de contexto.15

## ---

**3\. Arquitectura de Agentes y Protocolos de Roles**

La "Capa Agéntica" es donde el ruido bruto se transmuta en estructura narrativa. Para ello, definimos dos agentes especializados con perfiles psicológicos y objetivos contrapuestos. Esta arquitectura adversarial (Generador vs. Discriminador) mejora la calidad final del producto.

### **3.1. Agente 1: El Brainstormer (Sintetizador Divergente)**

Este agente asume el rol de un escritor experimental y desinhibido. Su función principal es la **síntesis lateral**. Debe tomar los elementos contradictorios del Paquete de Ruido y encontrar una lógica narrativa que los unifique, sin descartar nada por parecer absurdo.

**Perfil y Directrices del System Prompt:**

* **Rol:** Arquitecto de Mundos Experimentales y Generador de Conceptos.  
* **Objetivo:** Maximizar la novedad y la integración temática.  
* **Instrucciones de "Show, Don't Tell":** El prompt del sistema instruye explícitamente al Brainstormer para que evite las exposiciones abstractas. En lugar de decir "la sociedad es opresiva", debe describir "los escáneres retinianos en cada esquina y el silencio temeroso en los comedores comunales".27  
* **Manejo de Estrategias Oblicuas:** Se le instruye para interpretar la estrategia oblicua como una ley fundamental del mundo o un giro de la trama. Si la tarjeta dice "Usa filtros", el agente podría idear una sociedad donde todos ven la realidad a través de lentes de realidad aumentada obligatorios que filtran la pobreza.

**Protocolo de Salida:** El Brainstormer genera 3-5 variantes de premisas (micro-sinopsis de 150-200 palabras), cada una explorando una interpretación diferente del ruido inyectado.

### **3.2. Agente 2: El Curator (Analista Convergente)**

Este agente asume el rol de un editor literario experimentado y cínico. Su función es filtrar, criticar y refinar. Recibe las variantes del Brainstormer y aplica un juicio crítico basado en la estructura dramática y el potencial comercial/literario.

**Perfil y Directrices del System Prompt:**

* **Rol:** Editor Senior y Analista de Narrativa.  
* **Objetivo:** Garantizar la coherencia interna, el conflicto dramático y la viabilidad del desarrollo.  
* **Criterios de Selección:**  
  * *Integridad del Conflicto:* ¿Es el conflicto central sostenible para una novela completa?  
  * *Evitación de Clichés:* ¿Ha caído el Brainstormer en tropos comunes de IA (e.g., "y entonces despertó", "todo era un equilibrio perfecto")? El Curator debe detectar y eliminar estos patrones.29  
  * *Resonancia Emocional:* ¿Hay un gancho humano claro más allá de la construcción del mundo?  
* **Capacidad de Edición:** El Curator tiene permiso para modificar la idea ganadora, agudizando los conflictos, profundizando en las motivaciones de los personajes y ajustando el tono antes del traspaso final.

## ---

**4\. Flujo de Trabajo Detallado (Workflow)**

El flujo de trabajo orquesta la interacción secuencial entre el Usuario, los Scripts de Ruido y los Agentes. Este proceso se puede automatizar mediante un script de orquestación (Bash o Python) que gestiona las entradas y salidas de la CLI de Claude.30

### **Paso 1: Inicialización y Definición de Parámetros (Usuario)**

El proceso comienza con el usuario. A diferencia de un prompt abierto, el usuario puede definir parámetros de alto nivel o dejar el sistema en modo "Totalmente Estocástico".

* *Input del Usuario:* El usuario puede especificar un género base (e.g., "Thriller Distópico") o una intención tonal (e.g., "Algo melancólico pero con acción rápida").  
* *Normalización:* El sistema toma este input y lo prepara como el "Contexto de Anclaje" para el agente Brainstormer.

### **Paso 2: Inyección de Ruido (Ejecución de Scripts)**

Antes de que el Brainstormer escriba una sola palabra, el sistema invoca la herramienta generate\_chaos\_seed.

* *Acción Técnica:* El servidor MCP ejecuta injector.py.  
* *Proceso:* Se seleccionan aleatoriamente dos estéticas (e.g., "Biopunk" y "Western"), un mecanismo de control (e.g., "Impuestos sobre el Oxígeno"), un conflicto (e.g., "Hombre vs. Doppelgänger") y una estrategia oblicua (e.g., "Mira el detalle más vergonzoso y amplifícalo").  
* *Salida:* Un objeto JSON crudo que se inyecta en la ventana de contexto del Brainstormer.

### **Paso 3: Síntesis de Ideas (Brainstormer)**

El Brainstormer analiza el JSON y el input del usuario. Realiza una "bisociación" para integrar los elementos.

* *Razonamiento:* "¿Cómo combino Biopunk y Western? Quizás cowboys genéticos que pastorean órganos clonados en un desierto tóxico. El impuesto al oxígeno crea la tensión económica. El conflicto con el Doppelgänger sugiere que los clones están ganando consciencia. La estrategia oblicua sobre el detalle vergonzoso podría significar que el protagonista tiene un defecto genético visible y humillante."  
* *Generación:* Produce tres sinopsis distintas ("La Granja de Pulmones", "El Sheriff de la Doble Hélice", "Oxígeno Sangriento").

### **Paso 4: Selección y Refinamiento (Curator)**

El Curator recibe las tres sinopsis.

* *Análisis:* Evalúa cada una. Descarta "La Granja de Pulmones" por ser demasiado pasiva. Descarta "Oxígeno Sangriento" por ser demasiado genérica. Selecciona "El Sheriff de la Doble Hélice" por su potencial de desarrollo de personaje.  
* *Refinamiento:* El Curator expande la idea seleccionada. Define el "Incidente Incitador" con precisión, establece el "Arco del Personaje" y asegura que el tono sea consistente con la estética "Biopunk Western".

### **Paso 5: Formateo y Handover (Traspaso)**

El paso final es crucial. El Curator transforma la narrativa refinada en el formato estricto del protocolo de Handover. No es texto libre; es un objeto de datos estructurado diseñado para ser la "semilla" perfecta para el siguiente sistema de IA encargado de escribir el libro.

## ---

**5\. Protocolo de Handover: La Semilla Narrativa Estructurada**

Para asegurar que la complejidad y los matices de la idea generada no se pierdan cuando se traspase al sistema de escritura masiva, definimos un esquema JSON riguroso. Este esquema actúa como el "ADN" de la novela. Un resumen en prosa es insuficiente porque los LLMs tienden a "olvidar" detalles sutiles o reinterpretar el tono si no se especifica explícitamente.14

### **5.1. Esquema JSON de la Semilla (seed.json)**

El siguiente esquema define los campos obligatorios y su propósito. Cada campo está diseñado para guiar aspectos específicos de la generación de texto posterior (diálogos, descripciones, ritmo).

JSON

{  
  "meta": {  
    "version": "1.0",  
    "generator": "Stochastic\_Ideation\_Engine\_v1",  
    "timestamp": "ISO8601\_TIMESTAMP",  
    "seed\_entropy\_id": "INTEGER\_ID"  
  },  
  "core\_concept": {  
    "title\_working": "Título provisional evocador",  
    "logline": "Resumen de una oración con Protagonista \+ Objetivo \+ Obstáculo \+ Estacas.",  
    "genres":,  
    "themes":  
  },  
  "world\_building": {  
    "setting\_description": "Descripción sensorial densa del entorno (visión, sonido, olor).",  
    "rules\_physics\_magic": "Reglas inmutables del mundo (e.g., tecnología, magia, leyes sociales).",  
    "societal\_structure": "Descripción de la jerarquía social y mecanismos de control."  
  },  
  "narrative\_mechanics": {  
    "conflict\_vector": "Definición precisa del conflicto central (e.g., Man vs. Self).",  
    "oblique\_constraint\_application": "Explicación de cómo se aplicó la estrategia oblicua a la trama.",  
    "pacing\_guide": "Instrucciones sobre el ritmo (e.g., 'Slow burn' o 'Frenético')."  
  },  
  "characters":,  
  "plot\_outline": {  
    "inciting\_incident": "Evento detonante específico.",  
    "plot\_points":  
  },  
  "style\_guidelines": {  
    "tone": "Adjetivos tonales (e.g., claustrofóbico, esperanzador).",  
    "show\_dont\_tell\_examples": "Ejemplos concretos de cómo describir emociones sin nombrarlas."  
  }  
}

### **5.2. Ejemplo de Instancia de Semilla (Caso de Estudio)**

A continuación, se presenta un ejemplo real de cómo se vería una semilla generada por el sistema, ilustrando la profundidad de la información.

**Caso: "Echoes of the Chlorophyll Void"**

JSON

{  
  "meta": {  
    "version": "1.0",  
    "seed\_entropy\_id": 84921  
  },  
  "core\_concept": {  
    "title\_working": "Echoes of the Chlorophyll Void",  
    "logline": "En una estación espacial abandonada invadida por una jungla mutante, una archivista sorda debe navegar mediante vibraciones para escapar de una IA que usa el sonido para reescribir la memoria humana.",  
    "genres":,  
    "themes":  
  },  
  "world\_building": {  
    "setting\_description": "La Estación 'Verde Zenith'. Pasillos metálicos estrangulados por enredaderas bioluminiscentes. La luz es verde y pulsante. El aire huele a ozono y tierra mojada.",  
    "rules\_physics\_magic": "El sonido de alta frecuencia activa las esporas de la planta, que liberan neurotoxinas alucinógenas.",  
    "societal\_structure": "Colonia fallida, ahora tribal y silenciosa. Jerarquía basada en la capacidad de sigilo."  
  },  
  "narrative\_mechanics": {  
    "conflict\_vector": "Man vs. Technology (The AI) & Man vs. Nature (The Spores)",  
    "oblique\_constraint\_application": "Estrategia: 'Usa gente no cualificada'. La protagonista no es una guerrera ni científica, es una archivista, lo que la obliga a usar el conocimiento histórico como arma en lugar de la fuerza.",  
    "pacing\_guide": "Tensión sostenida y silenciosa, interrumpida por estallidos de ruido caótico."  
  },  
  "characters":,  
  "style\_guidelines": {  
    "tone": "Opresivo, Húmedo, Silencioso.",  
    "show\_dont\_tell\_examples": "No digas que hay ruido peligroso; describe las enredaderas vibrando y liberando polvo dorado."  
  }  
}

## ---

**6\. Guía de Implementación Técnica y Despliegue**

La implementación efectiva de este sistema requiere la orquestación de componentes locales y servicios de IA. A continuación se detallan los pasos y el código necesario para desplegar el "Motor de Ideación".

### **6.1. Requisitos del Sistema**

* **Entorno:** Sistema operativo basado en Unix (Linux/macOS) o WSL en Windows.  
* **Lenguaje:** Python 3.10 o superior.  
* **Herramientas de IA:** Cuenta de Anthropic (para Claude Code) y uv o pip para gestión de paquetes Python.  
* **Librerías:** fastmcp, typer, python-dotenv.

### **6.2. Implementación del Servidor MCP (server.py)**

El servidor MCP es el puente entre la lógica local y el cerebro de la IA. Utilizamos fastmcp para una implementación rápida y decoradores para definir las herramientas.

Python

\# Archivo: scripts/server.py  
from fastmcp import FastMCP  
import random  
import json  
import os  
from typing import Dict, List

\# Inicialización del servidor MCP  
mcp \= FastMCP("IdeationEngine")

\# Rutas relativas a los datos  
BASE\_DIR \= os.path.dirname(os.path.abspath(\_\_file\_\_))  
DATA\_DIR \= os.path.join(BASE\_DIR, '../data')

def load\_json\_data(filename: str) \-\>  Dict:  
    """Función auxiliar para cargar datos JSON de forma segura."""  
    filepath \= os.path.join(DATA\_DIR, filename)  
    try:  
        with open(filepath, 'r', encoding='utf-8') as f:  
            return json.load(f)  
    except FileNotFoundError:  
        return {"error": f"File {filename} not found"}

@mcp.tool()  
def get\_aesthetic\_fusion() \-\> str:  
    """  
    Selecciona dos estéticas aleatorias del banco de datos y las fusiona.  
    Útil para generar ambientes visuales únicos.  
    """  
    data \= load\_json\_data('aesthetics.json')  
    if "error" in data: return "Error loading aesthetics"  
      
    \# Selección de 2 estéticas distintas  
    aesthetics \= data.get('aesthetics',)  
    selected \= random.sample(aesthetics, 2)  
    return f"{selected} x {selected\[1\]}"

@mcp.tool()  
def get\_dystopian\_scenario() \-\> Dict\[str, str\]:  
    """  
    Genera un escenario distópico combinando un mecanismo de control  
    y un fallo social.  
    """  
    data \= load\_json\_data('tropes\_dystopia.json')  
    mechanisms \= data.get('control\_mechanisms',)  
    flaws \= data.get('societal\_flaws',)  
      
    return {  
        "mechanism": random.choice(mechanisms),  
        "social\_flaw": random.choice(flaws)  
    }

@mcp.tool()  
def get\_oblique\_strategy() \-\> str:  
    """  
    Recupera una Estrategia Oblicua aleatoria para aplicar como restricción lateral.  
    """  
    data \= load\_json\_data('oblique\_strategies.json')  
    strategies \= data if isinstance(data, list) else  
    return random.choice(strategies)

@mcp.tool()  
def get\_conflict\_vector() \-\> str:  
    """Selecciona un tipo de conflicto narrativo."""  
    data \= load\_json\_data('conflicts.json')  
    conflicts \= data.get('types',)  
    return random.choice(conflicts)

@mcp.tool()  
def generate\_chaos\_seed(complexity: int \= 2) \-\> str:  
    """  
    HERRAMIENTA MAESTRA: Genera el Paquete de Ruido completo.  
    El Agente Brainstormer DEBE llamar a esta función para iniciar la ideación.  
    """  
    aesthetic \= get\_aesthetic\_fusion()  
    scenario \= get\_dystopian\_scenario()  
    strategy \= get\_oblique\_strategy()  
    conflict \= get\_conflict\_vector()  
    seed\_id \= random.randint(10000, 99999)  
      
    packet \= {  
        "seed\_id": seed\_id,  
        "directive": "SYNTHESIZE\_NARRATIVE",  
        "constraints": {  
            "visual\_style": aesthetic,  
            "world\_rules": scenario,  
            "narrative\_conflict": conflict,  
            "lateral\_strategy": strategy  
        }  
    }  
    return json.dumps(packet, indent=2)

if \_\_name\_\_ \== "\_\_main\_\_":  
    mcp.run()

### **6.3. Script de Orquestación (Bash)**

Para ejecutar el flujo de trabajo completo, utilizamos un script de Bash run\_ideation.sh que interactúa con Claude Code CLI. Este script encadena las entradas y salidas, pasando el contexto de un agente al siguiente mediante tuberías (pipes) y archivos temporales.

Bash

\#\!/bin/bash  
\# Archivo: run\_ideation.sh

\# Configuración de colores para salida  
GREEN='\\033 Iniciando Motor de Ideación...${NC}"

\# Paso 0: Asegurar que el servidor MCP está registrado (paso único o verificación)  
\# claude mcp add ideation\_server \-- python scripts/server.py

\# Paso 1: Captura de Input de Usuario (opcional)  
read \-p "Introduce una intención o tema base (dejar vacío para aleatorio): " USER\_INTENT  
if; then  
    USER\_INTENT="Generar una historia completamente nueva y sorprendente."  
fi

\# Paso 2: Fase Brainstormer  
echo \-e "${GREEN} Generando Ruido y Sintetizando Ideas...${NC}"  
\# El prompt instruye a Claude a usar la herramienta MCP 'generate\_chaos\_seed'  
claude \-p "Actúa como el Agente Brainstormer. Tu contexto base es: '$USER\_INTENT'. USA la herramienta 'generate\_chaos\_seed' para obtener los parámetros. Genera 3 sinopsis narrativas detalladas que integren todos los elementos del ruido. NO escribas el JSON final todavía." \> temp\_ideas.md

echo \-e "${GREEN} Ideas Generadas. Iniciando Curaduría...${NC}"  
cat temp\_ideas.md

\# Paso 3: Fase Curator  
echo \-e "${GREEN}\[Agente Curator\] Evaluando y Seleccionando...${NC}"  
\# Pasamos las ideas generadas como contexto al Curator  
cat temp\_ideas.md | claude \-p "Actúa como el Agente Curator. Evalúa las ideas anteriores. Selecciona la mejor basándote en originalidad y conflicto. Refínala y genera el archivo JSON de Semilla Final siguiendo el esquema estricto de Handover." \> final\_seed.json

echo \-e "${GREEN} Proceso completado. Semilla guardada en 'final\_seed.json'.${NC}"

## ---

**7\. Conclusiones y Escalabilidad Futura**

El diseño presentado en este reporte establece una base sólida para la generación narrativa asistida por IA que evita las trampas de la predictibilidad estadística. Al inyectar entropía estructurada mediante herramientas externas (Python/MCP) y forzar la síntesis lateral mediante agentes con roles adversariales, el "Motor de Ideación" asegura que el punto de partida de cualquier proyecto de escritura sea intrínsecamente novedoso.

La escalabilidad del sistema es inherente a su diseño modular. Los bancos de datos JSON pueden ampliarse infinitamente con nuevos géneros, culturas y conceptos científicos sin necesidad de reentrenar modelos ni modificar el código de los agentes. Futuras iteraciones podrían incluir un módulo de retroalimentación humana en el paso de Curaduría (human-in-the-loop) o la integración de modelos de generación de imágenes para visualizar las estéticas fusionadas como parte del paquete de semilla.

Este sistema transforma el rol del escritor: de generador de texto desde cero a director de una orquesta de caos controlado, donde la tecnología sirve para expandir, y no reemplazar, la imaginación humana.

## ---

**Anexos: Tablas de Datos de Referencia**

### **Tabla 1: Matriz de Tropos Distópicos y Consecuencias**

19

*Referencia para data/tropes\_dystopia.json*

| Mecanismo de Control | Consecuencia Social (Fallo) | Elemento Visual Asociado |
| :---- | :---- | :---- |
| **Neural Override Implants** | Pérdida del subtexto lingüístico; literalidad forzada. | Puertos de datos en la base del cráneo; ojos vidriosos. |
| **Child Allocation Lottery** | Mercado negro de identidad genética; "Hijos Fantasma". | Guarderías industriales masivas; códigos de barras biológicos. |
| **Emotion Suppression Drugs** | "Felicidad Obligatoria"; incapacidad de procesar el duelo. | Dispensadores de pastillas en cada esquina; sonrisas rictus. |
| **Resource Hoarding (Water)** | Cultos religiosos al agua; deshidratación como castigo. | Piel agrietada; arquitectura hidropónica fortificada. |
| **Memory Editing Bureau** | Historia inestable; paranoia colectiva. | Proyectores holográficos que reescriben fachadas de edificios. |

### **Tabla 2: Matriz de Fusión Estética (Ejemplos de Combinatoria)**

18

*Referencia para la lógica de combinación en injector.py*

| Estética Base (Mundo) | Estética Modificadora (Tono) | Resultado Conceptual (Inspiración) |
| :---- | :---- | :---- |
| **Solarpunk** | **Analog Horror** | Una utopía verde perfecta donde los registros antiguos (VHS) revelan crímenes fundacionales sangrientos. |
| **Cyberpunk** | **Cottagecore** | Hackers que viven en comunas agrícolas desconectadas ("Off-grid"), usando tecnología biológica y musgo. |
| **Gothic** | **Space Opera** | Naves espaciales con arquitectura de catedrales; vampirismo tecnológico en el vacío del espacio. |
| **Noir** | **Biopunk** | Detectives genéticos investigando crímenes en una ciudad hecha de carne cultivada; lluvia de fluidos. |
| **Western** | **Vaporwave** | Un desierto de neón en un servidor abandonado; cowboys digitales buscando fragmentos de datos nostálgicos. |

### **Tabla 3: Estrategias Oblicuas y Aplicación Narrativa**

24

*Guía de interpretación para el Agente Brainstormer*

| Estrategia Oblicua | Interpretación Narrativa Sugerida |
| :---- | :---- |
| *"Honor thy error as a hidden intention"* | Convertir un fallo del protagonista (o del sistema) en la clave de la salvación/resolución. |
| *"Use an unacceptable color"* | Introducir una amenaza o elemento mágico asociado a un espectro visual prohibido o imposible. |
| *"Look closely at the most embarrassing details"* | Centrar el conflicto en una debilidad patética o humillante del héroe, no en su fuerza. |
| *"Abandon normal instruments"* | El protagonista debe resolver el problema sin usar su habilidad principal o tecnología estándar. |
| *"Disconnect from desire"* | El personaje logra su objetivo solo cuando deja de quererlo activamente (paradoja zen aplicada a la trama). |

#### **Obras citadas**

1. What is LLM Temperature? \- IBM, fecha de acceso: enero 4, 2026, [https://www.ibm.com/think/topics/llm-temperature](https://www.ibm.com/think/topics/llm-temperature)  
2. Controlling randomness in LLMs: Temperature and Seed \- Dylan Castillo, fecha de acceso: enero 4, 2026, [https://dylancastillo.co/posts/seed-temperature-llms.html](https://dylancastillo.co/posts/seed-temperature-llms.html)  
3. Controlling Creativity: How to Get Reproducible Outcomes from LLMs | by Prabhavith Reddy | Medium, fecha de acceso: enero 4, 2026, [https://medium.com/@prabhavithreddy/controlling-creativity-how-to-get-reproducible-outcomes-from-llms-016ec0991891](https://medium.com/@prabhavithreddy/controlling-creativity-how-to-get-reproducible-outcomes-from-llms-016ec0991891)  
4. Using the Oblique Strategies Technique for More Creativity in your Academic Work, fecha de acceso: enero 4, 2026, [https://lumivero.com/resources/using-the-oblique-strategies-technique-for-more-creativity-in-your-academic-work/](https://lumivero.com/resources/using-the-oblique-strategies-technique-for-more-creativity-in-your-academic-work/)  
5. Oblique Strategies. Brian Eno and Peter Schmidt first… | by Alexander Russell \- Medium, fecha de acceso: enero 4, 2026, [https://medium.com/@alexanderussell/oblique-strategies-cf0a1f86c90a](https://medium.com/@alexanderussell/oblique-strategies-cf0a1f86c90a)  
6. Claude Code on the web, fecha de acceso: enero 4, 2026, [https://code.claude.com/docs/en/claude-code-on-the-web](https://code.claude.com/docs/en/claude-code-on-the-web)  
7. The Claude Developer Guide — MCP in the API | by Aserdargun | Nov, 2025, fecha de acceso: enero 4, 2026, [https://medium.com/@aserdargun/the-claude-developer-guide-mcp-in-the-api-d2f1461313fe](https://medium.com/@aserdargun/the-claude-developer-guide-mcp-in-the-api-d2f1461313fe)  
8. Leveraging the strengths of LLMs for creativity & thinking | by Tony Jin | UX Collective, fecha de acceso: enero 4, 2026, [https://uxdesign.cc/leverage-the-strengths-of-llms-for-creativity-thinking-58137a8da8b9](https://uxdesign.cc/leverage-the-strengths-of-llms-for-creativity-thinking-58137a8da8b9)  
9. How to make a random story generator in Python | by Markus Urban \- Medium, fecha de acceso: enero 4, 2026, [https://markusurban.medium.com/how-to-make-a-random-story-generator-in-python-3373f285d149](https://markusurban.medium.com/how-to-make-a-random-story-generator-in-python-3373f285d149)  
10. How to build a Random Story Generator using Python? \- GeeksforGeeks, fecha de acceso: enero 4, 2026, [https://www.geeksforgeeks.org/python/how-to-build-a-random-story-generator-using-python/](https://www.geeksforgeeks.org/python/how-to-build-a-random-story-generator-using-python/)  
11. How we built our multi-agent research system \- Anthropic, fecha de acceso: enero 4, 2026, [https://www.anthropic.com/engineering/multi-agent-research-system](https://www.anthropic.com/engineering/multi-agent-research-system)  
12. AI Agents with Microsoft Agent Framework and Elsa Workflows, fecha de acceso: enero 4, 2026, [https://sipkeschoorstra.medium.com/ai-agents-with-microsoft-agent-framework-and-elsa-workflows-4870e33a7134](https://sipkeschoorstra.medium.com/ai-agents-with-microsoft-agent-framework-and-elsa-workflows-4870e33a7134)  
13. How to Use JSON Format to Write Shockingly Accurate Prompts? \- Apidog, fecha de acceso: enero 4, 2026, [https://apidog.com/blog/json-format-prompts/](https://apidog.com/blog/json-format-prompts/)  
14. The official Python SDK for Model Context Protocol servers and clients \- GitHub, fecha de acceso: enero 4, 2026, [https://github.com/modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk)  
15. Claude Code: Best practices for agentic coding \- Anthropic, fecha de acceso: enero 4, 2026, [https://www.anthropic.com/engineering/claude-code-best-practices](https://www.anthropic.com/engineering/claude-code-best-practices)  
16. Cyberpunk derivatives \- Wikipedia, fecha de acceso: enero 4, 2026, [https://en.wikipedia.org/wiki/Cyberpunk\_derivatives](https://en.wikipedia.org/wiki/Cyberpunk_derivatives)  
17. List of Aesthetics, fecha de acceso: enero 4, 2026, [https://aesthetics.fandom.com/wiki/List\_of\_Aesthetics](https://aesthetics.fandom.com/wiki/List_of_Aesthetics)  
18. 100 dystopian writing prompts \- EveryWriter \- Every Writer's Resource, fecha de acceso: enero 4, 2026, [https://www.everywritersresource.com/100-dystopian-writing-prompts/](https://www.everywritersresource.com/100-dystopian-writing-prompts/)  
19. YA Dystopian Tropes (genre breakdown) \- Write the Magic, fecha de acceso: enero 4, 2026, [https://writethemagic.com/ya-dystopian-tropes-genre-breakdown/](https://writethemagic.com/ya-dystopian-tropes-genre-breakdown/)  
20. The 7 Types of Conflict in Literature: Examples and Writing Tips \- Spines, fecha de acceso: enero 4, 2026, [https://spines.com/the-7-types-of-conflict-in-literature/](https://spines.com/the-7-types-of-conflict-in-literature/)  
21. Decoding the Six Conflicts in Literature (With Examples) \- ServiceScape, fecha de acceso: enero 4, 2026, [https://www.servicescape.com/blog/decoding-the-six-conflicts-in-literature-with-examples](https://www.servicescape.com/blog/decoding-the-six-conflicts-in-literature-with-examples)  
22. A cool guide to the 9 Conflicts in Literature : r/coolguides \- Reddit, fecha de acceso: enero 4, 2026, [https://www.reddit.com/r/coolguides/comments/17eavy2/a\_cool\_guide\_to\_the\_9\_conflicts\_in\_literature/](https://www.reddit.com/r/coolguides/comments/17eavy2/a_cool_guide_to_the_9_conflicts_in_literature/)  
23. Oblique Strategies: ideas for creative lateral thinking \- GitHub, fecha de acceso: enero 4, 2026, [https://github.com/joelparkerhenderson/oblique-strategies](https://github.com/joelparkerhenderson/oblique-strategies)  
24. List of All Oblique Strategies \- Matt Rickard, fecha de acceso: enero 4, 2026, [https://mattrickard.com/list-of-all-oblique-strategies](https://mattrickard.com/list-of-all-oblique-strategies)  
25. Creating Your First MCP Server: A Hello World Guide | by Gianpiero Andrenacci | AI Bistrot | Dec, 2025, fecha de acceso: enero 4, 2026, [https://medium.com/data-bistrot/creating-your-first-mcp-server-a-hello-world-guide-96ac93db363e](https://medium.com/data-bistrot/creating-your-first-mcp-server-a-hello-world-guide-96ac93db363e)  
26. Show, Don't Tell: Tips and Examples of The Golden Rule \- Reedsy, fecha de acceso: enero 4, 2026, [https://reedsy.com/blog/show-dont-tell/](https://reedsy.com/blog/show-dont-tell/)  
27. “Show, Don't Tell” in Creative Writing | Writers.com, fecha de acceso: enero 4, 2026, [https://writers.com/show-dont-tell-writing](https://writers.com/show-dont-tell-writing)  
28. Prompt engineering techniques and best practices: Learn by doing with Anthropic's Claude 3 on Amazon Bedrock | Artificial Intelligence, fecha de acceso: enero 4, 2026, [https://aws.amazon.com/blogs/machine-learning/prompt-engineering-techniques-and-best-practices-learn-by-doing-with-anthropics-claude-3-on-amazon-bedrock/](https://aws.amazon.com/blogs/machine-learning/prompt-engineering-techniques-and-best-practices-learn-by-doing-with-anthropics-claude-3-on-amazon-bedrock/)  
29. Use Claude to make bash and/or Python scripts. They are a life saver. : r/ClaudeAI \- Reddit, fecha de acceso: enero 4, 2026, [https://www.reddit.com/r/ClaudeAI/comments/1i3l7rb/use\_claude\_to\_make\_bash\_andor\_python\_scripts\_they/](https://www.reddit.com/r/ClaudeAI/comments/1i3l7rb/use_claude_to_make_bash_andor_python_scripts_they/)  
30. How to properly utilize Claude for creative writing? : r/ClaudeAI \- Reddit, fecha de acceso: enero 4, 2026, [https://www.reddit.com/r/ClaudeAI/comments/1pjoax9/how\_to\_properly\_utilize\_claude\_for\_creative/](https://www.reddit.com/r/ClaudeAI/comments/1pjoax9/how_to_properly_utilize_claude_for_creative/)
# **Narratología Algorítmica: Un Marco Técnico Integral para la Generación de Ficción Larga con Modelos de Lenguaje Grande**

## **1\. Introducción: La Convergencia de la Ingeniería de Sistemas y la Teoría Narrativa**

La irrupción de los Modelos de Lenguaje Grande (LLMs) ha transformado radicalmente el panorama de la producción textual. Sin embargo, la transición de la generación de textos breves a la construcción de narrativas de larga extensión, como una novela de 80,000 a 120,000 palabras, presenta desafíos técnicos y estructurales de una magnitud superior. El problema fundamental no reside en la capacidad del modelo para generar prosa gramaticalmente correcta o estilísticamente coherente en el corto plazo, sino en fenómenos computacionales y cognitivos conocidos como **deriva contextual**, **alucinación estructural** y **amnesia narrativa**. A medida que la longitud de la secuencia de tokens se expande, la capacidad de atención del modelo se diluye, provocando que detalles críticos establecidos en los primeros capítulos se pierdan o contradigan en los actos posteriores.  
Este informe técnico propone una solución robusta a este problema mediante el diseño de un flujo de trabajo de **Autoría Recursiva Asistida por IA**. En lugar de tratar la escritura de una novela como un proceso lineal de generación de texto, este marco la conceptualiza como un problema de ingeniería de sistemas, donde la novela es un sistema complejo de estados interconectados (personajes, tramas, inventarios, reglas del mundo) que deben ser gestionados, actualizados y validados continuamente.  
El enfoque se basa en la integración de metodologías probadas de la teoría narrativa, específicamente la estructura de ritmos de Blake Snyder ("Save the Cat") y las Unidades de Motivación-Reacción (MRU) de Dwight Swain , con técnicas avanzadas de ingeniería de prompts como la Cadena de Densidad ("Chain of Density") y la gestión de estado mediante esquemas JSON. El objetivo es externalizar la memoria de la historia desde la ventana de contexto limitada del LLM hacia una estructura de archivos persistente, permitiendo que el modelo actúe no solo como un redactor, sino como un gestor de base de datos narrativa.  
Un componente central de esta propuesta es el sistema de **'Lectura Progresiva'**, un mecanismo de retroalimentación diseñado para simular la experiencia crítica de un lector humano. Este sistema no se limita a resumir lo escrito, sino que evalúa la resonancia emocional y la coherencia lógica, inyectando estos "vectores de crítica" en el contexto de generación de los capítulos subsiguientes para mantener la tensión narrativa y la integridad del arco de los personajes.

## **2\. Arquitectura del Sistema y Estructura de Datos Híbrida**

Para gestionar la complejidad de una novela, es imperativo abandonar la noción de un único documento de texto en crecimiento. En su lugar, adoptamos una arquitectura de archivos híbrida JSON/Markdown que separa el contenido legible por humanos (la prosa) de los datos estructurados legibles por la máquina (el estado de la simulación narrativa).

### **2.1 Justificación Técnica de la Separación JSON/Markdown**

Los LLMs modernos demuestran un rendimiento superior en tareas de razonamiento lógico y mantenimiento de consistencia cuando los datos se presentan en formatos estructurados como JSON. Mientras que el Markdown es ideal para la fluidez de la narrativa y la lectura humana, el JSON permite definir esquemas estrictos que obligan al modelo a categorizar la información.

* **Markdown (.md):** Se utiliza para los borradores de escenas, notas de investigación y resúmenes narrativos. Su sintaxis ligera facilita la inyección de texto en los prompts sin consumir tokens excesivos en formato.  
* **JSON (.json):** Se utiliza para la "Biblia de la Serie" y el seguimiento de estados. Permite actualizaciones programáticas y validación de campos (e.g., asegurar que un personaje no pueda usar un objeto que no está en su inventario inventory\_list).

### **2.2 Estructura del Directorio del Proyecto**

El flujo de trabajo requiere una inicialización rigurosa del entorno de trabajo. A continuación, se detalla la estructura de directorios propuesta, diseñada para maximizar la recuperabilidad de la información y minimizar la contaminación del contexto.

| Directorio / Archivo | Formato | Función Técnica | Fuente Teórica |
| :---- | :---- | :---- | :---- |
| **/00\_Bible** | Directorio | **Fuente de la Verdad (Source of Truth).** Contiene los datos inmutables y mutables que rigen la lógica del mundo. |  |
| plot\_structure.json | JSON | El esqueleto estructural. Contiene los 15 beats de *Save the Cat* y la lista de escenas planificadas. |  |
| characters.json | JSON | Perfiles dinámicos. Rastrea el arco emocional, inventario y relaciones (Eneagrama). |  |
| world\_rules.md | MD | Reglas de magia/tecnología y modelo de Iceberg Cultural. |  |
| **/01\_Drafts** | Directorio | **Manuscrito en Proceso.** Archivos individuales por escena para evitar la sobrecarga de contexto. |  |
| Ch01\_Scene01.md | MD | Texto narrativo crudo generado por el LLM. |  |
| **/02\_Context** | Directorio | **Memoria a Largo Plazo.** Archivos procesados para inyección en prompts. |  |
| story\_so\_far.md | MD | Resumen recursivo generado mediante *Chain of Density*. |  |
| memory\_log.json | JSON | Registro cronológico de eventos clave y cambios de estado. |  |
| **/03\_Feedback** | Directorio | **Sistema de Lectura Progresiva.** Salidas de la autocrítica simulada. |  |
| critique\_log.md | MD | Análisis cualitativo de cada capítulo (ritmo, tono). |  |

### **2.3 Esquemas de Datos JSON**

#### **2.3.1 Esquema de Personajes (characters.json)**

Este archivo no es estático; se actualiza tras cada capítulo. Se basa en el sistema de personalidad del Eneagrama para definir motivaciones profundas, no solo rasgos superficiales.  
`{`  
  `"character_id": "PROT_01",`  
  `"name": "Elias Thorne",`  
  `"archetype": {`  
    `"enneagram_type": "5w4",`  
    `"descriptor": "El Iconoclasta",`  
    `"core_fear": "Ser inútil o incapaz",`  
    `"core_desire": "Ser competente y capaz"`  
  `},`  
  `"narrative_arc": {`  
    `"start_state": "Aislamiento intelectual",`  
    `"end_state": "Conexión emocional",`  
    `"current_status": "Desafiado por el evento incitante",`  
    `"false_belief": "El conocimiento es la única seguridad"`  
  `},`  
  `"relationships":,`  
  `"inventory":`  
`}`

#### **2.3.2 Esquema de Estructura de Trama (plot\_structure.json)**

Define la hoja de ruta. Se genera inicialmente pero permite flexibilidad.  
`{`  
  `"global_settings": {`  
    `"genre": "Cyberpunk Noir",`  
    `"pov": "Tercera Persona Limitada",`  
    `"target_word_count": 80000`  
  `},`  
  `"beats": [`  
    `{`  
      `"beat_name": "Opening Image",`  
      `"percentage": "0-1%",`  
      `"description": "Establecer el statu quo defectuoso.",`  
      `"scenes": ["1.1"]`  
    `},`  
    `{`  
      `"beat_name": "Catalyst",`  
      `"percentage": "10%",`  
      `"description": "Evento disruptivo que rompe el equilibrio.",`  
      `"scenes": ["1.5"]`  
    `}`  
  `]`  
`}`

## **3\. Fase 1: Ingeniería Estructural y Planificación (El Arquitecto)**

Antes de escribir una sola línea de prosa, el sistema requiere la construcción de un andamiaje robusto. Utilizaremos una combinación del **Método Snowflake** para la expansión fractal de la idea y la estructura **Save the Cat (STC)** para asegurar el ritmo narrativo.

### **3.1 Paso 1: Definición de la Premisa y Expansión Fractal**

El primer paso es transformar una idea vaga en una estructura operativa. El LLM actúa como un consultor estructural.  
**Prompt de Entrada (Inicialización):**

# **ROL: Arquitecto Narrativo Experto**

# **TAREA: Inicializar la estructura de una novela basada en una premisa de usuario.**

# **METODOLOGÍA:**

1. Utiliza el "Método Snowflake" para expandir la premisa en un resumen de 4 párrafos.  
2. Mapea estos párrafos a los 4 actos estructurales (Acto 1, Acto 2A, Acto 2B, Acto 3).  
3. Define los siguientes metadatos críticos en formato JSON:  
   * Logline (25 palabras).  
   * Tema Central (Argumento Moral).  
   * "Mentira" que cree el protagonista.  
   * "Verdad" que debe aprender.

# **PREMISA DEL USUARIO:**

\[Insertar idea aquí, e.g., "Un detective en una colonia marciana descubre que el aire es un placebo."\]

# **SALIDA ESPERADA:**

Un bloque de texto Markdown con el resumen y un bloque de código JSON con los metadatos.

### **3.2 Paso 2: Generación de la Hoja de Ritmos (Beat Sheet)**

Una vez definida la sinopsis expandida, se procede a la granularización mediante los 15 beats de Blake Snyder. Esto es crucial para evitar el "valle de la muerte" del segundo acto, común en la escritura con IA.  
**Prompt de Entrada (Generación de Beats):**

# **CONTEXTO:**

Se te proporciona el resumen expandido y los metadatos del proyecto.

# **TAREA:**

Generar un archivo plot\_structure.json completo distribuyendo la historia en los 15 beats de Save the Cat.

# **REQUISITOS TÉCNICOS:**

* Calcula el recuento de palabras estimado para cada beat basándote en un total de 80,000 palabras.  
* Para cada beat, define:  
  1. "Conflict\_Target": El objetivo del conflicto en esta sección.  
  2. "Emotional\_Shift": El cambio emocional esperado en el protagonista (positivo a negativo o viceversa).  
  3. "Scene\_List": Una lista preliminar de escenas necesarias para cumplir el beat.

# **BEATS REQUERIDOS:**

1....[source](https://expertbeacon.com/saving-the-cat-and-crafting-powerful-themes-with-chatgpt/) Dark Night of the Soul (75-80%) 13\. Break Into Three (80%) 14\. Finale (80-99%) 15\. Final Image (99-100%)

# **SALIDA:**

Únicamente el objeto JSON válido.  
**Análisis de la Estrategia:** Al solicitar el Emotional\_Shift en el JSON, preparamos el terreno para la generación de prosa. Los LLMs tienden a escribir escenas planas si no se les instruye explícitamente sobre la polaridad emocional (e.g., una escena debe comenzar con esperanza y terminar en desesperación).

## **4\. Fase 2: Modelado del Mundo y Entidades (El Demiurgo)**

La consistencia es el mayor desafío en textos largos. Para mitigar esto, definimos el mundo y los personajes como entidades con reglas fijas.

### **4.1 Definición del Mundo: El Iceberg Cultural**

Para el archivo world\_rules.md, utilizamos el modelo del Iceberg Cultural para obligar al LLM a considerar aspectos profundos del mundo que informan el subtexto, no solo la descripción visual.  
**Prompt de Entrada (Worldbuilding):**

# **TAREA:**

Generar la Biblia del Mundo (world\_rules.md) utilizando el modelo del Iceberg Cultural.

# **INSTRUCCIONES DE PROCESAMIENTO:**

Divide la definición del mundo en tres niveles de profundidad:

1. **Nivel Superficial (Visible):** Arquitectura, moda, comida, rituales públicos.  
2. **Nivel Intermedio (Normas no escritas):** Conceptos de cortesía, espacio personal, jerarquía social, tabúes conversacionales.  
3. **Nivel Profundo (Valores Core):** Concepto del tiempo, relación con la naturaleza/tecnología, definición de "éxito" y "vergüenza".

# **FORMATO DE SALIDA:**

Markdown estructurado con viñetas. Incluye una sección final de "Reglas Físicas/Mágicas Inmutables" si aplica.

### **4.2 Perfilado de Personajes: Eneagrama y Voz**

Los personajes generados por IA a menudo suenan intercambiables. Para evitar esto, utilizamos el Eneagrama para definir su psicología y asignamos pautas lingüísticas estrictas.  
**Prompt de Entrada (Personajes):**

# **TAREA:**

Crear el archivo characters.json para el elenco principal.

# **PARÁMETROS DE GENERACIÓN:**

Para cada personaje, define:

* **Eneagrama:** Tipo y Ala (e.g., 8w7 "El Retador").  
* **Herida Fantasma (Ghost Wound):** Trauma pasado que dicta su comportamiento actual.  
* **Voz y Diálogo:**  
  * *Léxico:* (e.g., académico, callejero, técnico).  
  * *Sintaxis:* (e.g., oraciones cortas y directas vs. oraciones complejas y subordinadas).  
  * *Muletillas:* Palabras o gestos recurrentes.

# **SALIDA:**

JSON array con objetos de personaje detallados.

## **5\. Fase 3: Flujo de Trabajo de Redacción (El Tejedor)**

Esta fase constituye el núcleo operativo. No se debe pedir al LLM que "escriba el Capítulo 1". La solicitud debe ser granular, basada en escenas y gobernada por principios estilísticos estrictos.

### **5.1 Principio Rector: Unidades de Motivación-Reacción (MRU)**

Para garantizar que la prosa tenga un flujo lógico y causal, imponemos la estructura de MRU descrita por Dwight Swain.

* **Motivación (M):** Un estímulo externo objetivo (lo que el personaje ve, oye, toca).  
* **Reacción (R):** La respuesta interna y externa del personaje, en orden estricto:  
  1. Sensación visceral (involuntaria).  
  2. Reflejo emocional.  
  3. Acción racional/Pensamiento.  
  4. Habla.

Los LLMs a menudo invierten este orden (haciendo que el personaje hable antes de reaccionar visceralmente) o mezclan la motivación y la reacción en un "puré" narrativo. El prompt debe prohibir esto explícitamente.

### **5.2 Prompt Maestro de Redacción de Escenas**

Este es el prompt que se utiliza repetidamente para generar el texto del manuscrito.

# **SISTEMA: Experto en Escritura de Ficción Literaria**

Eres un novelista experto especializado en "Deep POV" (Punto de Vista Profundo) y "Show, Don't Tell".

# **CONTEXTO DE ENTRADA (Inyectar dinámicamente):**

* **Personajes Presentes:** \[Extraer de characters.json\]  
* **Configuración de Escena:** \[Ubicación y hora\]  
* **Beat de la Trama:**  
* **Estado Anterior:**  
* **Objetivo de la Escena:** \[Conflicto específico\]

# **INSTRUCCIONES DE ESTILO (CRÍTICO):**

1. **Adherencia a MRU:** Escribe en ciclos estrictos de Motivación (estímulo externo) seguida de Reacción (procesamiento interno \+ acción). Nunca mezcles el orden.  
2. **Deep POV:** Elimina verbos de filtro (vio, sintió, escuchó, pensó).  
   * *Mal:* "Juan vio que la puerta estaba abierta y sintió miedo."  
   * *Bien:* "La puerta estaba abierta. Un escalofrío recorrió la espalda de Juan."  
3. **Especificidad Sensorial:** Usa descripciones concretas. Involucra al menos 3 sentidos.  
4. **Variación de Ritmo:** Usa oraciones cortas para la acción y largas para la introspección.

# **TAREA:**

Escribir la escena (aprox. 800-1000 palabras). Detente si la escena alcanza una resolución natural o un cliffhanger.

### **5.3 Gestión de la Salida Markdown**

El usuario debe guardar la salida en 01\_Drafts/ChXX\_SceneXX.md. Es fundamental no concatenar todo en un solo archivo durante la fase de borrador para facilitar la edición modular.

## **6\. Fase 4: Sistema de 'Lectura Progresiva' (Autocrítica y Memoria)**

Esta sección aborda el requisito específico de un sistema que simule la experiencia de un lector humano. La mayoría de los flujos de trabajo fallan porque solo acumulan texto; este sistema acumula *comprensión*.

### **6.1 Concepto de Resumen Recursivo: Chain of Density (CoD)**

Para mantener el contexto ("Context Window Management") , no podemos simplemente resumir el capítulo anterior, ya que se perderían detalles sutiles. Utilizamos la técnica **Chain of Density** para crear resúmenes hiperdensos que retienen "entidades" narrativas críticas.

#### **6.1.1 Prompt de Compresión de Memoria (CoD)**

# **TAREA:**

Generar un Resumen Recursivo del texto proporcionado utilizando el método 'Chain of Density'.

# **TEXTO DE ENTRADA:**

# **PROCESO ITERATIVO (5 PASOS):**

1. Genera un resumen inicial verboso (aprox. 80 palabras).  
2. Identifica 1-3 "Entidades Perdidas" (detalles clave, objetos, cambios emocionales sutiles) que faltan en el resumen anterior.  
3. Reescribe el resumen para incluir estas entidades sin aumentar la longitud, utilizando fusión y compresión lingüística.  
4. Repite el paso 2 y 3 cinco veces.

# **DEFINICIÓN DE ENTIDAD PERDIDA:**

* Relevante para la trama principal.  
* Específica (nombre propio, objeto concreto).  
* Novedosa (no estaba en el resumen anterior).

# **SALIDA:**

Un objeto JSON con el array de iteraciones y el resumen final denso.  
El "resumen final denso" se añade al archivo story\_so\_far.md. Este archivo es lo que el LLM "lee" antes de escribir el siguiente capítulo, asegurando que recuerde no solo los hechos, sino la densidad narrativa.

### **6.2 El Lector Simulado: Autocrítica y Análisis de Sentimiento**

Este componente actúa como un editor humano que lee el borrador y ofrece correcciones antes de que se considere "finalizado".  
**Prompt de Lectura Progresiva (Crítica):**

# **ROL: Editor Crítico y Lector "Beta"**

# **TAREA: Realizar una 'Lectura Progresiva' del borrador actual.**

# **ENTRADA:**

\[Perfil del Personaje de characters.json\]

# **INSTRUCCIONES DE ANÁLISIS:**

1. **Verificación de Voz:** ¿El diálogo del personaje coincide con sus directrices de voz en el JSON? (Cita ejemplos de desviación).  
2. **Análisis de Ritmo:** ¿Hay secciones donde la descripción detiene innecesariamente la acción?  
3. **Detección de "Telling":** Identifica párrafos donde se resumen emociones en lugar de mostrarlas.  
4. **Coherencia Lógica:** ¿Hay contradicciones con eventos anteriores o reglas del mundo?

# **SALIDA (Markdown):**

## **Informe de Lectura**

* **Puntuación de Tensión (1-10):** \[Valor\]  
* **Inconsistencias Detectadas:** \[Lista\]  
* **Sugerencias de Reescritura:**

### **6.3 Actualización de Estado (El Bucle de Retroalimentación)**

Después de la crítica y la aceptación del borrador, se debe actualizar el estado del sistema. Esto no es automático en los LLMs; requiere un prompt explícito.  
**Prompt de Actualización de JSON:**

# **TAREA: Actualizar los archivos de estado basados en el nuevo capítulo.**

# **ENTRADA:**

\[Estado Actual de characters.json\]

# **INSTRUCCIONES:**

Analiza los eventos del capítulo y genera un "JSON Patch" con los cambios necesarios:

1. ¿Ha cambiado la relación entre personajes? (Actualizar relationships).  
2. ¿Se ha adquirido o perdido algún objeto? (Actualizar inventory).  
3. ¿El protagonista ha dado un paso hacia su "Verdad" o se ha aferrado a su "Mentira"? (Actualizar narrative\_arc).

# **SALIDA:**

JSON con los campos a modificar.

## **7\. Tablas de Referencia y Resumen del Flujo de Trabajo**

### **7.1 Resumen del Flujo de Trabajo Diario**

| Fase | Acción Humana | Acción del LLM | Archivo de Entrada | Archivo de Salida |
| :---- | :---- | :---- | :---- | :---- |
| **1\. Carga** | Seleccionar escena y revisar estado. | Cargar contexto. | story\_so\_far.md, characters.json | Memoria Activa |
| **2\. Planificación** | Solicitar opciones de esquema para la escena. | Generar 3 opciones de conflicto. | plot\_structure.json | Opciones de Escena |
| **3\. Borrador** | Seleccionar opción e iniciar prompt de redacción. | Generar prosa (MRU \+ Deep POV). | Prompt Maestro de Redacción | ChXX\_SceneXX\_Draft.md |
| **4\. Crítica** | Ejecutar prompt de "Lectura Progresiva". | Analizar y criticar el borrador. | ChXX\_SceneXX\_Draft.md | critique\_log.md |
| **5\. Refinamiento** | Solicitar reescritura de secciones débiles. | Reescribir párrafos específicos. | Feedback del usuario | ChXX\_SceneXX\_Final.md |
| **6\. Consolidación** | Ejecutar Chain of Density y Update State. | Generar resumen y JSON patch. | ChXX\_SceneXX\_Final.md | story\_so\_far.md, characters.json (actualizado) |

### **7.2 Comparativa de Estrategias de Contexto**

| Estrategia | Descripción | Ventajas | Desventajas |
| :---- | :---- | :---- | :---- |
| **Ventana Deslizante** | Solo se alimenta el texto de los últimos X capítulos. | Fácil de implementar. | Pérdida total de eventos antiguos (Amnesia). |
| **Resumen Simple** | Un resumen único que crece indefinidamente. | Mantiene la trama general. | Pérdida de detalle y "aplanamiento" narrativo. |
| **Resumen Recursivo (Propuesto)** | Uso de Chain of Density para mantener resúmenes densos \+ RAG para detalles. | Alta coherencia y retención de subtexto. | Requiere mayor gestión de prompts y tokens. |

## **8\. Gestión de Alucinaciones y Recuperación de Información (RAG)**

A pesar de la estructura rigurosa, los LLMs pueden alucinar detalles fácticos (e.g., cambiar el color de ojos de un personaje en el capítulo 20). Para mitigar esto en una obra de gran extensión, se recomienda una implementación ligera de **RAG (Retrieval-Augmented Generation)**.

### **8.1 Implementación de "Búsqueda de Palabras Clave"**

Si no se dispone de una base de datos vectorial compleja, se puede simular RAG mediante un sistema de etiquetas en el Markdown.

* En cada archivo de escena, añadir metadatos al inicio: Tags:,, \[Objeto: Carta Antigua\]  
* Antes de escribir una escena que involucre la "Carta Antigua", el usuario (o un script) busca todos los archivos anteriores con ese tag e inyecta los fragmentos relevantes en el contexto del LLM.

**Prompt de Inyección de Contexto RAG:**

# **INFORMACIÓN RECUPERADA (CONTEXTO ADICIONAL):**

Los siguientes fragmentos provienen de capítulos anteriores y DEBEN ser respetados como hechos inmutables:

* Del Cap 3: "La carta estaba sellada con cera azul y olía a lavanda."  
* Del Cap 12: "Sofía juró nunca volver a leer la carta."

Usa esta información para asegurar la continuidad en la nueva escena.

## **9\. Conclusión**

La escritura de una novela con un LLM no es un acto de magia, sino un ejercicio de arquitectura de información. El flujo de trabajo presentado transforma el proceso vago de "pedirle a la IA que escriba" en un sistema determinista y controlado.  
Al separar el **estado** (JSON) de la **narrativa** (Markdown) y al interponer un sistema de **Lectura Progresiva** (Autocrítica y Chain of Density) entre cada ciclo de escritura, logramos simular la memoria y la intencionalidad de un autor humano. Este enfoque permite explotar la creatividad inagotable del LLM mientras se encorseta su volatilidad dentro de una estructura narrativa clásica y rigurosa. El resultado es un manuscrito que mantiene su coherencia, ritmo y profundidad emocional desde la "Imagen de Apertura" hasta la "Imagen Final".

### **Anexo: Lista de Verificación para el Usuario (Antes de cada Sesión)**

1. ¿Está actualizado characters.json con los cambios del último capítulo?  
2. ¿Se ha generado el resumen denso en story\_so\_far.md?  
3. ¿Cuál es el beat de *Save the Cat* que corresponde a la sesión de hoy?  
4. ¿Tengo definidos los estímulos sensoriales (MRU) para la escena que voy a solicitar?

Este rigor técnico es lo que distingue a un operador de IA profesional de un usuario casual, permitiendo la creación de obras de ficción largas que son indistinguibles, en estructura y coherencia, de las escritas enteramente por humanos.

#### **Obras citadas**

1\. Towards Robust Synthetic Data Generation for Simplification of Text in French \- MDPI, https://www.mdpi.com/2504-4990/7/3/68 2\. Effective context engineering for AI agents \- Anthropic, https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents 3\. Context Window Management: Strategies for Long-Context AI Agents and Chatbots, https://www.getmaxim.ai/articles/context-window-management-strategies-for-long-context-ai-agents-and-chatbots/ 4\. Book Review | Quirk, https://fencer.wordpress.com/category/book-review/ 5\. Save the Cat Beat Sheet: The Ultimate Guide (+ Template) \- Reedsy, https://reedsy.com/blog/guide/story-structure/save-the-cat-beat-sheet/ 6\. Scene & Sequel in exposition or world building \- Writing Stack Exchange, https://writing.stackexchange.com/questions/41906/scene-sequel-in-exposition-or-world-building 7\. Writing Motivation-reaction Units (MRUs According to Swain) \- September C. Fawkes, https://www.septembercfawkes.com/2022/01/writing-motivation-reaction-units-mrus.html 8\. From Sparse to Dense: GPT-4 Summarization with Chain of Density Prompting \- PMC \- NIH, https://pmc.ncbi.nlm.nih.gov/articles/PMC11419567/ 9\. Better Summarization with Chain of Density Prompting \- PromptHub, https://www.prompthub.us/blog/better-summarization-with-chain-of-density-prompting 10\. Creating your first schema \- JSON Schema, https://json-schema.org/learn/getting-started-step-by-step 11\. ChatGPT and JSON Responses: Prompting & Modifying Code-Friendly Objects \- Medium, https://medium.com/@bobmain49/chatgpt-and-json-responses-prompting-modifying-code-friendly-objects-ad368822ec86 12\. I Used the Same Prompt on ChatGPT but one was JSON Formatted and Got Crazy Different Results \- Reddit, https://www.reddit.com/r/PromptEngineering/comments/1pgo0ve/i\_used\_the\_same\_prompt\_on\_chatgpt\_but\_one\_was/ 13\. Definition of the \[snowflake\] method for writing a story : r/writers \- Reddit, https://www.reddit.com/r/writers/comments/16vef98/definition\_of\_the\_snowflake\_method\_for\_writing\_a/ 14\. See How Easily You Can Write A Novel Using The Snowflake Method \- Reddit, https://www.reddit.com/r/writing/comments/2w7o3p/see\_how\_easily\_you\_can\_write\_a\_novel\_using\_the/ 15\. Save the Cat Beat Sheet 101: 15 Beats for Perfect Story Structure | Kindlepreneur, https://kindlepreneur.com/save-the-cat-beat-sheet/ 16\. How to Outline Your Novel with the Save the Cat\! Beat Sheet \- Savannah Gilbo, https://www.savannahgilbo.com/blog/plotting-save-the-cat 17\. How to Create a Fictional Culture (With a Checklist) \- Campfire, https://www.campfirewriting.com/learn/how-to-create-fictional-cultures 18\. Enneagram Character Profiles: Build Complex Psyches \[Template\] \- Plottr, https://plottr.com/enneagram-character-template/ 19\. Motivation-Reaction Units: how the masters do it \- Writes With Tools, https://writeswithtools.com/2024/02/28/motivation-reaction-units-how-the-masters-do-it/ 20\. 8 Paragraph Mistakes You Don't Know You're Making, https://www.helpingwritersbecomeauthors.com/paragraph-mistakes/ 21\. AI Prompting (3/10): Context Windows Explained—Techniques Everyone Should Know, https://www.reddit.com/r/PromptEngineering/comments/1iftklk/ai\_prompting\_310\_context\_windows/ 22\. Chain of Density (CoD) \- Learn Prompting, https://learnprompting.org/docs/advanced/self\_criticism/chain-of-density 23\. llm functions \- Need short summary of 60 Page document using LLMFunctions, https://mathematica.stackexchange.com/questions/288538/need-short-summary-of-60-page-document-using-llmfunctions 24\. Metadata-Driven Retrieval-Augmented Generation for Financial Question Answering \- arXiv, https://arxiv.org/html/2510.24402v1
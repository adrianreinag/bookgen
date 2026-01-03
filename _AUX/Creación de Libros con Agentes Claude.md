# **Arquitectura de Sistemas Literarios Autónomos: Implementación de Orquestación Multi-Agente mediante Claude Code**

## **Resumen Ejecutivo**

La evolución de los Grandes Modelos de Lenguaje (LLM) ha transitado desde interfaces de chat efímeras hacia entornos de ejecución agéntica capaces de interactuar directamente con sistemas operativos y archivos. En el contexto de la creación literaria de gran formato (novelas, ensayos técnicos, sagas), los enfoques tradicionales basados en ventanas de contexto único han demostrado ser insuficientes debido a la degradación de la coherencia narrativa y la "alucinación" de hechos previamente establecidos. Este informe detalla una arquitectura técnica exhaustiva para desplegar **Claude Code** —la interfaz de línea de comandos agéntica de Anthropic— como un motor de orquestación robusto para la generación de libros.

A diferencia de los asistentes de codificación estándar, Claude Code se conceptualiza aquí como un sistema operativo creativo. Aprovechando sus capacidades nativas de manipulación del sistema de archivos, ejecución de comandos Bash y gestión de sub-agentes, proponemos un modelo de "Orquestador-Trabajadores" (Orchestrator-Workers). Este sistema mantiene el estado narrativo en archivos persistentes (Markdown) que actúan como una "Fuente de la Verdad" (Source of Truth \- SOT) inmutable, permitiendo un crecimiento recursivo desde una semilla conceptual hasta un manuscrito finalizado. El informe aborda la topología de agentes, la definición de flujos de trabajo recursivos, la ingeniería de contexto mediante CLAUDE.md y SKILL.md, y las estrategias para mitigar la entropía narrativa en proyectos de más de 80.000 palabras.

## ---

**1\. El Paradigma de Claude Code en la Ingeniería Narrativa**

Para comprender cómo construir una máquina de escritura autónoma, es imperativo primero disecar la herramienta central: Claude Code. Aunque se comercializa y discute en la literatura técnica como una herramienta de asistencia para la programación 1, su arquitectura subyacente es fundamentalmente la de un orquestador agéntico de propósito general. Esta distinción es crucial. Un programador ve "código", "funciones" y "refactorización"; un ingeniero narrativo debe ver "tramas", "escenas" y "revisión estilística". Claude Code permite esta transposición gracias a su capacidad de vivir en la terminal y manipular el sistema de archivos como una extensión de su memoria cognitiva.3

### **1.1 El Sistema de Archivos como Memoria Neuronal Externa**

En una interacción estándar con un LLM, la "memoria" está limitada estrictamente a la ventana de contexto —el búfer deslizante de tokens que el modelo puede procesar en una sola inferencia—. En proyectos de larga duración, como una novela, confiar en la ventana de contexto es una estrategia fallida; inevitablemente, los detalles del Capítulo 1 se pierden o se comprimen con pérdida cuando se escribe el Capítulo 20\.5

Claude Code cambia este paradigma al integrar el sistema de archivos local como un mecanismo de Recuperación Aumentada (RAG) nativo. La capacidad de la herramienta para ejecutar comandos como ls, grep y read permite que el agente trate un directorio de archivos Markdown no como documentos pasivos, sino como una base de datos activa y consultable.6 Para un sistema de escritura de libros, esto significa que la narrativa no reside en la "mente" efímera de la IA, sino en la estructura del directorio del proyecto. Cuando un agente necesita verificar el color de ojos de un personaje secundario introducido hace trescientas páginas, no confía en su memoria latente; ejecuta una búsqueda precisa en el directorio bible/characters/, recuperando el dato exacto sin contaminar su contexto con información irrelevante.

Esta arquitectura de "memoria externa" es lo que permite escalar de cuentos cortos a sagas de múltiples volúmenes. La persistencia del archivo garantiza que la "Fuente de la Verdad" (SOT) permanezca inmutable e independiente de las alucinaciones del modelo.8

### **1.2 "Plan Mode": La Capa Arquitectónica del Razonamiento**

Una innovación crítica de Claude Code es la introducción del "Plan Mode" (Modo Planificación), activado mediante secuencias de comandos específicas o banderas en la CLI.9 En el desarrollo de software, esto previene la generación de código defectuoso mediante la planificación previa. En la ingeniería narrativa, el **Plan Mode actúa como el Arquitecto de la Trama**.

Cuando el sistema opera en este modo, se bloquean las herramientas de escritura destructiva. El agente se ve obligado a analizar los requisitos, leer la estructura existente y generar un archivo de plan (PLAN.md) antes de escribir una sola línea de prosa.11 Esta separación de preocupaciones —planificación frente a ejecución— replica el proceso cognitivo de los autores profesionales que distinguen claramente entre la esquematización (outlining) y el borrador (drafting). Técnicamente, esto reduce la carga cognitiva durante la fase de generación de texto, ya que el modelo no necesita "inventar" la trama y "escribir" la prosa simultáneamente; la trama ya ha sido resuelta y "congelada" en el archivo de plan, permitiendo que el modelo dedique todos sus recursos computacionales a la calidad estilística.12

### **1.3 Sub-agentes y la Topología de "Writer's Room"**

La complejidad de una novela requiere múltiples tipos de inteligencia: la lógica estructural para la trama, la creatividad sensorial para la descripción y la rigurosidad analítica para la continuidad. Un solo "prompt" o agente monolítico no puede mantener estos modos de pensamiento contradictorios simultáneamente sin degradar su rendimiento.

Claude Code permite la instanciación de **sub-agentes** —instancias especializadas de Claude con sus propios prompts de sistema, herramientas permitidas y ventanas de contexto aisladas—.13 Esto habilita la creación de una topología de "Writer's Room" (Sala de Escritores), donde agentes específicos (El Arquitecto, El Bibliotecario, El Redactor) realizan tareas distintas en paralelo o secuencia. El aislamiento del contexto es vital aquí: el agente encargado de escribir una escena de acción no necesita tener cargado en su contexto el análisis temático profundo de la obra, solo los hechos inmediatos requeridos. Esto optimiza el uso de tokens y mantiene la "voz" de cada agente pura y enfocada.15

## ---

**2\. Arquitectura del Sistema: Modelo Orquestador-Trabajadores**

Para satisfacer el requisito de crear un sistema que "crezca desde una semilla" y gestione la complejidad de un libro completo, proponemos una arquitectura jerárquica basada en el patrón **Orquestador-Trabajadores** (Orchestrator-Workers).15 En este modelo, una instancia central de Claude Code actúa como el director ejecutivo, manteniendo el estado global del proyecto y delegando tareas específicas a agentes especializados que operan sobre la estructura de archivos.

### **2.1 Estructura de Directorios: La Definición de la SOT**

La estructura del sistema de archivos no es meramente organizativa; es el mapa cognitivo del sistema. Definimos un esquema de directorios rígido que separa ontológicamente la "Verdad del Mundo" (La Biblia), el "Flujo Narrativo" (La Estructura) y la "Salida Creativa" (El Manuscrito). Esta separación permite que diferentes agentes tengan permisos de lectura/escritura granulares, protegiendo la integridad del proyecto.18

| Directorio / Archivo | Propósito y Función Técnica | Agente Responsable (Escritura) |
| :---- | :---- | :---- |
| root/ | Punto de entrada. Contiene configuración global. | Orquestador |
| root/CLAUDE.md | Memoria del proyecto, reglas globales, definición de comandos. | Orquestador |
| root/bible/ | **Fuente de la Verdad (SOT)**. Datos inmutables del mundo. | Archivista |
| root/bible/characters/ | Hojas de personaje (Markdown estructurado). | Archivista |
| root/bible/locations/ | Archivos de construcción de mundo (Worldbuilding). | Archivista |
| root/bible/timeline.md | Cronología maestra de eventos fácticos. | Archivista |
| root/structure/ | El esqueleto narrativo mutable. | Arquitecto |
| root/structure/outline.md | Arquitectura de alto nivel (Actos, Capítulos). | Arquitecto |
| root/structure/beats/ | Guiones paso a paso por capítulo (Beat Sheets). | Arquitecto |
| root/manuscript/ | Salida de prosa. | Redactor |
| root/manuscript/drafts/ | Texto generado en bruto. | Redactor |
| root/manuscript/final/ | Texto revisado y pulido. | Editor / Crítico |
| root/.claude/skills/ | Definiciones de habilidades reutilizables (SKILL.md). | Ingeniero (Usuario) |
| root/.claude/agents/ | Configuración de personae de sub-agentes. | Ingeniero (Usuario) |

### **2.2 Roles Agénticos y Definición de Personas**

Para llevar a cabo la orquestación, debemos instanciar agentes específicos. En Claude Code, estos se configuran mediante el comando /agents o definiendo archivos de configuración en .claude/agents/. La investigación sugiere que la especialización profunda mejora el rendimiento en tareas complejas.19

#### **2.2.1 El Orquestador (The Executive)**

* **Implementación:** La instancia principal de Claude Code en la terminal.  
* **Responsabilidad:** No escribe contenido. Su función es entender la intención del usuario ("Quiero avanzar el Capítulo 3"), descomponer esa intención en pasos técnicos, asignar tareas a los sub-agentes y verificar que los archivos resultantes cumplan con los requisitos técnicos (existencia, formato).  
* **Herramientas:** Acceso total al sistema (Bash, File System, Agent Dispatch).

#### **2.2.2 El Arquitecto (The Architect)**

* **Implementación:** Sub-agente especializado.  
* **Prompt del Sistema:** "Eres un experto en estructura narrativa y teoría literaria (ej. Save the Cat, El Viaje del Héroe). Tu objetivo es la causalidad, el ritmo (pacing) y la arquitectura de la trama. No escribes prosa florida; escribes planos estructurales. Tu salida debe ser siempre archivos Markdown jerárquicos."  
* **Flujo:** Lee la seed (semilla) o el outline actual \-\> Identifica huecos estructurales \-\> Genera o actualiza structure/beats/.

#### **2.2.3 El Archivista (The Archivist)**

* **Implementación:** Sub-agente con alta penalización a la creatividad.  
* **Prompt del Sistema:** "Eres el guardián de la continuidad y la Fuente de la Verdad (SOT). Tu trabajo es detectar contradicciones y registrar hechos. Si el Capítulo 1 dice que un personaje cojea, te aseguras de que no corra una maratón en el Capítulo 5 sin explicación. Gestionas la base de datos en bible/."  
* **Flujo:** Escanea nuevos borradores \-\> Extrae nuevos hechos (lugares, nombres) \-\> Actualiza bible/ \-\> Reporta inconsistencias.

#### **2.2.4 El Redactor (The Drafter)**

* **Implementación:** Sub-agente con alta temperatura (creatividad).  
* **Prompt del Sistema:** "Eres un novelista de ficción literaria. Tu enfoque está en el detalle sensorial, el monólogo interno y el diálogo realista. Te basas estrictamente en los 'beats' proporcionados por el Arquitecto. No inventas giros de trama; ejecutas la escena."  
* **Flujo:** Lee structure/beats/ \+ bible/characters/ \-\> Genera manuscript/drafts/.

#### **2.2.5 El Crítico (The Critic)**

* **Implementación:** Sub-agente analítico.  
* **Prompt del Sistema:** "Eres un editor despiadado. Analizas el texto buscando repeticiones, adverbios excesivos, falta de claridad y violaciones del tono. No reescribes; generas informes de 'diff' o listas de cambios sugeridos."

## ---

**3\. Implementación Técnica en Claude Code**

La implementación de este sistema requiere configurar el entorno de Claude Code para soportar flujos de trabajo complejos y persistentes. A continuación, se detalla cómo configurar los archivos de control y las habilidades agénticas.

### **3.1 Ingeniería de Contexto: CLAUDE.md**

El archivo CLAUDE.md situado en la raíz del proyecto es el primer punto de contacto para la ingeniería de contexto.21 Debe establecer las "Leyes de la Física" del proyecto.

**Contenido Recomendado para CLAUDE.md:**

# **Sistema de Generación de Novela Autónoma**

## **Directivas Primarias**

1. **Inmutabilidad de la Biblia:** El directorio bible/ es la autoridad absoluta. Nunca contradigas la información contenida en él al generar estructura o prosa.  
2. **Separación de Preocupaciones:** Nunca generes prosa sin que exista previamente un archivo de beat aprobado en structure/.  
3. **Formato:** Todos los archivos de salida deben ser Markdown válido. Usa encabezados (\#) para separar escenas.

## **Protocolo de Agentes**

* Para tareas de planificación o estructura, invoca al sub-agente architect.  
* Para tareas de escritura de contenido, invoca al sub-agente drafter.  
* Para verificación de hechos o consultas de lore, invoca al sub-agente archivist.

## **Comandos del Proyecto**

* build-chapter \[n\]: Ejecuta la secuencia completa de generación para el capítulo n.  
* update-bible: Escanea los últimos borradores y actualiza la base de datos de conocimiento.

### **3.2 Definición de "Agent Skills" (SKILL.md)**

Las "Habilidades de Agente" (Agent Skills) son módulos reutilizables que permiten estandarizar tareas complejas.22 Crearemos habilidades específicas que el Orquestador puede llamar. Estas se guardan en .claude/skills/.

#### **Habilidad 1: develop-beats (Desarrollo de Escenas)**

* **Ubicación:** .claude/skills/develop-beats/SKILL.md  
* **Metadata YAML:**  
  YAML  
  name: develop-beats  
  description: Convierte un resumen de capítulo de alto nivel en una hoja de beats detallada escena por escena.  
  allowed-tools:

* **Instrucciones Markdown:**  
  1. Leer el resumen del capítulo objetivo desde structure/outline.md.  
  2. Identificar los personajes presentes y leer sus fichas desde bible/characters/.  
  3. Desglosar el capítulo en 3-5 escenas distintas.  
  4. Para cada escena, definir explícitamente: Objetivo del personaje, Conflicto, Desastre/Resultado.  
  5. Guardar el resultado en structure/beats/chapter\_\[XX\].md.

#### **Habilidad 2: draft-from-beats (Escritura de Prosa)**

* **Ubicación:** .claude/skills/draft-from-beats/SKILL.md  
* **Metadata YAML:**  
  YAML  
  name: draft-from-beats  
  description: Genera prosa literaria completa basada en una hoja de beats aprobada.  
  allowed-tools:

* **Instrucciones Markdown:**  
  1. Leer el archivo de beats especificado.  
  2. Leer bible/style\_guide.md para ajustar el tono.  
  3. Invocar al sub-agente drafter para convertir cada beat en prosa.  
  4. Asegurar que el diálogo respete la "voz" definida en las fichas de personaje.  
  5. Escribir el archivo manuscript/drafts/chapter\_\[XX\].md.

#### **Habilidad 3: integrity-scan (Verificación de Consistencia)**

* **Ubicación:** .claude/skills/integrity-scan/SKILL.md  
* **Instrucciones Markdown:**  
  1. Leer el borrador recién generado.  
  2. Extraer todas las entidades nombradas (personas, lugares, objetos).  
  3. Usar grep para buscar estas entidades en bible/.  
  4. Si una entidad existe, verificar que la descripción en el borrador coincida con la SOT.  
  5. Si una entidad es nueva, generar una alerta sugiriendo la creación de una nueva entrada en la Biblia.

## ---

**4\. Definición del Flujo de Creación: De la Semilla al Libro**

El flujo de trabajo propuesto es **recursivo e iterativo**. No intentamos generar el libro en una sola pasada lineal. En su lugar, utilizamos un enfoque de "Crecimiento Fractal", donde cada etapa añade resolución y detalle a la anterior.23

### **Fase 1: La Semilla y la Inicialización (Fase de Génesis)**

El objetivo de esta fase es establecer el ADN del proyecto. Sin una base sólida, la orquestación posterior derivará en incoherencia.

1. **Entrada del Usuario:** El usuario proporciona una "Semilla" (Seed). Esto puede ser un párrafo simple: *"Una novela de ciencia ficción noir sobre un detective que investiga el robo de recuerdos en una colonia de Marte en el año 2350."*  
2. **Acción del Orquestador:**  
   * Ejecuta mkdir para crear la estructura de directorios (bible, structure, manuscript).  
   * Crea el archivo bible/seed.md con la premisa inicial.  
3. **Expansión del Archivista:**  
   * El Orquestador invoca al Archivista: *"Interroga la semilla. Genera una lista de 20 preguntas fundamentales sobre el mundo, los personajes y el tono que necesitamos responder para construir la Biblia."*  
   * El Archivista genera bible/worldbuilding\_questions.md.  
   * El usuario (o el agente en modo auto-reflexivo) responde estas preguntas, poblando bible/premise.md y las primeras fichas en bible/characters/.

### **Fase 2: Arquitectura Estructural (El Esqueleto)**

Una vez que la Biblia tiene suficiente densidad crítica, pasamos a la estructura.

1. **Comando del Usuario:** *"Genera un esquema de 12 capítulos basado en la premisa."*  
2. **Acción del Arquitecto:**  
   * Lee bible/premise.md y bible/characters/.  
   * Aplica una plantilla estructural (ej. Estructura de Tres Actos).  
   * Genera structure/outline.md, donde cada capítulo tiene un resumen de 2-3 oraciones.  
3. **Refinamiento en "Plan Mode":** El usuario entra en Plan Mode (Shift+Tab) para discutir y ajustar el esquema con el Arquitecto. *"El Acto 2 es muy lento. Introduce un giro en el Capítulo 6."* El Arquitecto actualiza el archivo.

### **Fase 3: Planificación de Escenas (Los Músculos)**

Aquí es donde el sistema se diferencia de un chat normal. No escribimos prosa todavía.

1. **Comando del Orquestador:** *"Ejecuta la habilidad develop-beats para el Capítulo 1."*  
2. **Ejecución:** El agente lee el resumen del Capítulo 1, consulta la Biblia para ver quién está en la escena y dónde ocurre, y genera structure/beats/chapter\_01.md.  
3. **Resultado:** Un archivo técnico que describe: *"Escena 1: El Detective entra al bar. El aire huele a ozono. Habla con el informante. Descubre que el robo fue interno. Conflicto: El informante no quiere hablar. Resolución: El Detective lo soborna."*

### **Fase 4: Producción de Prosa (La Piel)**

Solo cuando los beats están aprobados, se genera el texto.

1. **Comando del Orquestador:** *"Ejecuta la habilidad draft-from-beats para el Capítulo 1."*  
2. **Acción del Redactor:**  
   * Carga el archivo de beats y la guía de estilo.  
   * Genera la prosa, enfocándose exclusivamente en la calidad literaria, ya que la trama está resuelta.  
   * Guarda manuscript/drafts/chapter\_01.md.

### **Fase 5: El Bucle de Retroalimentación SOT (El Sistema Inmune)**

Esta es la fase crítica para evitar la "podredumbre del contexto" (Context Rot).

1. **Acción del Archivista:** Inmediatamente después de generar el borrador, el Archivista lo escanea.  
2. **Extracción de Hechos:** Si el Redactor inventó que *"El bar tiene una luz de neón que parpadea en rosa"*, el Archivista extrae este dato.  
3. **Actualización de la Biblia:** Se actualiza bible/locations/bar.md con el detalle *"Iluminación: Neón rosa parpadeante"*.  
4. **Implicación:** Cuando se escriba el Capítulo 10 y el personaje vuelva al bar, el sistema *sabrá* que la luz es rosa, manteniendo la coherencia sin necesidad de releer el Capítulo 1\.8

## ---

**5\. Investigación sobre Flujos y Orquestación en Claude**

La investigación de los patrones de flujo de Claude 19 revela que el éxito en tareas complejas depende de evitar bucles infinitos y gestionar la ventana de contexto mediante "Compresión y Delegación".

### **5.1 Gestión del Contexto y Prevención de Alucinaciones**

El problema principal en la escritura de libros con IA es que el modelo "olvida" lo que escribió al principio. Nuestra arquitectura mitiga esto delegando la memoria al almacenamiento en disco.

* **Estrategia de Contexto Just-in-Time (JIT):** Los agentes nunca cargan el libro completo. El Redactor solo carga el capítulo actual y las fichas de personaje relevantes. Esto mantiene la ventana de contexto limpia y reduce drásticamente el costo de tokens y la latencia.7  
* **Compresión de Estado:** Al finalizar una sesión de trabajo, el Orquestador puede ejecutar un comando /compact (o su equivalente lógico) para resumir la sesión actual en un archivo de registro, limpiando la memoria activa antes de comenzar el siguiente capítulo.

### **5.2 Automatización con Bash y Hooks**

Claude Code permite la ejecución de scripts Bash. Podemos automatizar partes del flujo mediante "Hooks" (Ganchos) o scripts de shell simples.

* **Automatización de Backups:** Podemos instruir a Claude para que ejecute git commit después de cada fase de generación exitosa, creando un historial versionado del manuscrito.  
* **Validación de Formato:** Un script simple en Python puede ser invocado por el Orquestador para verificar que todos los archivos Markdown tengan los encabezados correctos antes de proceder, actuando como un "linter" narrativo.

### **5.3 Uso de MCP (Model Context Protocol)**

Para enriquecer el libro, podemos conectar Claude Code a servidores MCP externos.26

* **MCP de Investigación:** Si la novela requiere precisión histórica o científica, un servidor MCP de búsqueda web puede ser invocado por el Arquitecto durante la fase de outline para validar hechos (ej. "¿Cuánto tarda una señal en llegar de Marte a la Tierra?").  
* **MCP de Sistema de Archivos:** Aunque Claude Code tiene acceso nativo, un servidor MCP dedicado puede proporcionar capacidades de búsqueda semántica más avanzadas sobre la Biblia del proyecto.

## ---

**6\. Desafíos y Estrategias de Mitigación**

A pesar de la robustez de esta arquitectura, existen desafíos inherentes a la generación agéntica.

### **6.1 El Problema de la Homogeneidad Estilística**

Los LLM tienden a converger hacia un estilo de prosa "seguro" y promedio.

* **Mitigación:** Uso intensivo de bible/style\_guide.md con ejemplos *negativos* ("No uses estas palabras") y *positivos* (fragmentos de texto de referencia con el tono deseado). El sub-agente Crítico debe estar configurado para penalizar los clichés.

### **6.2 Bucles de Planificación Infinita**

A veces, los agentes se quedan atascados refinando planes sin ejecutar.

* **Mitigación:** Implementar un límite estricto de iteraciones en las instrucciones del Orquestador. "Si el Arquitecto no produce un esquema final en 3 intentos, escala la decisión al usuario humano".

### **6.3 Deriva Narrativa (Narrative Drift)**

A medida que el libro crece, la trama puede desviarse de la premisa original.

* **Mitigación:** El archivo bible/premise.md debe ser inyectado obligatoriamente en el contexto del Arquitecto en cada sesión de planificación para asegurar que los nuevos capítulos sigan alineados con la visión central.

## ---

**Conclusión**

Llevar a cabo un sistema de escritura de libros con Claude Code no es simplemente una tarea de "pedirle a la IA que escriba". Es un ejercicio de **Ingeniería de Sistemas Agénticos**. Requiere tratar la literatura como un problema de gestión de estado, donde la coherencia es una función de la integridad de la base de datos (La Biblia) y la calidad narrativa es una función de la especialización de los agentes.

La arquitectura propuesta de **Orquestador-Trabajadores**, apoyada por una estructura de archivos SOT rigurosa y el uso estratégico de Sub-agentes y Habilidades, transforma a Claude Code de un asistente de chat en un estudio de producción literaria autónomo. La clave del éxito reside en la disciplina del flujo: **Planificar \-\> Estructurar \-\> Escribir \-\> Actualizar SOT**. Al adherirse a este ciclo recursivo, es posible trascender las limitaciones de la ventana de contexto y generar obras de extensión y complejidad arbitrarias.

### **Pasos Inmediatos para la Implementación**

1. **Instalar Claude Code** y autenticar con la API de Anthropic.  
2. **Inicializar el Repositorio:** Crear las carpetas bible, structure, manuscript.  
3. **Configurar CLAUDE.md:** Definir las reglas inmutables del proyecto.  
4. **Crear los Sub-agentes:** Definir las personas del Arquitecto y el Archivista primero.  
5. **Ejecutar la Semilla:** Generar el primer archivo de premisa y comenzar el ciclo de expansión fractal.

#### **Obras citadas**

1. anthropics/claude-code: Claude Code is an agentic coding ... \- GitHub, fecha de acceso: enero 3, 2026, [https://github.com/anthropics/claude-code](https://github.com/anthropics/claude-code)  
2. fecha de acceso: enero 3, 2026, [https://www.anthropic.com/engineering/claude-code-best-practices\#:\~:text=Claude%20Code%20is%20a%20command,line%20tool%20for%20agentic%20coding.](https://www.anthropic.com/engineering/claude-code-best-practices#:~:text=Claude%20Code%20is%20a%20command,line%20tool%20for%20agentic%20coding.)  
3. What's Claude Code? : r/ClaudeAI \- Reddit, fecha de acceso: enero 3, 2026, [https://www.reddit.com/r/ClaudeAI/comments/1ixave9/whats\_claude\_code/](https://www.reddit.com/r/ClaudeAI/comments/1ixave9/whats_claude_code/)  
4. Claude Code overview \- Claude Code Docs, fecha de acceso: enero 3, 2026, [https://code.claude.com/docs/en/overview](https://code.claude.com/docs/en/overview)  
5. Context Engineering: The Invisible Discipline Keeping AI Agents from Drowning in Their Own Memory, fecha de acceso: enero 3, 2026, [https://medium.com/@juanc.olamendy/context-engineering-the-invisible-discipline-keeping-ai-agents-from-drowning-in-their-own-memory-c0283ca6a954](https://medium.com/@juanc.olamendy/context-engineering-the-invisible-discipline-keeping-ai-agents-from-drowning-in-their-own-memory-c0283ca6a954)  
6. Building agents with the Claude Agent SDK \- Anthropic, fecha de acceso: enero 3, 2026, [https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)  
7. Effective context engineering for AI agents \- Anthropic, fecha de acceso: enero 3, 2026, [https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)  
8. Messaging as the Single Source of Truth | Confluent, fecha de acceso: enero 3, 2026, [https://www.confluent.io/blog/messaging-single-source-truth/](https://www.confluent.io/blog/messaging-single-source-truth/)  
9. Common workflows \- Claude Code Docs, fecha de acceso: enero 3, 2026, [https://code.claude.com/docs/en/common-workflows](https://code.claude.com/docs/en/common-workflows)  
10. Claude Code Plan Mode: Revolutionizing the Senior Engineer's Workflow \- Medium, fecha de acceso: enero 3, 2026, [https://medium.com/@kuntal-c/claude-code-plan-mode-revolutionizing-the-senior-engineers-workflow-21d054ee3420](https://medium.com/@kuntal-c/claude-code-plan-mode-revolutionizing-the-senior-engineers-workflow-21d054ee3420)  
11. What Actually Is Claude Code's Plan Mode? | Armin Ronacher's Thoughts and Writings, fecha de acceso: enero 3, 2026, [https://lucumr.pocoo.org/2025/12/17/what-is-plan-mode/](https://lucumr.pocoo.org/2025/12/17/what-is-plan-mode/)  
12. Plan Mode Is Now Mandatory. Auto-Compact Should Be Enabled., fecha de acceso: enero 3, 2026, [https://paddo.dev/blog/plan-mode-mandatory-auto-compact-yes/](https://paddo.dev/blog/plan-mode-mandatory-auto-compact-yes/)  
13. \*\*UPDATED 2026\*\* Claude Code Tutorial \#1 \- Intro & Setup ..., fecha de acceso: enero 3, 2026, [https://www.youtube.com/watch?v=NBQePr-XjrU](https://www.youtube.com/watch?v=NBQePr-XjrU)  
14. Subagents \- Claude Code Docs, fecha de acceso: enero 3, 2026, [https://code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents)  
15. Building Effective AI Agents \- Anthropic, fecha de acceso: enero 3, 2026, [https://www.anthropic.com/research/building-effective-agents](https://www.anthropic.com/research/building-effective-agents)  
16. Claude Custom Sub Agents are amazing feature and I built 20 of them to open source., fecha de acceso: enero 3, 2026, [https://www.reddit.com/r/ClaudeAI/comments/1mb95kp/claude\_custom\_sub\_agents\_are\_amazing\_feature\_and/](https://www.reddit.com/r/ClaudeAI/comments/1mb95kp/claude_custom_sub_agents_are_amazing_feature_and/)  
17. Building Effective AI Agents: A Guide from Anthropic | by Bharatkumar kori \- Medium, fecha de acceso: enero 3, 2026, [https://medium.com/accredian/building-effective-ai-agents-a-guide-from-anthropic-e66b533ff091](https://medium.com/accredian/building-effective-ai-agents-a-guide-from-anthropic-e66b533ff091)  
18. Writing a Novel in Markdown with Obsidian (70+ Books Later) | pdworkman.com, fecha de acceso: enero 3, 2026, [https://pdworkman.com/writing-a-novel-in-markdown/](https://pdworkman.com/writing-a-novel-in-markdown/)  
19. How we built our multi-agent research system \- Anthropic, fecha de acceso: enero 3, 2026, [https://www.anthropic.com/engineering/multi-agent-research-system](https://www.anthropic.com/engineering/multi-agent-research-system)  
20. AI-Driven Storytelling with Multi-Agent LLMs \- Part III \- The Computist Journal, fecha de acceso: enero 3, 2026, [https://blog.apiad.net/p/ai-driven-storytelling-with-multi-3ed](https://blog.apiad.net/p/ai-driven-storytelling-with-multi-3ed)  
21. Claude Code: Best practices for agentic coding \- Anthropic, fecha de acceso: enero 3, 2026, [https://www.anthropic.com/engineering/claude-code-best-practices](https://www.anthropic.com/engineering/claude-code-best-practices)  
22. Agent Skills \- Claude Code Docs, fecha de acceso: enero 3, 2026, [https://code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills)  
23. Beyond Outlining: Heterogeneous Recursive Planning for Adaptive Long-form Writing with Language Models \- arXiv, fecha de acceso: enero 3, 2026, [https://arxiv.org/pdf/2503.08275](https://arxiv.org/pdf/2503.08275)  
24. claude-cookbooks/patterns/agents/orchestrator\_workers.ipynb at main \- GitHub, fecha de acceso: enero 3, 2026, [https://github.com/anthropics/anthropic-cookbook/blob/main/patterns/agents/orchestrator\_workers.ipynb](https://github.com/anthropics/anthropic-cookbook/blob/main/patterns/agents/orchestrator_workers.ipynb)  
25. Claude Code: Behind-the-scenes of the master agent loop \- PromptLayer Blog, fecha de acceso: enero 3, 2026, [https://blog.promptlayer.com/claude-code-behind-the-scenes-of-the-master-agent-loop/](https://blog.promptlayer.com/claude-code-behind-the-scenes-of-the-master-agent-loop/)  
26. Introducing advanced tool use on the Claude Developer Platform \- Anthropic, fecha de acceso: enero 3, 2026, [https://www.anthropic.com/engineering/advanced-tool-use](https://www.anthropic.com/engineering/advanced-tool-use)  
27. Writing effective tools for AI agents—using AI agents \- Anthropic, fecha de acceso: enero 3, 2026, [https://www.anthropic.com/engineering/writing-tools-for-agents](https://www.anthropic.com/engineering/writing-tools-for-agents)
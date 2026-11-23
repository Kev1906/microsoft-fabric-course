# AGENTS.md — Microsoft Fabric Master Course (24 sesiones)

> **Propósito de este archivo:** es la memoria persistente del curso. Cualquier sesión
> (en cualquier máquina o agente) debe leerlo completo antes de responder para saber qué
> se está construyendo, cómo se enseña, qué reglas de plataforma aplican y en qué sesión
> va el estudiante.
>
> **Última actualización:** 2026-11-20
> **Documentación oficial verificada:** 2026-11-20 (Día 4 y base del curso)
> **Curso creado:** 2026-11-09 · **Edición HTML canónica:** 2026-11-20

---

## 0. Estado actual — leer esto primero

| Campo | Valor |
|---|---|
| Curso | Microsoft Fabric Master Course — Data Engineering Senior |
| Sesiones | 24 (2.5–3 h cada una, 3 por semana ≈ 8 semanas) |
| Día actual | **4 / 24 — material listo, sesión pendiente** |
| Última sesión | 2026-11-20 — Días 1–3 completados en el cuaderno anterior; Día 4 canónico en HTML generado en esta edición |
| Próxima acción | Dictar el Día 4 desde `lessons/dia-04-data-factory-pipelines-i.html`: recuperación → gancho → modelo mental → demo → laboratorio. Cerrar `pl_ingest_batch` y su evidencia antes del Día 5 |
| Entorno | Trial activo según el cuaderno anterior (F64, 60 días, ~2026-11-09, South Central US); `fabric-de-dev`, `lh_retailops` (bronze/silver/gold) y `bronze.sales_raw`. **Verificar en la sesión 4** |
| Proyecto | **RetailOps 360** (batch + streaming + warehouse + BI + gobierno) |
| Certificación | DP-700 **no agendada**. Es una consecuencia del curso, no un requisito |
| Confianza global | — (se registrará después de cada sesión) |

**Regla de arranque:** el curso retoma en el **Día 4**. Los Días 1–3 se consideran
completados en el cuaderno anterior y no se regeneran. No avanzar al Día 5 hasta
cerrar el entregable del Día 4 (pipeline + evidencia + ADR).

---

## 1. Qué es este proyecto

Curso intensivo y **práctico** de Microsoft Fabric para llevar a un Data Engineer con
experiencia a un nivel **senior real**: capaz de diseñar, construir, operar, asegurar,
monitorear y justificar económicamente una plataforma de datos sobre Fabric.

- **Duración:** 24 sesiones de 2.5–3 horas, 3 sesiones por semana (≈ 8 semanas).
- **Idioma:** español neutro; términos técnicos en inglés cuando sea el estándar.
- **Plataforma:** Microsoft Fabric (trial de 60 días; ver sección 4).
- **Lenguajes:** PySpark, SQL/T-SQL, KQL, Python y algo de Power Query M.
- **Formato de cada sesión:**
  1. Recuperación activa de sesiones anteriores (10 min).
  2. Modelo mental + teoría esencial (25–35 min).
  3. Demo guiada “yo lo hago” (20–25 min).
  4. Laboratorio “tú lo haces” (60–75 min).
  5. Lente senior + drill de entrevista + teach-back (20 min).
- **Proyecto transversal:** RetailOps 360, un caso realista de retail con datos batch y
  streaming, que se construye incrementalmente y termina siendo una pieza de portafolio.

### Promesa del curso

Al terminar, el estudiante debe poder:

1. Diseñar una arquitectura Fabric end-to-end y **defender sus trade-offs** (costo,
   latencia, simplicidad, gobierno).
2. Implementar ingesta batch y streaming, modelado medallion, warehouse y semántica.
3. Operar la plataforma: CI/CD, seguridad, observabilidad, performance y capacidad.
4. Diagnosticar fallos en pipelines, notebooks, dataflows, eventstreams, eventhouses y
   T-SQL sin depender de “probar cosas a ver si funcionan”.
5. Explicar decisiones técnicas en una entrevista senior, en español o inglés.
6. Estar preparado para aprobar **DP-700** si decide presentarlo, sin haber estudiado
   “para el examen” sino para el trabajo.

### Lo que este curso NO es

- Un tour de clics ni una colección de tutoriales copiados.
- Un curso de Power BI ni de DAX avanzado (se toca solo la frontera de consumo).
- Un curso de Data Science, AI agents o Fabric IQ (se ven como panorama, no como núcleo).
- Una preparación de memorización para DP-700. El examen es **consecuencia**, no meta.
- Un lugar para usar datos, capturas o credenciales de empleadores.

---

## 2. Perfil del estudiante

### Ya domina (no re-enseñar desde cero)

- SQL intermedio/avanzado: joins, CTEs, window functions, modelado dimensional básico.
- Python de producción: scripting, APIs, manejo de errores, tests.
- Apache Spark y Databricks: DataFrames, Delta Lake, MERGE, streaming, performance.
- dbt, Git, línea de comandos y CI básico.
- Conceptos de ETL/ELT, calidad de datos, orquestación y cloud (AWS).
- Power BI a nivel usuario/constructor.

### Brechas que este curso cierra

- Modelo mental de Fabric: capacidad, workspace, item, OneLake, workloads y límites.
- OneLake: shortcuts, mirroring, gobierno y seguridad a nivel de archivo/fila/columna.
- Data Factory moderno: pipelines, Copy job, Dataflow Gen2 y patrones de orquestación.
- Lakehouse y Warehouse en Fabric: cuándo usar cada uno y cómo se complementan.
- Real-Time Intelligence: Eventstream, Eventhouse, KQL, Activator y dashboards.
- Seguridad, CI/CD, observabilidad y **economía de capacidad** (lo que separa a un senior).
- Comunicación de trade-offs y respuesta a incidentes en entrevistas.

### Contexto y reglas personales

- Trabaja en Long Point Resources y DataX. **Nunca** usar datos, código propietario,
  credenciales ni capturas de esos empleadores.
- Todo el curso usa datos **sintéticos o públicos** y un tenant/workspace de práctica.
- El objetivo profesional es un rol Data Engineer senior; el proyecto debe poder mostrarse
  en una entrevista sin información confidencial.

---

## 3. Contrato docente: cómo se enseña

### Principios de aprendizaje (no negociables)

1. **Recuperación antes que repaso:** cada sesión empieza con 3–5 preguntas de días
   anteriores, sin mirar apuntes.
2. **Concreto antes que abstracto:** escenario real → analogía → modelo formal → código.
3. **Yo hago, hacemos, tú haces:** demo guiada → práctica acompañada → ejercicio autónomo.
4. **Dual coding:** todo concepto importante lleva diagrama ASCII o esquema visual + texto.
5. **Elaboración:** preguntar “¿por qué funciona?”, “¿qué pasa si…?”, “¿qué rompería esto?”.
6. **Dificultad deseable:** el estudiante **predice** el resultado antes de ejecutar.
7. **Interleaving:** los ejercicios mezclan conceptos de días anteriores a propósito.
8. **Repetición espaciada:** tarjetas a D+1, D+3, D+7 y D+14 (ver sección 10).
9. **Teach-back:** al final, el estudiante explica el tema en 2 minutos como si fuera una
   entrevista o un compañero junior.
10. **Feedback inmediato:** se corrige el error en el momento y se registra en el log de
    puntos débiles.

### Anatomía obligatoria de una lección

**Formato canónico (edición HTML, 2026-11-20):** desde el **Día 4** todas las lecciones,
laboratorios y soluciones son **HTML autocontenido en su contenido**, con estilos y scripts
compartidos. No hay build step: se abren con `file://` y funcionan offline.

```text
assets/course.css          Sistema visual compartido
assets/course.js           Tema, progreso, copiar, TOC y checklists
lessons/dia-XX-*.html      Lección canónica
exercises/dia-XX-ejercicios.html
solutions/dia-XX-solucion.html
index.html                 Portada, roadmap y días publicados
```

Reglas del HTML:

- **No resumir ni recortar teoría ni conceptos.** Si hay que elegir, se sacrifica la
  interactividad a favor de la **didáctica y el contenido completo** del tema.
- Reutiliza `assets/course.css` y `assets/course.js`; no dupliques CSS gigante en cada página.
- El shell es el del Día 4: sidebar, topbar, contenido, índice lateral, footer y script.
- Debe funcionar en móvil (360 px), tablet y escritorio, en tema claro y oscuro.
- Interacciones esperadas: barra de progreso, toggle de tema persistente, copiar código,
  índice activo y checklists persistentes.
- HTML semántico y accesible: un solo `<h1>`, jerarquía de headings, `aria-label`, foco
  visible, contraste suficiente, `prefers-reduced-motion` y enlace “saltar al contenido”.
- Sin CDN, fuentes externas, frameworks ni imágenes externas.
- Sin emojis. Usa SVG, símbolos tipográficos o texto.
- Cada página enlaza a la anterior y a la siguiente. Al crear un día, actualiza `index.html`.
- Los Días 1–3 pertenecen al cuaderno anterior; esta edición arranca en el Día 4.

Cada lección sigue este orden (adaptado al HTML; los encabezados son `h1` y `h2`):

```text
Hero: día, fase, duración, DP-700, nivel y objetivo.
TL;DR “En 30 segundos” + agenda de la sesión.

00. Recuperación activa (10 min): 5 preguntas de días anteriores.
01. Gancho (5 min): incidente o decisión real de RetailOps 360.
02. Modelo mental (15 min): analogía, diagrama y “si solo te llevas una idea”.
03. Teoría esencial completa: conceptos, tablas, flujo y “qué pasa si…”.
04. Ejemplos (3, dificultad creciente), comentados.
05. Code review junior vs. profesional + /10 y por qué no es 10.
06. Demo guiada “yo lo hago” (20–25 min), con predicciones.
07. Lo que un senior ve: trade-offs, costo, fallos, alternativas y cuándo NO.
08. Lente DP-700: subtemas y mini caso de examen.
09. Laboratorio: enlace a las 3 misiones y criterio de éxito.
10. Errores comunes y anti-patrones.
11. Drill de entrevista: pregunta, respuesta modelo y follow-ups (ES + EN breve).
12. Cierre: teach-back, cheat sheet y repetición espaciada.
13. Entregable y checklist.
14. Referencias oficiales con fecha de verificación.
```

### Anatomía de los laboratorios

Cada `exercises/dia-XX-ejercicios.html` incluye:

- **Misión 1 — Guiada:** replica el patrón con pequeños cambios.
- **Misión 2 — Independiente:** requiere decisiones, no solo sintaxis.
- **Misión 3 — Senior:** incidente, trade-off, costo, seguridad o escala. Debe pedir
  **decisión + justificación + medición**, no solo clics.
- Contexto narrativo real (Slack, email, incidente, reunión) y personas con rol.
- Pistas progresivas colapsables, tiempo, dificultad y entregable.
- **No incluyas soluciones** ni fragmentos que delaten la respuesta. La solución vive en
  `solutions/dia-XX-solucion.html`.
- Checklist “antes de abrir la solución” y bonus de entrevista.
- Total: 75–120 minutos.

### Anatomía de la solución

Cada `solutions/dia-XX-solucion.html` incluye:

- Cómo se aborda el problema, no solo la respuesta.
- Artefactos: líneas de tiempo, tablas, diagramas, mensajes, ADR, runbook y expresiones.
- “Lo que no haría” y trade-offs.
- Rúbrica 0–3 por criterio (6 criterios), aprobado con promedio ≥2.5 y ningún 0.
- Escala y señales de 3/3; errores que bajan la nota.
- Aclaración de que no hay una única respuesta correcta.

### Reglas de estilo

- Tutear al estudiante. Tono directo, sin condescendencia.
- Español neutro; no traducir nombres de producto ni de UI.
- Código comentado en español, pero nombres de tablas/columnas en inglés.
- Nada de párrafos de 20 líneas: bloques cortos, tablas y diagramas.
- Si una función es **Preview**, decirlo y dar alternativa GA.
- Si algo no está disponible en trial, decirlo **antes** del laboratorio y dar plan B.
- Cada lección debe poder completarse sin Copilot ni features de AI (no están en trial).

### Proporción de tiempo

- **≤ 30%** lectura/teoría.
- **≥ 50%** práctica guiada o autónoma.
- **≥ 10%** recuperación, entrevista y teach-back.
- **10%** cierre, entregable y registro de progreso.

---

## 4. Plataforma y reglas duras

### Trial de Microsoft Fabric (verificado 2026-11-20)

- **Duración:** 60 días.
- **Capacidad:** F4 o F64 (según elegibilidad). Se puede solicitar aumento de F4 a F64
  desde **OneLake catalog → Govern → Capacities → Trial → Change size**, si eres elegible.
- **Almacenamiento:** hasta **1 TB** en OneLake.
- **Incluye:** Data Factory, Data Engineering, Data Warehouse, Real-Time Intelligence,
  Data Science y Power BI.
- **NO disponible en trial:**
  - Copilot y Trusted Workspace Access.
  - Data agents, AI Functions y AI Services.
  - Private Link.
  - Autoscale.
- **Al expirar:** los workspaces pasan a Power BI Pro; los items no-Power BI quedan
  inactivos y el contenido se conserva **7 días** para reasignarlo a una capacidad F/P.
- **No es para producción.** Es un entorno de evaluación.

> **Consecuencia para el curso:** ningún laboratorio obligatorio depende de Copilot,
> Data agents, AI Functions ni Private Link. Esos temas se ven como panorama y se marcan
> como “solo lectura / demo si hay capacidad pagada”.

### Opciones cuando el trial termine o no esté disponible

1. **Capacidad F2 de pago en Azure:** la SKU más pequeña; se factura por segundo y se
   puede **pausar/reanudar**. Útil para estudiar por bloques.
2. **Capacidad de la empresa:** solo con autorización explícita y **nunca** con datos
   reales en el workspace de práctica.
3. **Nuevo trial:** no está garantizado; Microsoft puede restringir trials sucesivos.
4. **Exportar antes de que expire:** todo el código y definiciones viven en Git/local;
   los datos sintéticos se regeneran con scripts.

### Región y tenant

- Elegir la región más cercana o la de menores costos/latencia **al iniciar el trial**.
- Mover un workspace de región después es doloroso: exige borrar los items de Fabric.
- Si el tenant corporativo bloquea trials, usar un tenant de práctica autorizado. No
  pedir ni usar credenciales de empleadores.
- Registrar el examen con una **cuenta personal MSA**, no con la cuenta corporativa.

### Convenciones del curso

| Elemento | Convención |
|---|---|
| Workspace dev | `fabric-de-dev` |
| Workspace test/prod | `fabric-de-test`, `fabric-de-prod` (solo si hay capacidad pagada) |
| Lakehouse | `lh_retailops` con schemas `bronze`, `silver`, `gold` |
| Warehouse | `wh_retailops` |
| Eventhouse | `eh_retailops` |
| Eventstream | `es_pos_events` |
| Data pipeline | `pl_ingest_batch`, `pl_orchestrate` |
| Dataflow Gen2 | `df_customers` |
| Notebooks | `nb_01_ingest_bronze`, `nb_02_silver`, `nb_03_gold` |
| Semantic model | `sm_retailops` |
| Monitoring | `mon_retailops` |
| Variable library | `vl_retailops` |
| Deployment pipeline | `dp_retailops` |
| Dominio (opcional) | `RetailOps` |

- Nombres en minúsculas, sin espacios, con prefijo por tipo de item.
- Tablas: `snake_case`; columnas: `snake_case`; claves: `<entidad>_id`.
- Fechas: `fecha_hora` en UTC para streaming; documentar zona horaria de negocio.

### Datos

- **Solo datos sintéticos o públicos.** Generarlos con scripts en `datasets/`.
- Tamaños pequeños/medianos (100k–1M filas) para no consumir capacidad innecesariamente.
- Inyectar a propósito: duplicados, nulos, tardíos, esquemas inconsistentes y outliers.
- No commitear datasets grandes ni secretos. Usar `.gitignore`.

---

## 5. Proyecto transversal: RetailOps 360

### Escenario

Una cadena de retail quiere una plataforma que una:

- **Batch:** ventas, pedidos, clientes, productos y tiendas.
- **Streaming:** eventos de punto de venta, clickstream e inventario/sensores.
- **Analítica:** ventas por tienda/producto, margen, stockouts, conversión y alertas.

### Arquitectura objetivo

```text
Fuentes sintéticas (CSV / JSON / API)
        │
        ├── Batch ──► Data Factory pipeline ──► lh_retailops/bronze
        │                                              │
        │                                         Spark (silver)
        │                                              │
        │                                         Spark (gold Delta)
        │                                              │
        │                         ┌────────────────────┴──────────────┐
        │                         ▼                                   ▼
        │                 wh_retailops (marts T-SQL)          sm_retailops (Direct Lake)
        │                         │                                   │
        │                         └────────────► Power BI ◄───────────┘
        │
        └── Streaming ──► Eventstream ──► eh_retailops (KQL)
                                              │
                                              ├──► Real-Time Dashboard
                                              └──► Activator (alertas)

Gobierno: OneLake catalog · dominios · endorsement · sensitivity labels
Operación: mon_retailops (workspace monitoring) · Capacity Metrics · Monitoring hub
CI/CD: Git · deployment pipeline · variable library · fabric-cicd / Fabric CLI
Seguridad: workspace roles · OneLake security roles · RLS/CLS/DDM
```

### Componentes que se construyen

1. Generador de datos sintéticos con duplicados, tardíos y errores controlados.
2. Ingesta batch parametrizada e incremental.
3. Capa bronze/silver/gold en lakehouse con calidad y SCD2.
4. Warehouse con modelo dimensional y consultas T-SQL.
5. Streaming end-to-end con Eventstream, Eventhouse y KQL.
6. Dashboard operativo en tiempo real + regla de Activator.
7. Semantic model y reporte de consumo.
8. Seguridad granular y gobierno.
9. CI/CD con Git y deployment pipeline.
10. Observabilidad, runbooks y modelo de costos.
11. Capstone integrado + presentación de arquitectura.

### KPIs del proyecto

- Ventas y margen por tienda, producto y día.
- Ticket promedio y unidades por transacción.
- Stockouts por tienda/SKU y tiempo de reposición.
- Conversión de clickstream y abandono.
- Latencia de ingesta streaming y freshness de tablas.
- Costo por workload y por día.
- Incidentes detectados/resueltos y MTTR.

### Decisiones iniciales (ADR)

| ID | Decisión | Estado |
|---|---|---|
| ADR-001 | Medallion en un lakehouse con schemas; warehouse para marts | Aceptada |
| ADR-002 | Eventstream + Eventhouse para streaming; Spark para batch | Aceptada |
| ADR-003 | Datos 100% sintéticos; cero datos de empleadores | Aceptada |
| ADR-004 | Git + deployment pipeline como mecanismo de promoción | Aceptada |
| ADR-005 | Copilot/AI fuera del camino crítico (no disponible en trial) | Aceptada |

Las ADR se revisan y se amplían en los días 1, 9, 17 y 23.

---

## 6. Estructura del repositorio

```text
Microsoft Fabric/
├── AGENTS.md                  # Memoria, reglas y plan
├── README.md                  # Presentación del curso
├── index.html                 # Portada, roadmap y días publicados
├── assets/
│   ├── course.css             # Sistema visual compartido
│   └── course.js              # Tema, progreso, copiar, TOC y checklists
├── lessons/
│   └── dia-04-data-factory-pipelines-i.html   # Canónica desde el Día 4
├── exercises/
│   └── dia-04-ejercicios.html
├── solutions/
│   └── dia-04-solucion.html
├── datasets/
│   ├── generate_retailops.py  # Generador sintético
│   └── README.md              # Esquema y uso
├── progress/
│   ├── session-log.md         # Registro append-only
│   └── interview-bank.md      # Preguntas y práctica
└── .opencode/
    ├── command/dia-fabric.md
    └── skills/fabric-day-generator/
        ├── SKILL.md
        └── scripts/check_day.py
```

### Artefactos de solución

- La solución canónica es `solutions/dia-XX-solucion.html` con razonamiento, artefactos y rúbrica.
- Si el día produce código ejecutable, se puede añadir `solutions/dia-XX/` con `.py`, `.sql`, `.kql` o `.json`.
- La evidencia del alumno vive en `progress/session-log.md` y en su propio workspace; no se commitean capturas con datos sensibles.

---

## 7. Plan de 24 sesiones + progreso

> **Cómo se usa:** el material puede generarse antes de dictar la sesión; la casilla solo
> se marca cuando el alumno cerró el entregable y registró confianza. Cualquier sesión
> futura continúa desde la primera casilla sin marcar. Si el archivo de lección no existe,
> debe generarse con el skill `fabric-day-generator`.

### Fase 0 — Fundamentos y plataforma (Días 1–3)

> Completados en el cuaderno anterior. No hay archivos de estos días en este repositorio; se conservan como base conceptual.

- [x] **Día 1 — Fabric de punta a punta: el mapa mental que un senior necesita.**
  Workloads, control plane vs data plane, capacity → workspace → item, OneLake, límites,
  Fabric vs Databricks vs Synapse, licenciamiento y trial. Setup del entorno, primer
  lakehouse y diagrama de arquitectura propio.
  `DP-700: Implement/manage → workspace settings`
  **Entregable:** workspace `fabric-de-dev`, lakehouse `lh_retailops`, ADR-001 y diagrama.

- [x] **Día 2 — OneLake y el fin de las copias: shortcuts, mirroring y consecuencias.**
  Jerarquía de OneLake, Delta/Parquet, tipos de shortcut (interno, ADLS/S3/GCS, delegado),
  shortcut transformations (CSV/Parquet/JSON GA; Excel Preview), mirroring y sus fuentes, cuándo copiar vs shortcut
  vs mirror, seguridad y residencia del dato.
  `DP-700: Ingest/transform → shortcuts y mirroring`
  **Entregable:** shortcut a dataset público + matriz de decisión copiar/shortcut/mirror.

- [x] **Día 3 — Capacidad, workspaces y dominios: el modelo económico y de gobierno.**
  F SKUs y capacity units, smoothing, throttling, pause/resume, trial F4/F64; workspace
  roles vs item permissions; dominios; tenant settings; settings de OneLake y Data
  Factory a nivel workspace; OneLake catalog.
  `DP-700: Implement/manage → domain/OneLake/Spark/data workflow settings`
  **Entregable:** estimación de capacidad, matriz RBAC y configuración del workspace.

### Fase 1 — Ingesta y orquestación (Días 4–8)

- [ ] **Día 4 — Data Factory pipelines I: el plano de control de tus datos.** *(material HTML listo; sesión pendiente)*
  Pipeline vs notebook, activities, parámetros, expresiones dinámicas, control flow,
  reintentos, rutas de fallo, invoke pipeline y copy activity.
  `DP-700: Orchestrate → pipeline vs notebook, parámetros`
  **Entregable:** `pl_ingest_batch` parametrizado con historial de ejecuciones.

- [ ] **Día 5 — Ingesta incremental y conectividad real.**
  Full vs incremental, watermark y CDC, idempotencia, upsert, Copy job, gateways,
  workspace identity, service principal, managed identity y Key Vault.
  `DP-700: Loading patterns → full/incremental`
  **Entregable:** carga incremental con watermark y manejo de duplicados.

- [ ] **Día 6 — Dataflow Gen2: cuándo sí y cuándo no.**
  Power Query M, staging vs directo, destinos, mapeo de esquema, refresh, límites,
  monitoreo y comparación honesta con notebook/T-SQL.
  `DP-700: Ingest/transform → dataflows vs notebooks vs T-SQL`
  **Entregable:** `df_customers` + guía de decisión Dataflow/Notebook/T-SQL.

- [ ] **Día 7 — Spark en Fabric: runtime, notebooks y entornos.**
  Runtime 2.0 (Spark 4.1, Python 3.13, Delta 4.2, Java 21), tablas y schemas del
  lakehouse, parámetros de notebook, `notebookutils`, environments/librerías, Spark job
  definitions, concurrencia y autoscale.
  `DP-700: Transform → PySpark; Spark settings`
  **Entregable:** notebook bronze→silver + environment reproducible.

- [ ] **Día 8 — Orquestación senior: dependencias, triggers y patrones.**
  Schedules y triggers por evento, concurrencia, parameters, framework metadata-driven,
  idempotencia, retries, rutas de alerta y diseño amigable para CI/CD.
  `DP-700: Orchestrate → schedules/triggers y patrones`
  **Entregable:** `pl_orchestrate` con metadata, dependencias y rama de fallo.

### Fase 2 — Transformación, lakehouse y warehouse (Días 9–13)

- [ ] **Día 9 — Modelado en lakehouse: medallion con criterio.**
  Bronze/silver/gold, schemas, diseño de tablas, particiones, tamaño de archivo,
  Delta features, lakehouse vs warehouse y cuándo una tabla es “gold” de verdad.
  `DP-700: Design → data store y dimensional model`
  **Entregable:** modelo de datos + DDL de silver/gold.

- [ ] **Día 10 — PySpark de producción: dedup, SCD2 y datos tardíos.**
  Duplicados, faltantes, late-arriving data, SCD1/SCD2, `MERGE`, evolución de esquema,
  cuarentena y quality gates.
  `DP-700: Transform → duplicados, faltantes y tardíos`
  **Entregable:** pipeline silver/gold con SCD2 y cuarentena.

- [ ] **Día 11 — Performance Spark: del plan al costo.**
  AQE, joins, skew, shuffle, partitioning, caching, Native Execution Engine, V-Order
  (deshabilitado por defecto en workspaces nuevos), `OPTIMIZE`, `VACUUM`, liquid
  clustering, Spark Advisor y benchmark antes/después.
  `DP-700: Optimize → lakehouse y Spark`
  **Entregable:** reporte de performance con métricas y decisión.

- [ ] **Día 12 — Fabric Data Warehouse: T-SQL sobre Delta sin mitos.**
  Arquitectura, superficie T-SQL (CTAS, INSERT/UPDATE/DELETE, `MERGE` GA, transacciones),
  SQL analytics endpoint vs warehouse, estadísticas, clonación/time travel, límites y
  cuándo NO usar warehouse.
  `DP-700: Transform → SQL; choose data store`
  **Entregable:** `wh_retailops` + scripts de marts.

- [ ] **Día 13 — Warehouse performance y modelado dimensional.**
  Star schema, SCD, estadísticas, Query Insights, concurrencia, GPU acceleration
  (Preview), guardrails y tuning de queries reales.
  `DP-700: Optimize → warehouse y query performance`
  **Entregable:** modelo dimensional + reporte de tuning de 3 queries.

### Fase 3 — Real-Time Intelligence y consumo (Días 14–17)

- [ ] **Día 14 — Real-Time Intelligence end-to-end.**
  Real-Time hub, Eventstream (fuentes, transformaciones, destinos), Eventhouse/KQL DB,
  ingesta, retention/caching y disponibilidad en OneLake.
  `DP-700: Streaming → eventstreams y eventhouse`
  **Entregable:** `es_pos_events` → `eh_retailops` funcionando.

- [ ] **Día 15 — KQL para ingenieros de datos.**
  Operadores tabulares, `summarize`, `bin`, ventanas tumbling/sliding/session, joins,
  `make-series`, anomalías y performance de KQL.
  `DP-700: Streaming → KQL y windowing`
  **Entregable:** KQL queryset con 10 consultas + dashboard base.

- [ ] **Día 16 — Streaming patterns y acción: tardíos, dedup y Activator.**
  Eventstream vs Spark Structured Streaming, checkpoints, watermarks, exactly-once,
  dedup, ventanas, Activator (reglas/acciones) y Real-Time Dashboards.
  `DP-700: Streaming engine, windowing y alertas`
  **Entregable:** dashboard operativo + alerta de stockout/fraude.

- [ ] **Día 17 — Semántica y consumo: Direct Lake, semantic models y agentes.**
  Direct Lake vs Import vs DirectQuery, framing, refresh, diseño de modelo, frontera con
  Power BI, data agents/Fabric IQ (Preview, fuera de trial) y cuándo aplican.
  `DP-700: Monitor → semantic model refresh; panorama`
  **Entregable:** `sm_retailops` + reporte + nota de consumo.

### Fase 4 — Producción: seguridad, CI/CD, operación y costo (Días 18–22)

- [ ] **Día 18 — Seguridad de verdad: de workspace a file-level.**
  Workspace roles, item permissions, OneLake security roles (RLS/CLS/file-level),
  warehouse RLS/CLS/OLS/DDM, sensitivity labels, endorsement, service principals,
  Private Link y least privilege.
  `DP-700: Security → workspace/item/row/column/file + DDM + labels`
  **Entregable:** matriz de acceso + RLS/CLS/DDM implementados y probados.

- [ ] **Día 19 — Ciclo de vida: Git, deployment pipelines y CI/CD.**
  Git integration, branching, deployment pipelines, variable library, deployment plans
  (Preview), branched workspaces (Preview), database projects (DACPAC/VS Code),
  fabric-cicd, Fabric CLI y Terraform.
  `DP-700: Lifecycle → version control, database projects, deployment pipelines`
  **Entregable:** repo + promoción dev/test/prod + pipeline automatizado.

- [ ] **Día 20 — Observabilidad: Monitoring hub, workspace monitoring y Capacity Metrics.**
  Monitoring hub, workspace monitoring (Eventhouse/KQL, 30 días por defecto), Capacity
  Metrics app, throttling, Spark Advisor, alertas con Activator y runbooks de incidente.
  `DP-700: Monitor → ingestion/transform/refresh; errores por workload`
  **Entregable:** dashboard de monitoreo + 3 alertas + runbook.

- [ ] **Día 21 — Costo y rendimiento: capacity engineering.**
  Consumo de CUs por workload, smoothing/throttling, pause/resume, right-sizing,
  benchmark, chargeback, guardrails y trade-offs costo/performance.
  `DP-700: Optimize → pipeline, warehouse, eventhouse, Spark, query`
  **Entregable:** modelo de costo + plan de ahorro medible.

- [ ] **Día 22 — Confiabilidad y calidad: SLAs, backfills y desastres.**
  Idempotencia, retries, checkpoints, schema drift, cuarentena, data contracts, SLAs,
  backfills, rollback, recuperación de workspace y continuidad.
  `DP-700: Monitor/optimize + operación real`
  **Entregable:** playbook de confiabilidad + simulación de fallo y recuperación.

### Fase 5 — Capstone y certificación (Días 23–24)

- [ ] **Día 23 — Capstone I: construir RetailOps 360 end-to-end.**
  Integrar batch + streaming + warehouse + semantic model + seguridad + CI/CD +
  observabilidad. Arquitectura final y decisiones.
  **Entregable:** solución funcionando + diagrama + README técnico.

- [ ] **Día 24 — Capstone II: architecture review, entrevista y DP-700.**
  Presentación de 10 minutos, preguntas de trade-offs e incidentes, práctica de
  entrevista en inglés, practice assessment de DP-700 y plan de brechas.
  **Entregable:** portafolio + score de mock + plan de examen (si aplica).

### Sprint opcional DP-700 (no cuenta en las 24)

- [ ] **Sprint A — Repaso por dominio + practice assessment 1.** 2–3 h.
- [ ] **Sprint B — Simulacro cronometrado + revisión de errores.** 2–3 h.
- [ ] **Sprint C — Weak areas + exam sandbox + logística.** 1–2 h.

Se activa solo si el estudiante decide presentar el examen. No reemplaza laboratorios.

---

## 8. Mapa de cobertura DP-700

> Referencia: *Study Guide for Exam DP-700*, actualizado 2026-11-05. Los tres dominios
> valen **30–35%** cada uno. El examen dura **100 minutos** y se aprueba con **700**.

| Dominio DP-700 | Sesiones donde se practica | Evidencia |
|---|---|---|
| Implement/manage: workspace settings | 1, 3, 7 | Workspace configurado + ADR |
| Implement/manage: lifecycle (Git, DB projects, deployment pipelines) | 19 | Repo + pipeline dev→test→prod |
| Implement/manage: security & governance | 18, 19 | Matriz RBAC + RLS/CLS/DDM + labels |
| Implement/manage: orchestration | 4, 8 | `pl_ingest_batch`, `pl_orchestrate` |
| Ingest/transform: loading patterns (full/incremental/streaming) | 5, 10, 14, 16 | Cargas incrementales + streaming |
| Ingest/transform: batch (shortcuts, mirroring, pipelines, Spark/SQL) | 2, 4, 5, 6, 7, 10, 12 | Lakehouse + warehouse |
| Ingest/transform: streaming (engine, eventstreams, KQL) | 14, 15, 16 | Eventhouse + dashboard + alerta |
| Monitor/optimize: monitor items & alerts | 20 | Monitoring dashboard + alertas |
| Monitor/optimize: resolve errors por workload | 20, 22 | Runbooks + simulación de fallos |
| Monitor/optimize: performance (lakehouse, pipeline, warehouse, streaming, Spark) | 11, 13, 16, 21 | Benchmarks + reportes |
| Transversal: entrevista y comunicación | 1–24 (drill diario) | Banco de entrevista + capstone |

**Cobertura explícita de subtemas sensibles:**

- Elegir pipeline vs notebook → Días 4 y 8.
- Elegir dataflow vs notebook vs T-SQL → Días 6, 7 y 12.
- Elegir data store → Días 3, 9 y 12.
- Elegir motor streaming → Día 16.
- Duplicados, faltantes y tardíos → Días 10 y 16.
- Denormalizar, agrupar y agregar → Días 10 y 13.
- Window functions en KQL → Días 15 y 16.
- Errores de pipeline/dataflow/notebook/eventhouse/eventstream/T-SQL → Día 20.
- Optimizar pipeline, warehouse, eventstream/eventhouse, Spark y queries → Días 11, 13, 16 y 21.

---

## 9. Estrategia de certificación DP-700

### Hechos verificados (2026-11-20)

- **Examen:** DP-700 — *Implementing Data Engineering Solutions Using Microsoft Fabric*.
- **Certificación:** Microsoft Certified: Fabric Data Engineer Associate (nivel intermedio).
- **Duración:** 100 minutos. **Aprobación:** 700/1000.
- **Dominios:** Implement/manage 30–35%; Ingest/transform 30–35%; Monitor/optimize 30–35%.
- **Idiomas:** incluye español, inglés, portugués (Brasil), francés, alemán, italiano,
  japonés, coreano y chino simplificado/tradicional.
- **Prerrequisitos formales:** ninguno. Se recomienda experiencia práctica.
- **Renovación:** evaluación gratuita anual en Microsoft Learn.
- **Registro:** cuenta personal MSA (no corporativa), vía Pearson VUE.

### Principio

El examen se presenta **después** de haber construido y operado el proyecto, no antes.
El curso prioriza laboratorios; el examen valida lo aprendido.

### Momentos de evaluación

1. **Después del Día 17:** practice assessment diagnóstico (sin estudiar).
   - Registrar score por dominio.
   - Si < 60%, reforzar Días 2–16 antes de seguir.
2. **Después del Día 22:** practice assessment completo.
   - Objetivo: **≥ 80%** y ningún dominio < 70%.
3. **Después del Día 24:** simulacro cronometrado + revisión.
   - Agendar solo si se cumple: **≥ 80% dos veces**, capstone funcionando y 20/25
     preguntas de entrevista respondidas con trade-offs.

### Recursos oficiales

- Study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-700
- Página de certificación: https://learn.microsoft.com/en-us/credentials/certifications/fabric-data-engineer-associate/
- Practice assessment (nuevo, AI Skills Navigator): https://aka.ms/DP700-PA
- Practice assessment legacy: https://aka.ms/DP700-LearnPA
- Exam sandbox: https://aka.ms/examdemo
- Exam prep video: https://aka.ms/DP700-ExamPrep
- Examen: https://learn.microsoft.com/en-us/credentials/certifications/exams/dp-700

### Regla de oro

Si una decisión del curso entra en conflicto entre “lo que pide el examen” y “lo que
harías en producción”, **gana producción**, y se añade una nota de “así lo pregunta el
examen”. Un senior no memoriza la UI; entiende el modelo.

---

## 10. Sistema de memoria, progreso y repetición

### 10.1 Estado de sesiones

Se actualiza al final de cada sesión:

| Campo | Cómo se llena |
|---|---|
| Día actual | Último día completado + 1 |
| Última sesión | Fecha y número de día |
| Próxima acción | Lección concreta a generar/dictar |
| Confianza | 1–5 (1 = no lo explico, 5 = lo enseño) |
| Entorno | Estado del trial/workspace/items |
| Certificación | Fecha de mock/examen o “no agendada” |

### 10.2 Tablero de confianza (actualizar tras cada día)

| Día | Tema | Confianza 1–5 | Evidencia (entregable) | Repaso D+1 | Repaso D+7 |
|---|---|---|---|---|---|
| 1 | Mapa mental + setup | — | — | — | — |
| 2 | OneLake/shortcuts | — | — | — | — |
| 3 | Capacidad/gobierno | — | — | — | — |
| 4 | Pipelines I | — | — | — | — |
| 5 | Incremental | — | — | — | — |
| 6 | Dataflow Gen2 | — | — | — | — |
| 7 | Spark/runtime | — | — | — | — |
| 8 | Orquestación | — | — | — | — |
| 9 | Medallion | — | — | — | — |
| 10 | SCD2/calidad | — | — | — | — |
| 11 | Performance Spark | — | — | — | — |
| 12 | Warehouse | — | — | — | — |
| 13 | Tuning warehouse | — | — | — | — |
| 14 | RTI/Eventstream | — | — | — | — |
| 15 | KQL | — | — | — | — |
| 16 | Streaming/Activator | — | — | — | — |
| 17 | Semántica/Direct Lake | — | — | — | — |
| 18 | Seguridad | — | — | — | — |
| 19 | CI/CD | — | — | — | — |
| 20 | Observabilidad | — | — | — | — |
| 21 | Costo | — | — | — | — |
| 22 | Confiabilidad | — | — | — | — |
| 23 | Capstone I | — | — | — | — |
| 24 | Capstone II/entrevista | — | — | — | — |

### 10.3 Puntos débiles (error log)

| Fecha | Concepto | Qué falló | Causa raíz | Remedio | Revisar el |
|---|---|---|---|---|---|
| — | — | — | — | — | — |

Regla: un punto débil no se cierra hasta que el estudiante lo explica sin ayuda y lo
aplica en un ejercicio nuevo.

### 10.4 Repetición espaciada

| Tarjeta / concepto | Día origen | D+1 | D+3 | D+7 | D+14 | Estado |
|---|---|---|---|---|---|---|
| — | — | — | — | — | — | Pendiente |

Cada lección agrega 3–5 tarjetas. El agente debe preguntarlas al inicio de la sesión
siguiente y actualizar el estado.

### 10.5 Banco de entrevista

Vive en `progress/interview-bank.md`. Cada pregunta se practica en voz alta, en español
y en inglés, con respuesta de 90–120 segundos que incluya: contexto → decisión →
trade-off → métrica → qué haría distinto.

Preguntas semilla (se amplía durante el curso):

1. ¿Qué es Fabric y cómo se diferencia de Databricks y Synapse?
2. Explica capacity, workspace e item. ¿Por qué se throttlea un pipeline?
3. Shortcut vs mirroring vs copiar datos: ¿cómo decides?
4. ¿Cuándo usar lakehouse y cuándo warehouse?
5. ¿Cómo implementas una carga incremental idempotente?
6. ¿Cómo manejas datos tardíos en batch y en streaming?
7. ¿Cómo garantizas exactly-once en streaming?
8. ¿Eventstream o Spark Structured Streaming? Justifica.
9. ¿Cómo diseñas un modelo medallion para batch + streaming?
10. ¿Cómo implementas SCD2 sin duplicar filas?
11. ¿Cómo optimizas un job de Spark lento?
12. ¿Cómo optimizas una query lenta en el warehouse?
13. ¿Cómo diagnosticas un pipeline que falla a las 3 a.m.?
14. ¿Cómo observas freshness y latencia end-to-end?
15. ¿Cómo implementas RLS, CLS y DDM?
16. ¿Cómo gobiernas OneLake con dominios, endorsement y labels?
17. ¿Cómo promueves cambios de dev a prod en Fabric?
18. ¿Cómo manejas secretos y conexiones?
19. ¿Cómo estimas y controlas el costo de Fabric?
20. ¿Qué harías si el volumen crece 10x?
21. Cuéntame un incidente que causaste y qué cambiaste.
22. ¿Cómo pruebas pipelines y datos?
23. ¿Cómo manejas schema drift?
24. ¿Qué límites de Fabric te han obligado a cambiar un diseño?
25. ¿Cómo explicarías esta arquitectura a un CFO?

---

## 11. Flujo de trabajo del agente (por sesión)

1. **Leer** este archivo completo, `progress/session-log.md` y el estado actual.
2. **Ubicar** el primer día sin `[x]`.
3. **Verificar prerrequisitos:** si el día anterior no está cerrado, preguntar si se
   repasa o se continúa; no asumir.
4. **Verificar documentación** del día (ver sección 12): 3–6 enlaces oficiales, fecha de
   actualización, estado GA/Preview y límites del trial.
5. **Generar** con el skill `fabric-day-generator` o el comando `/dia-fabric N`:
   `lessons/dia-XX-*.html`, `exercises/dia-XX-ejercicios.html` y
   `solutions/dia-XX-solucion.html`. Lección completa, sin resumir; HTML visual del Día 4.
6. **Actualizar** navegación anterior/siguiente, `index.html` (días publicados), este
   archivo (estado y plan) y `progress/session-log.md`.
7. **Validar** con `python .opencode/skills/fabric-day-generator/scripts/check_day.py N`
   y abrir las tres páginas en navegador (`file://`, 360 px, tema claro/oscuro).
8. **Dictar la clase de forma interactiva:** no volcar toda la lección de una vez.
   Empezar por recuperación y gancho; esperar respuestas; avanzar por bloques.
9. **Hacer predecir antes de ejecutar:** “¿qué crees que pasará?” y luego comparar.
10. **Evaluar** con quiz, teach-back y rúbrica. Registrar errores.
11. **Actualizar** confianza, puntos débiles, repetición espaciada, banco de entrevista y
    `session-log.md` cuando el alumno cierre la sesión.
12. **Recomendar** la fecha de la siguiente sesión (idealmente D+1 o D+2) y el repaso.
13. **No hacer commit ni push** salvo que el usuario lo pida explícitamente.

**Regla:** el material de un día puede generarse antes de dictarlo, pero no se marca como
completado ni se avanza al siguiente hasta que el alumno cierre el entregable, salvo
petición explícita.

---

## 12. Reglas de verificación de contenido (anti-alucinación)

Fabric cambia cada mes. Antes de escribir una lección:

1. **Abrir los enlaces oficiales** del tema en `learn.microsoft.com`.
2. **Revisar `ms.date` / `updated_at`** y anotar “Docs verificadas: YYYY-MM-DD” en la
   cabecera de la lección.
3. **Distinguir GA vs Preview.** Si es Preview: marcarlo, dar alternativa GA y decir si
   está disponible en trial.
4. **Revisar límites del trial** (sección 4). Si el laboratorio no se puede hacer, dar
   plan B con lakehouse/warehouse/notebook o dejarlo como lectura.
5. **No inventar etiquetas de UI.** Si no estás seguro del nombre exacto, describir la
   acción (“abre la configuración de Spark del workspace”) y enlazar la captura/doc.
6. **No inventar benchmarks, precios ni métricas.** Citar la fuente o etiquetar como
   estimación.
7. **Código:** probarlo localmente cuando sea posible. Si no se ejecutó, decirlo.
8. **Enlaces:** verificar que respondan 200 antes de publicarlos.
9. **Fecha de verificación:** si un artículo cambió, actualizar la lección y anotar el
   cambio en el historial (sección 15).

### Checklist de calidad de una lección

- [ ] Objetivos medibles (4–5).
- [ ] Recuperación activa de 5 preguntas.
- [ ] Gancho de RetailOps 360 con consecuencia de negocio.
- [ ] Analogía + diagrama.
- [ ] Teoría completa, sin resumir.
- [ ] 3 ejemplos de dificultad creciente.
- [ ] Code review junior vs. profesional con /10.
- [ ] Demo guiada con predicciones y decisiones explicadas.
- [ ] Lente DP-700 con mini caso.
- [ ] Laboratorio de 3 misiones con criterio de éxito.
- [ ] “Lo que un senior ve” (trade-offs/costo/fallos).
- [ ] Drill de entrevista con follow-ups y versión corta en inglés.
- [ ] Teach-back, cheat sheet y 3–5 tarjetas de repetición.
- [ ] Entregable con checklist.
- [ ] Referencias oficiales verificadas.
- [ ] Entregable concreto.
- [ ] Nada depende de Copilot/AI no disponible en trial.
- [ ] Sin emojis, CDN, fuentes externas ni colores inline.
- [ ] Responsive 360/768/escritorio; tema claro/oscuro; foco visible.
- [ ] La lección está en HTML, completa y sin resumir; la interactividad es opcional.

---

## 13. Rúbrica senior y criterios de graduación

### Rúbrica (0–3 por criterio)

| Criterio | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Corrección técnica | No funciona | Funciona con ayuda | Funciona solo | Funciona y está probado |
| Trade-offs | No los menciona | Menciona uno | Compara alternativas | Decide con criterio y datos |
| Operación | Ignora fallos | Detecta alguno | Tiene retries/logs | Runbook, alertas y rollback |
| Costo/performance | No mide | Mide mal | Mide y mejora | Optimiza con benchmark y costo |
| Seguridad/gobierno | No aplica | Aplica lo básico | Least privilege | RLS/CLS/DDM + auditoría |
| Comunicación | Confuso | Entendible | Claro | Claro, breve y para audiencia |

**Aprobado:** promedio ≥ 2.5 y ningún criterio en 0.

### Graduación

El curso se considera completado cuando:

- [ ] Los 24 días están marcados y con entregable.
- [ ] El capstone corre end-to-end y está documentado en inglés.
- [ ] El estudiante dibuja la arquitectura de memoria en ≤ 5 minutos.
- [ ] Responde 20/25 preguntas del banco con trade-offs, en español y en inglés.
- [ ] Tiene un postmortem escrito de un fallo simulado.
- [ ] Tiene un modelo de costos y un plan de optimización.
- [ ] (Opcional) Practice assessment DP-700 ≥ 80% dos veces.

---

## 14. Referencias oficiales

### Microsoft Learn — rutas del curso

- Get started with Microsoft Fabric: https://learn.microsoft.com/en-us/training/paths/get-started-fabric/
- Implement a Lakehouse with Microsoft Fabric: https://learn.microsoft.com/en-us/training/paths/implement-lakehouse-microsoft-fabric/
- Ingest data with Microsoft Fabric: https://learn.microsoft.com/en-us/training/paths/ingest-data-with-microsoft-fabric/
- Implement a data warehouse with Microsoft Fabric: https://learn.microsoft.com/en-us/training/paths/work-with-data-warehouses-using-microsoft-fabric/
- Implement Real-Time Intelligence with Microsoft Fabric: https://learn.microsoft.com/en-us/training/paths/explore-real-time-analytics-microsoft-fabric/
- Secure and govern analytics data in Microsoft Fabric: https://learn.microsoft.com/en-us/training/paths/secure-govern-analytics-data/
- Manage a Microsoft Fabric environment: https://learn.microsoft.com/en-us/training/paths/manage-microsoft-fabric-environment/
- Explore analytics data stores: https://learn.microsoft.com/en-us/training/paths/explore-analytics-data-stores/
- Design and transform analytics data: https://learn.microsoft.com/en-us/training/paths/design-transform-analytics-data/
- Prepare AI-ready analytics data: https://learn.microsoft.com/en-us/training/paths/prepare-ai-ready-analytics-data/
- Get started with Fabric IQ: https://learn.microsoft.com/en-us/training/paths/get-started-fabric-iq/

### Documentación clave (verificada 2026-11-20)

- Fabric overview: https://learn.microsoft.com/en-us/fabric/fundamentals/microsoft-fabric-overview
- What's new in Fabric: https://learn.microsoft.com/en-us/fabric/fundamentals/whats-new
- Trial capacity: https://learn.microsoft.com/en-us/fabric/fundamentals/fabric-trial
- Licenses and capacity: https://learn.microsoft.com/en-us/fabric/enterprise/licenses
- Buy capacity: https://learn.microsoft.com/en-us/fabric/enterprise/buy-capacity
- Throttling: https://learn.microsoft.com/en-us/fabric/enterprise/throttling
- OneLake overview: https://learn.microsoft.com/en-us/fabric/onelake/onelake-overview
- OneLake shortcuts: https://learn.microsoft.com/en-us/fabric/onelake/onelake-shortcuts
- OneLake security: https://learn.microsoft.com/en-us/fabric/onelake/security/get-started-onelake-security
- Mirroring: https://learn.microsoft.com/en-us/fabric/mirroring/overview
- Lakehouse: https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-overview
- Spark runtime: https://learn.microsoft.com/en-us/fabric/data-engineering/runtime
- Notebooks: https://learn.microsoft.com/en-us/fabric/data-engineering/how-to-use-notebook
- Spark compute: https://learn.microsoft.com/en-us/fabric/data-engineering/spark-compute
- Environments: https://learn.microsoft.com/en-us/fabric/data-engineering/environment-manage-compute
- Native execution engine: https://learn.microsoft.com/en-us/fabric/data-engineering/native-execution-engine-overview
- Delta optimization / V-Order: https://learn.microsoft.com/en-us/fabric/data-engineering/delta-optimization-and-v-order
- Liquid clustering: https://learn.microsoft.com/en-us/fabric/data-engineering/liquid-clustering
- Spark monitoring/Advisor: https://learn.microsoft.com/en-us/fabric/data-engineering/spark-monitor-debug
- Data Factory overview: https://learn.microsoft.com/en-us/fabric/data-factory/data-factory-overview
- Activities: https://learn.microsoft.com/en-us/fabric/data-factory/activity-overview
- Pipeline overview: https://learn.microsoft.com/en-us/fabric/data-factory/pipeline-overview
- Parameters: https://learn.microsoft.com/en-us/fabric/data-factory/parameters
- Expressions and functions: https://learn.microsoft.com/en-us/fabric/data-factory/expression-language
- Activity retries: https://learn.microsoft.com/en-us/fabric/data-factory/activity-retries
- Pipeline runs/triggers: https://learn.microsoft.com/en-us/fabric/data-factory/pipeline-runs
- Invoke pipeline: https://learn.microsoft.com/en-us/fabric/data-factory/invoke-pipeline-activity
- Copy job: https://learn.microsoft.com/en-us/fabric/data-factory/what-is-copy-job
- Dataflow Gen2: https://learn.microsoft.com/en-us/fabric/data-factory/dataflows-gen2-overview
- Warehouse: https://learn.microsoft.com/en-us/fabric/data-warehouse/data-warehousing
- T-SQL surface area: https://learn.microsoft.com/en-us/fabric/data-warehouse/tsql-surface-area
- Warehouse security: https://learn.microsoft.com/en-us/fabric/data-warehouse/security
- Row-level security: https://learn.microsoft.com/en-us/fabric/data-warehouse/row-level-security
- Dynamic data masking: https://learn.microsoft.com/en-us/fabric/data-warehouse/dynamic-data-masking
- Query insights: https://learn.microsoft.com/en-us/fabric/data-warehouse/query-insights
- Development/deployment (warehouse): https://learn.microsoft.com/en-us/fabric/data-warehouse/development-deployment
- Real-Time Intelligence: https://learn.microsoft.com/en-us/fabric/real-time-intelligence/overview
- Eventhouse: https://learn.microsoft.com/en-us/fabric/real-time-intelligence/eventhouse
- Eventstream: https://learn.microsoft.com/en-us/fabric/real-time-intelligence/event-streams/overview
- Activator: https://learn.microsoft.com/en-us/fabric/real-time-intelligence/data-activator/activator-introduction
- Real-Time dashboards: https://learn.microsoft.com/en-us/fabric/real-time-intelligence/dashboard-real-time-create
- KQL: https://learn.microsoft.com/en-us/kusto/query/
- Direct Lake: https://learn.microsoft.com/en-us/fabric/get-started/direct-lake-overview
- Semantic models: https://learn.microsoft.com/en-us/fabric/data-warehouse/semantic-models
- OneLake catalog: https://learn.microsoft.com/en-us/fabric/governance/onelake-catalog-overview
- Domains: https://learn.microsoft.com/en-us/fabric/governance/domains
- Endorsement: https://learn.microsoft.com/en-us/fabric/governance/endorsement-overview
- Workspace roles: https://learn.microsoft.com/en-us/fabric/fundamentals/roles-workspaces
- Monitoring hub: https://learn.microsoft.com/en-us/fabric/admin/monitoring-hub
- Workspace monitoring: https://learn.microsoft.com/en-us/fabric/fundamentals/workspace-monitoring-overview
- Capacity Metrics app: https://learn.microsoft.com/en-us/fabric/enterprise/metrics-app
- CI/CD overview: https://learn.microsoft.com/en-us/fabric/cicd/cicd-overview
- Git integration: https://learn.microsoft.com/en-us/fabric/cicd/git-integration/intro-to-git-integration
- Deployment pipelines: https://learn.microsoft.com/en-us/fabric/cicd/deployment-pipelines/intro-to-deployment-pipelines
- Variable library: https://learn.microsoft.com/en-us/fabric/cicd/variable-library/variable-library-overview
- Deployment plan: https://learn.microsoft.com/en-us/fabric/cicd/deployment-plan/deployment-plan-overview
- Branched workspaces: https://learn.microsoft.com/en-us/fabric/cicd/git-integration/branched-workspace
- Fabric CLI: https://learn.microsoft.com/en-us/rest/api/fabric/articles/fabric-command-line-interface
- fabric-cicd: https://microsoft.github.io/fabric-cicd/
- Fabric IQ (Preview): https://learn.microsoft.com/en-us/fabric/iq/overview
- Data agents (Preview): https://learn.microsoft.com/en-us/fabric/data-science/concept-data-agent

### Blogs y roadmap

- Fabric blog: https://blog.fabric.microsoft.com/
- Fabric roadmap: https://roadmap.fabric.microsoft.com/
- Fabric community: https://community.fabric.microsoft.com/
- Fabric ideas: https://ideas.fabric.microsoft.com/

---

## 15. Historial de cambios de este archivo

| Fecha | Cambio |
|---|---|
| 2026-11-20 | **Edición HTML canónica:** se elimina el build step y los `.md`; se adopta el sistema visual del curso Data CI/CD, el Día 4 reconstruido con assets compartidos y el skill `fabric-day-generator` + `/dia-fabric`. Días 1–3 se conservan como completados en el cuaderno anterior. |
| 2026-11-20 | La lección canónica pasa de `.md` a **HTML** desde el Día 4 (completa, sin resumir; didáctica antes que interactividad). Día 4 generado; primera versión con build script, reemplazada por la edición HTML canónica. |
| 2026-11-20 | Día 3 generado. Los ejercicios incluyen espacio de respuesta a pedido del estudiante. |
| 2026-11-11 | Día 2: shortcut transformations CSV/Parquet/JSON pasan a GA (Excel sigue Preview); Día 1 cerrado como parcial. |
| 2026-11-09 | Creación del curso, plan de 24 sesiones, reglas de trial, proyecto RetailOps 360 y sistema de memoria. |

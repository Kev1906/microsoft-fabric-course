---
name: fabric-day-generator
description: Genera una sesión completa del Microsoft Fabric Master Course de RetailOps 360 (lección, laboratorio y solución en HTML) con el estilo visual y la profundidad del Día 4. Úsalo cuando el usuario pida "genera el Día 5", "siguiente sesión de Fabric", "crea dia-05", "nuevo día del curso de Fabric" o recursos HTML para un día concreto de este repositorio.
---

# Fabric Day Generator

## Misión

Crear una sesión completa del **Microsoft Fabric Master Course** —lección, laboratorio y solución— con la misma profundidad, tono y sistema visual del Día 4. El objetivo no es producir HTML bonito: es que el alumno **entienda, construya, mida y defienda** decisiones de plataforma en Microsoft Fabric.

Este skill es específico de este repositorio y del proyecto **RetailOps 360**. Si la petición no es sobre este curso, no lo uses.

## Estado del curso

- Días 1–3: completados en el cuaderno anterior (mapa mental, OneLake, capacity y gobierno). No se regeneran.
- Día 4: primera sesión canónica en HTML; plantilla visual y de contenido.
- Siguiente: Día 5 — ingesta incremental y conectividad real.
- Formato: 24 sesiones de 2.5–3 h, 3 por semana.
- Certificación: DP-700 es consecuencia, no requisito.

## Cuándo se activa

- “Genera el Día 5.”
- “Siguiente sesión de Fabric.”
- “Crea `dia-05-*.html`.”
- “Haz lección, laboratorio y solución del Día 6.”
- `/dia-fabric 5` (comando del proyecto).

**No lo uses para:** generar varios días en lote, reescribir los Días 1–4, cambiar el sistema visual o crear contenido genérico de Fabric sin RetailOps 360.

## 0. Contexto obligatorio antes de escribir

Lee, en este orden:

1. `AGENTS.md` — reglas del curso, plan de 24 sesiones, estado, DP-700 y restricciones del trial.
2. `assets/course.css` y `assets/course.js` — componentes, tokens e interacciones.
3. `lessons/dia-04-data-factory-pipelines-i.html` — **shell canónico**, tono y estructura.
4. `exercises/dia-04-ejercicios.html` y `solutions/dia-04-solucion.html` — formato de laboratorio y rúbrica.
5. `index.html` — roadmap, días publicados y estado de fases.
6. El día anterior completo. Si no existe, no generes un día que dependa de él sin avisar.
7. `progress/session-log.md` y `progress/interview-bank.md` — estado del alumno y preguntas.
8. `docs` o `AGENTS.md` para las referencias del tema.
9. Documentación oficial de Microsoft Learn del tema. Verifica `ms.date`/`updated_at`, estado GA/Preview y límites del trial. Anota la fecha real de verificación.

Fabric cambia cada mes. No inventes etiquetas de UI, precios, benchmarks ni límites. Si no puedes verificar algo, descríbelo como acción y enlaza la doc; si es Preview, márcalo y da alternativa GA.

## 1. Fija el alcance

- Si el usuario da un número, úsalo. Si no, infiere el siguiente día faltante según el plan de `AGENTS.md`.
- Valida que esté entre 1 y 24.
- No generes un día si el anterior no está cerrado, salvo petición explícita. El curso es secuencial.
- Identifica:
  - día anterior y sus tres archivos;
  - día siguiente y si ya existe;
  - fase y duración;
  - herramientas que aparecen por primera vez;
  - subtemas DP-700 que cubre;
  - límites del trial que afectan el laboratorio.
- **Genera un solo día por invocación.** No encadenes días: la profundidad se degrada.

## 2. Planifica antes de escribir

Haz un esquema privado con:

- Una frase de objetivo.
- 4–5 resultados medibles (“al terminar podrás…”).
- 5 preguntas de recuperación de días anteriores.
- Un gancho de negocio o incidente de RetailOps 360.
- Una analogía cotidiana que explique el concepto central.
- Diagrama del flujo o arquitectura, con el riesgo que reduce cada parada.
- 3 ejemplos de dificultad creciente.
- Un code review junior vs. profesional con puntuación y “por qué no es 10”.
- Demo guiada paso a paso, con decisiones explicadas.
- Lente senior: trade-offs, blast radius, costo, seguridad, cuándo NO usar.
- Sección “Así lo pregunta DP-700” con un mini caso.
- 3 misiones de laboratorio: guiada, independiente y senior.
- 5–6 errores frecuentes.
- Drill de entrevista con respuesta modelo y follow-ups, en español y una versión corta en inglés.
- Teach-back de 2 minutos, cheat sheet y 3–5 tarjetas de repetición.
- Entregable y checklist.
- Referencias oficiales verificadas.

## 3. Contrato de contenido

### Reglas pedagógicas

- El alumno ya domina SQL, Python, Spark/Databricks, dbt y Git. **No re-enseñes esos fundamentos**; conéctalos con Fabric.
- Explica cada concepto nuevo desde el problema de negocio. Una idea a la vez.
- No uses “obvio”, “simplemente”, “solo tienes que” ni relleno motivacional.
- Cada sesión empieza con recuperación activa, no con una definición.
- Predicción antes de ejecutar: “¿qué crees que pasará?” y luego comparar.
- Teoría completa, sin resumir. Si hay que elegir, se sacrifica interactividad, no claridad.
- Nada de emojis. Usa SVG, símbolos tipográficos o texto.
- Nada de datos, capturas, código o credenciales de empleadores. Solo RetailOps 360 sintético.
- Si una feature está en **Preview**, dilo y ofrece alternativa GA.
- Si el laboratorio no se puede hacer en trial, dilo antes y da plan B.
- No prometas salarios ni resultados garantizados.

### Lección

Estructura mínima (puedes añadir subsecciones):

1. Hero: día, fase, duración, DP-700, nivel, título y objetivo.
2. TL;DR “En 30 segundos” y agenda de la sesión.
3. Recuperación activa (5 preguntas con respuestas revelables).
4. Gancho narrativo de RetailOps 360.
5. Modelo mental con analogía y diagrama.
6. Teoría esencial completa: conceptos, tablas, flujo y “qué pasa si…”.
7. 3 ejemplos de dificultad creciente.
8. Code review junior vs. profesional con /10 y por qué no es 10.
9. Demo guiada “yo lo hago”, paso a paso, con predicciones.
10. “Lo que un senior ve”: trade-offs, costo, fallos, alternativas y cuándo NO.
11. Lente DP-700 con mini caso y respuesta.
12. Laboratorio: enlace a las 3 misiones y criterio de éxito.
13. Errores frecuentes y anti-patrones.
14. Drill de entrevista (español + inglés) con follow-ups.
15. Teach-back, cheat sheet y repetición espaciada.
16. Entregable + checklist persistente.
17. Referencias oficiales con fecha de verificación.

Duración objetivo: 2.5–3 h de sesión; la lección debe poder leerse y usarse como material de clase.

### Laboratorio

- **Tres misiones de la vida real**, con contexto narrativo (Slack, email, incidente, reunión).
- Personas con nombre y rol; presión de negocio realista.
- Cada misión: contexto, tarea, entregable, restricciones, pistas colapsables, tiempo y dificultad.
- Misión 1 guiada; Misión 2 independiente; Misión 3 senior (incidente, trade-off, costo, seguridad o escala).
- La misión senior debe pedir **decisión + justificación + medición**, no solo clics.
- **No incluyas soluciones** ni fragmentos que delaten la respuesta.
- Cierra con checklist “antes de abrir la solución” y bonus de entrevista.
- Total: 75–120 minutos de laboratorio.

### Solución

- Empieza por **cómo se aborda**, no por la respuesta.
- Incluye artefactos: líneas de tiempo, tablas, diagramas, mensajes, ADR, runbook, expresiones.
- Añade “lo que no haría” y los trade-offs.
- Rúbrica 0–3 por criterio (6 criterios), aprobado con promedio ≥2.5 y ningún 0.
- Aclara que no hay una única respuesta correcta: se evalúa razonamiento, evidencia y operabilidad.
- Incluye señales de 3/3 y errores que bajan la nota.

## 4. Contrato visual

### Shell obligatorio

Copia el shell de `lessons/dia-04-data-factory-pipelines-i.html` y adapta:

- `<head>`: `lang="es"`, charset, viewport, title, description, `../assets/course.css` y script de tema con `fabric-theme`.
- `<body>`: skip link, `.reading-progress`, `.shell`, `.sidebar`, `.topbar`, `.page-grid`, `.article`, `.toc`, footer y `../assets/course.js`.
- Sidebar:
  - Días 1–3 como `is-complete` (sin enlace).
  - Día actual activo con `aria-current="page"`.
  - Subenlaces Lección / Laboratorio / Solución.
  - Días futuros como `is-locked`.
- Enlaces relativos correctos desde `lessons/`, `exercises/` o `solutions/`.
- Todas las páginas se enlazan entre sí.

### Componentes

Reutiliza los existentes:

- Callouts: `.callout--key`, `.callout--warn`, `.callout--staff`, `.callout--story`, `.callout--exam`.
- Tarjetas: `.card`, `.grid--2`, `.grid--3`.
- Flujos: `.rail`, `.compare`, `.arch`, `.agenda`.
- Mensajes: `.message`, `.message--email`, `.message--alert`.
- Misiones: `.mission`, `.deliverable`, `.hint-row`.
- Evaluación: `.rubric`, `.score-scale`, `.checklist`, `.quiz`, `.reveal`.
- Datos: `.table-wrap`, `.kpis`, `.sev`, `.outcomes`.
- Código: `.code-block`, `.code-head`, `.tok-com`, `.tok-key`, `.tok-str`.

No inventes colores inline. Usa los tokens. Si necesitas un componente nuevo, añádelo a `assets/course.css` con tokens y úsalo de forma consistente.

### Reglas visuales

- Sin CDN, fuentes externas, frameworks ni imágenes externas.
- Sin emojis.
- Un solo `<h1>` por página.
- Contraste suficiente, foco visible, `aria-label` útil y `prefers-reduced-motion`.
- Debe funcionar en 360 px, 768 px y escritorio; sin scroll horizontal del body; tablas dentro de `.table-wrap`.
- Tema claro y oscuro con persistencia (`fabric-theme`).
- La barra de progreso, TOC activo, copiar código y checklists deben funcionar.
- El contenido debe ser legible sin JavaScript.

### Nombres de archivo

- Lección: `lessons/dia-XX-<slug>.html` (slug corto, en inglés o español, sin espacios).
- Laboratorio: `exercises/dia-XX-ejercicios.html`.
- Solución: `solutions/dia-XX-solucion.html`.
- No crees `.md` paralelos. El HTML es la fuente de verdad.

## 5. Actualiza navegación, índice y memoria

Al terminar:

1. Actualiza los enlaces “Siguiente” del día anterior en sus tres páginas.
2. En las páginas nuevas, enlaza “Anterior” al día anterior y “Siguiente” al siguiente si existe.
3. Si el siguiente no existe, enlaza `../index.html#recorrido` con “Próximamente / Portada”. No inventes URLs.
4. En `index.html`:
   - añade el día a `.day-list`;
   - actualiza la fase y el estado;
   - conserva los días futuros como “Próximamente”.
5. En `AGENTS.md`:
   - actualiza “Día actual”, “Última sesión” y “Próxima acción”;
   - actualiza el checklist del plan (sin marcar una sesión como completada si el alumno no la cerró);
   - añade una fila al historial de cambios si cambió el estado.
6. En `progress/session-log.md`, añade la sesión como “material generado / sesión pendiente” hasta que el alumno la cierre.

## 6. Validación obligatoria

Ejecuta:

```bash
python .opencode/skills/fabric-day-generator/scripts/check_day.py DAY
```

Debe terminar en `RESULTADO: OK`.

Después verifica en navegador con `file://`:

- [ ] Las tres páginas abren sin errores de consola.
- [ ] Barra de progreso, tema, copiar, TOC y checklists funcionan.
- [ ] A 360 px no hay scroll horizontal del body.
- [ ] Las tablas hacen scroll dentro de su contenedor.
- [ ] Tema claro y oscuro se ven bien.
- [ ] Navegación por teclado y foco visible.
- [ ] Todos los enlaces locales resuelven.
- [ ] Sin IDs duplicados ni más de un `<h1>`.
- [ ] Jerarquía de headings correcta.

Si no puedes abrir el navegador, dilo y revisa el HTML manualmente.

## 7. Auditoría de contenido

- [ ] Recuperación activa de 5 preguntas.
- [ ] Gancho de RetailOps 360 con consecuencia de negocio.
- [ ] Analogía + diagrama.
- [ ] Teoría completa, no resumida.
- [ ] 3 ejemplos de dificultad creciente.
- [ ] Code review con /10 y por qué no es 10.
- [ ] Demo guiada con predicciones.
- [ ] Lente senior con trade-offs y costo.
- [ ] Sección DP-700 con mini caso.
- [ ] 3 misiones reales sin soluciones.
- [ ] Solución con razonamiento, artefactos, “lo que no haría” y rúbrica.
- [ ] Drill de entrevista en español y versión corta en inglés.
- [ ] Teach-back, cheat sheet y 3–5 tarjetas.
- [ ] Entregable con checklist.
- [ ] Fuentes oficiales verificadas y fecha real.
- [ ] Sin Copilot/AI/Private Link en el camino crítico del trial.
- [ ] Sin datos de empleadores.
- [ ] Sin emojis.

## 8. Entrega

Responde de forma breve con:

- Archivos creados.
- Qué aprende el alumno y qué podrá demostrar.
- Fuentes verificadas y fecha.
- Resultado de `check_day.py`.
- Limitaciones o verificaciones pendientes.
- Recordatorio de que no se ha hecho commit salvo petición.

No hagas commit ni push. No generes el día siguiente sin que el usuario lo pida.

## Errores que debes evitar

- Generar varios días de golpe.
- Copiar el Día 4 y cambiar solo el título.
- Re-enseñar Spark o SQL desde cero.
- Inventar límites, precios, benchmarks o etiquetas de UI.
- Usar Copilot/AI/Private Link como dependencia del laboratorio.
- Convertir las misiones en tickets corporativos.
- Incluir soluciones en el laboratorio.
- Usar emojis, colores inline, CDN o fuentes externas.
- Romper enlaces relativos o duplicar IDs.
- Olvidar actualizar índice, navegación, AGENTS y progreso.
- Marcar una sesión como completada sin evidencia del alumno.

## Referencia rápida

- Shell y tono: `lessons/dia-04-data-factory-pipelines-i.html`.
- Laboratorio canónico: `exercises/dia-04-ejercicios.html`.
- Rúbrica canónica: `solutions/dia-04-solucion.html`.
- Reglas del curso: `AGENTS.md`.
- Sistema visual: `assets/course.css` y `assets/course.js`.
- Validador: `.opencode/skills/fabric-day-generator/scripts/check_day.py`.
- Datos: `datasets/generate_retailops.py`.

# RetailOps 360 · Microsoft Fabric Master Course

> De clics sueltos a criterio de plataforma. 24 sesiones para diseñar, construir y operar una plataforma de datos en Microsoft Fabric, con DP-700 como consecuencia.

## Empieza aquí

Abre **`index.html`** con doble clic. No hay build step, servidor ni dependencias: el curso funciona offline con `file://`.

- Portada y roadmap: `index.html`
- Lección actual: `lessons/dia-04-data-factory-pipelines-i.html`
- Laboratorio actual: `exercises/dia-04-ejercicios.html`
- Solución y rúbrica: `solutions/dia-04-solucion.html`

## Estado

Los **Días 1–3** se completaron en el cuaderno anterior: mapa mental de Fabric, OneLake y capacity/gobierno. Esta edición visual retoma en el **Día 4 — Data Factory pipelines I**.

- Día actual: **04 / 24**
- Formato: HTML autocontenido, tema claro/oscuro, responsive, sin CDN
- Proyecto: **RetailOps 360**
- Certificación: **DP-700 no agendada**; es una consecuencia del curso, no un requisito

## Qué vas a dominar

- El modelo mental de Fabric: tenant, capacity, workspace, item, OneLake y workloads.
- Ingesta batch y streaming con Data Factory, Eventstream y notebooks.
- Lakehouse y Warehouse: cuándo usar cada uno y cómo se complementan.
- PySpark de producción: deduplicación, SCD2, datos tardíos y performance.
- T-SQL sobre Delta, modelado dimensional y tuning.
- KQL, Real-Time Intelligence, Activator y consumo con Direct Lake.
- Seguridad, gobierno, CI/CD, observabilidad, costo y confiabilidad.
- Comunicación de trade-offs y defensa de arquitectura en entrevistas senior.

## Cómo se aprende

Cada sesión de 2.5–3 h sigue el mismo contrato:

1. **Recuperación activa:** preguntas de días anteriores.
2. **Gancho:** un incidente o decisión real de RetailOps 360.
3. **Modelo mental + teoría esencial:** analogía, diagrama y concepto.
4. **Demo guiada:** el docente ejecuta y explica decisiones.
5. **Laboratorio:** tú construyes, rompes y mides.
6. **Lente senior + DP-700:** trade-offs, costo, fallos y pregunta de examen.
7. **Drill de entrevista + teach-back:** explicas el tema en 90–120 segundos.
8. **Entregable + repetición espaciada:** evidencia y tarjetas de repaso.

## Estructura

```text
Microsoft Fabric/
├── index.html
├── AGENTS.md
├── README.md
├── assets/
│   ├── course.css
│   └── course.js
├── lessons/dia-04-data-factory-pipelines-i.html
├── exercises/dia-04-ejercicios.html
├── solutions/dia-04-solucion.html
├── datasets/
│   ├── generate_retailops.py
│   └── README.md
├── progress/
│   ├── session-log.md
│   └── interview-bank.md
└── .opencode/
    ├── command/dia-fabric.md
    └── skills/fabric-day-generator/
```

## Requisitos

- SQL intermedio/avanzado, Python de producción, Spark/Databricks, dbt y Git.
- Un tenant de práctica con Fabric Trial (60 días, F4/F64) o una capacity F de pago.
- Datos sintéticos generados con `datasets/generate_retailops.py`.
- Nunca uses datos, código propietario, capturas o credenciales de tus empleadores.

## Generar las siguientes sesiones

Cuando el Día 4 esté cerrado:

```text
/dia-fabric 5
```

O pide: “usa fabric-day-generator para el Día 5”. El skill lee el día anterior, genera lección, laboratorio y solución HTML, actualiza la portada y valida los enlaces.

Validador manual:

```bash
python .opencode/skills/fabric-day-generator/scripts/check_day.py 4
```

## DP-700

El examen **DP-700: Implementing Data Engineering Solutions Using Microsoft Fabric** se aprueba con 700/1000 y cubre tres dominios de 30–35% cada uno:

1. Implement and manage an analytics solution.
2. Ingest and transform data.
3. Monitor and optimize an analytics solution.

El curso no memoriza la interfaz: construye y opera el proyecto. El examen valida lo aprendido.

## Referencias

- [Microsoft Fabric overview](https://learn.microsoft.com/en-us/fabric/fundamentals/microsoft-fabric-overview)
- [Data Factory overview](https://learn.microsoft.com/en-us/fabric/data-factory/data-factory-overview)
- [DP-700 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-700)

**Documentación verificada:** 2026-11-20. Fabric cambia con frecuencia; revisa release notes y `ms.date` antes de fijar una lección.

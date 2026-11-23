---
description: Genera una sesión completa del Microsoft Fabric Master Course con lección, laboratorio y solución HTML.
agent: build
---

Usa el skill `fabric-day-generator` para generar el día solicitado: $ARGUMENTS

Si no se indica un número, infiere el siguiente día faltante según el plan de `AGENTS.md`. Genera un solo día por invocación, actualiza navegación, `index.html`, `AGENTS.md` y `progress/session-log.md`, y ejecuta `python .opencode/skills/fabric-day-generator/scripts/check_day.py DAY` antes de responder. No hagas commit.

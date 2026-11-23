# RetailOps 360 · Datos sintéticos

Todos los laboratorios usan datos generados. No se usan datos, capturas ni credenciales de empleadores.

## Generar ventas

```bash
python datasets/generate_retailops.py --rows 5000 --date 2026-11-20 --out datasets/out
```

Archivo resultante:

```text
datasets/out/sales_2026-11-20.csv
```

Para el Día 4, súbelo al lakehouse como:

```text
lh_retailops / Files / landing / sales / 2026-11-20 / sales.csv
```

## Esquema

| Columna | Tipo esperado | Notas |
|---|---|---|
| `sale_id` | string | Clave de venta. El generador inyecta duplicados a propósito. |
| `order_id` | string | Agrupa líneas de una misma orden. |
| `store_id` | string | Tienda (`ST01`…`ST12`). |
| `product_id` | string | Producto (`P001`…`P080`). |
| `customer_id` | string | Cliente; algunos nulos controlados. |
| `quantity` | integer | Incluye outliers (999) para calidad de datos. |
| `unit_price` | decimal | Incluye valores negativos ocasionales. |
| `discount_pct` | decimal | Algunos nulos controlados. |
| `sale_ts` | timestamp UTC | Incluye llegadas tardías. |
| `ingest_ts` | timestamp UTC | Momento de ingesta simulado. |
| `source_file` | string | Archivo de origen. |

## Reglas

- Los archivos generados van a `datasets/out/` y no se versionan.
- La semilla es reproducible (`--seed 42` por defecto).
- Los problemas están inyectados a propósito: no los “arregles” en el generador; son parte del curso.

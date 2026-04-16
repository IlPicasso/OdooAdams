# OdooAdams

Repositorio base para trabajar con `oec.sh` manteniendo **solo customizaciones** del proyecto.

## Versión del repositorio
Ver archivo `VERSION` (actual: `0.2.0`).

## Enfoque actual
Este repositorio ya **no** incluye el código completo de Odoo Community como fork o submódulo.

La estrategia es:
- `oec.sh` administra/descarga Odoo Community externamente.
- Este repo mantiene solo:
  - módulos custom,
  - parches,
  - configuración y scripts de soporte.

## Estructura
- `oec/custom-addons/` → módulos propios.
- `oec/patches/` → parches opcionales.
- `oec/config/` → ejemplos de configuración.
- `oec/enterprise-addons/` → reservado para futuro Enterprise.

## Siguiente paso para ti
Con tu setup de `oec.sh` ya listo, apunta `addons_path` a:
1. ruta Community gestionada por `oec.sh`.
2. `oec/custom-addons` de este repositorio.

Referencia de ejemplo: `oec/config/odoo.conf.example`.

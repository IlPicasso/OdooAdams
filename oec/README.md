# Estructura local para `oec.sh`

Este repositorio **no** incluye un fork/submódulo completo de Odoo Community.
La idea es mantener aquí únicamente personalizaciones y soporte de despliegue.

## Carpetas
- `custom-addons/`: módulos propios del proyecto.
- `enterprise-addons/`: espacio reservado para código Enterprise privado (cuando se habilite).
- `patches/`: parches sobre Community/Enterprise si son necesarios.
- `config/`: ejemplos de configuración local.

## Flujo sugerido
1. `oec.sh` descarga/gestiona Community externamente.
2. Este repo versiona solo customizaciones.
3. `addons_path` debe incluir Community externo + `custom-addons` (+ Enterprise futuro).

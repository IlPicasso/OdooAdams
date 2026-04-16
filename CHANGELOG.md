# Changelog

## 0.3.0 - 2026-04-16
- Se creó el módulo `hello_world` para Odoo Community en `oec/custom-addons/hello_world`.
- El módulo incluye modelo `hello.world`, vistas (lista/formulario), menú y permisos base para usuarios internos.
- Se incrementó la versión del repositorio a `0.3.0`.

## 0.2.0 - 2026-04-16
- Se eliminó el submódulo `OdooCommunity` y `.gitmodules` para evitar mantener un fork completo en este repo.
- Se creó una estructura enfocada a `oec.sh` para versionar únicamente personalizaciones (`oec/custom-addons`, `oec/patches`, `oec/config`).
- Se reservó espacio para futura integración Enterprise (`oec/enterprise-addons`).
- Se actualizó documentación principal y de estructura operativa.

## 0.1.0 - 2026-04-16
- Se agregó `OdooCommunity` como submódulo apuntando a `odoo/odoo` rama `18.0`.
- Se documentó la inicialización para entornos con `oec.sh` y la ruta de evolución a Enterprise.

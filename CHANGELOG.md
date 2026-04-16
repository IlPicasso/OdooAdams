# Changelog

## 0.6.0 - 2026-04-16
- Se agregó una copia compatible de `hello_world` en `oec/custom-addons/hello_world` para entornos que aún usan la ruta legacy.
- Ambas rutas (`addons/hello_world` y `oec/custom-addons/hello_world`) quedaron con vistas Odoo 18 (`list`) y `view_mode` `list,form`.
- Se incrementó versión del módulo a `18.0.1.0.2` y versión del repositorio a `0.6.0`.

## 0.5.0 - 2026-04-16
- Se corrigió el tipo de vista XML de `tree` a `list` en `hello_world`, compatible con Odoo 18.
- Se actualizó `view_mode` de la acción a `list,form`.
- Se incrementó versión del módulo a `18.0.1.0.1` y versión del repositorio a `0.5.0`.

## 0.4.0 - 2026-04-16
- Se movió el módulo `hello_world` a `addons/hello_world` para alinearlo con la autodetección estándar de OEC.SH.
- Se actualizaron `README.md`, `oec/README.md` y `oec/config/odoo.conf.example` para usar `addons/` como ruta principal de módulos custom.
- Se incrementó la versión del repositorio a `0.4.0`.

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

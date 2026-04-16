{
    "name": "Hello World",
    "summary": "Módulo base de ejemplo para Odoo Community",
    "version": "18.0.1.0.0",
    "category": "Tools",
    "author": "OdooAdams",
    "license": "LGPL-3",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/hello_world_views.xml",
    ],
    "application": True,
    "installable": True,
}

from odoo import fields, models


class HelloWorld(models.Model):
    _name = "hello.world"
    _description = "Hello World Record"

    name = fields.Char(required=True, default="Hello World")
    active = fields.Boolean(default=True)

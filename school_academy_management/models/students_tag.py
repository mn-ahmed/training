from odoo import models, fields, api

class StudentTag(models.Model):
    _name = "school.tag"
    _description = "Etiquetas para alumnos"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    color = fields.Integer(string="Color")

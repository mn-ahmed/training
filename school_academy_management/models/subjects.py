from odoo import models, fields

class Subjects(models.Model):
    _name = 'school.subjects'
    _description = "School subjects"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    active = fields.Boolean(string="Active", default=True)
    carreer = fields.Many2many("school.carreers", string="Théme")

from odoo import models, fields, api

class Carreers(models.Model):
    _name = 'school.carreers'
    _description = "Théme"
    name = fields.Char(related='Product.name',string="Name", required=True)

    Product = fields.Many2one('product.template' , string="Name", required=True)
    description = fields.Text(string="Description", readonly=False, store=True)
    active = fields.Boolean(string="Active", default=True)
    subjects = fields.Many2many('school.subjects')

    # @api.depends("description")
    # def _compute_description(self):
    #     for record in self:
    #         record.description = "Sin descripción aún para la carrera %s" % record.name

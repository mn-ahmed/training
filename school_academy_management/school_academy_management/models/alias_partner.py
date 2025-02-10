from odoo import models, fields, api

class AliasPartner(models.Model):
    _inherit = 'res.partner'
    
    alias = fields.Char(string="Alias")

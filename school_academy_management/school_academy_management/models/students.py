# -*- coding: utf-8 -*-

from odoo import _, models, fields, api
from odoo.exceptions import ValidationError

class Student(models.Model):
    _name = "school.student"
    _description = "Participants"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order ="name asc"

    partner_id = fields.Many2one('res.partner', string="Name", required=True)
    company_name = fields.Char(related='partner_id.commercial_company_name' ,string="Société")

    name = fields.Char(related='partner_id.name', string="Name", store=True)
    alias = fields.Char(related='partner_id.alias', string="Alias", store=True, readonly=False)
    image = fields.Binary(related='partner_id.image_1920', string="Image", store=True)
    phone = fields.Char(related='partner_id.phone', string="Phone", store=True)
    mobile = fields.Char(related='partner_id.mobile', string="Mobile", store=True)
    street = fields.Char(related='partner_id.street', string="Street", store=True)
    city = fields.Char(related='partner_id.city', string="City", store=True)
    country_id= fields.Many2one(related='partner_id.country_id', string="Country", store=True)
    state_id= fields.Many2one(related='partner_id.state_id', string="State", store=True)
    email = fields.Char(related='partner_id.email', string="Email", store=True)
    zip = fields.Char(related='partner_id.zip', string="ZIP", store=True)
    tuition = fields.Integer(string="Enrollment", readonly=True, copy=False, default=0)
    
    # tuition = fields.Char(string="Enrollment", copy=False, tracking=20, required=True)
    inscription_date = fields.Date(string="Inscription date")
    carreers = fields.Many2one('school.carreers',string="Théme", required=True)
    subjects = fields.Many2many('school.subjects')
    course = fields.Char(string="Course")
    tag = fields.Many2many('school.tag', string="Tags")
    teacher = fields.Many2one('res.partner', string="Formateur")
    # teacher_assistant = fields.Many2one('res.partner', string="Teacher assistant")
    modality = fields.Selection([
                                        ('virtual', 'Virtual'),
                                        ('insitu', 'Presencial'),
                                        ], string="Modality", default="virtual")
    Type_formation = fields.Selection([
        ('inter', 'Inter'),
        ('intra', 'Intra')
    ], string='Type de Formation')
    date_debut = fields.Date(string="Date Début")
    beca = fields.Char(string="Scolarship")
    date_fin = fields.Date(string="Date Fin")
    active = fields.Boolean(string="Active", default=True)

    state = fields.Selection([
        ('draft', 'Not started'),
        ('ongoing', 'Ongoing'),
        ('done', 'Done'),
        ('abandoned', 'Abandoned'),
        ('expelled', 'Expelled'),
    ], string='Status', default='draft', tracking=20)

    def action_ongoing(self):
        self.state = "ongoing"

    def action_done(self):
        self.state = "done"

    def action_draft(self):
        self.state = "draft"

    def action_abandoned(self):
        self.state = "abandoned"

    def action_expelled(self):
        self.state = "expelled"

    @api.model
    def create(self, vals):
        if 'tuition' not in vals or vals['tuition'] == 0:
            last_record = self.search([], order="tuition desc", limit=1)
            vals['tuition'] = last_record.tuition + 1 if last_record else 1
        return super(Student, self).create(vals)
    

    # @api.depends('alias')
    # def _inverse_alias(self):
    #     for student in self:
    #         if student.partner_id:
    #             student.partner_id.alias = student.alias

    # @api.onchange('alias')
    # def _onchange_alias(self):
    #     for record in self:
    #         if record.alias and len(record.alias) > 7:
    #             return {
    #                 'warning': {
    #                     'title': _("Mensaje"),
    #                     'message': _('Se recomienda que el apodo sea corto')
    #                 }
    #             }

    @api.constrains('estimated_graduate_date')
    def _estimated_graduate_date_no_past(self):
        for record in self:
            if record.estimated_graduate_date < fields.Date.today():
                raise ValidationError('The date cannot be earlier than today')

    _sql_constraints = [
        ('check_tuition', 'UNIQUE(tuition)', 'The registration number must be unique')
    ]

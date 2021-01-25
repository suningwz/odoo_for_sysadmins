# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class TherapyTimetable(models.Model):
    _name = 'therapy.timetable'
    _description = 'Timetable'

    hour = fields.Float(string='Hour')
    done = fields.Boolean(string='Done')


class TherapyMedicament(models.Model):
    _name = 'therapy.medicament'
    _description = 'Medicament'

    name = fields.Char(string='Medicament')
    medicament_type = fields.Selection(string='Type',
                                       selection=[
                                           ('pill', 'Pill'),
                                           ('granulated', 'Granulated'),
                                           ('suppository', 'Suppository'),
                                       ])
    quantity = fields.Float(string='Quantity')
    timetable = fields.Many2many(comodel_name='therapy.timetable',
                                 relation='therapy_medicament_timetable',
                                 column1='hour',
                                 column2='done',
                                 string='Timetable')


class Therapy(models.Model):
    _name = 'therapy.therapy'
    _description = 'Therapy for personal use'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    def _default_user_id(self):
        return self.env.user

    name = fields.Many2one(comodel_name='res.users',
                           string='User',
                           default=_default_user_id)
    birthday_date = fields.Date(string='Birthday date')
    genre = fields.Selection(string="Genre",
                             selection=[('female', 'Female'),
                                        ('male', 'Male')])
    image = fields.Image(string='Image')
    medicament_ids = fields.Many2many(comodel_name='therapy.medicament',
                                      realtion='therapy_therapy_medicament',
                                      column1='name',
                                      column2='quantity',
                                      string='Medicaments')

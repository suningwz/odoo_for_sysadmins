# -*- coding: utf-8 -*-
from odoo import _, api, fields, models
from datetime import datetime


class TherapyPrescription(models.Model):
    _name = 'therapy.prescription'
    _description = 'Prescription'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    def _default_user_id(self):
        return self.env.user

    def _therapy_name(self):
        return '%s-%s' % (datetime.today().strftime('%Y-%m-%d'),
                          self.env.user.name)

    # name will be a computed field with a serial number + patient_id
    name = fields.Char(string='Therapy reference', default=_therapy_name)
    patient_id = fields.Many2one(comodel_name='res.users',
                                 string='User',
                                 required=True,
                                 default=_default_user_id)
    start_date = fields.Date(string='Start date')
    end_date = fields.Date(string='End date')
    medicament_ids = fields.One2many(comodel_name='product.medicament',
                                     inverse_name='name',
                                     string='Medicament')

    # saving this method for later
    # @api.model
    # def _check_timetable(self):
    #     # This code is an atrocity, fix it next time
    #     patients = self.env['therapy.reminder'].search([])
    #     for rec in patients:
    #         for med in rec.medicament_ids:
    #             for hours in med.timetable_ids:
    #                 print(hours.hour)

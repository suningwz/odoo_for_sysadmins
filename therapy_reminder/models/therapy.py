# -*- coding: utf-8 -*-
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from datetime import datetime


class TherapyPrescription(models.Model):
    _name = 'therapy.prescription'
    _description = 'Prescription'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    def _default_user_id(self):
        return self.env.user

    #  name will be a computed field with a serial number + patient_id
    @api.onchange('patient_id', 'start_date')
    def _therapy_name(self):
        date_name = ''
        patient_name = ''
        if self.start_date:
            date_name = self.start_date.strftime("%Y-%m-%d")
        else:
            date_name = datetime.now().strftime("%Y-%m-%d")
        if self.patient_id.name:
            patient_name = self.patient_id.name
        else:
            patient_name = self.env.user.name
        self.name = '%s-%s' % (date_name, patient_name)

    name = fields.Char(string='Therapy reference', default=_therapy_name)
    patient_id = fields.Many2one(comodel_name='res.users',
                                 string='User',
                                 required=True,
                                 default=_default_user_id)
    start_date = fields.Date(string='Start date',
                             required=True,
                             default=fields.Date.today)
    end_date = fields.Date(string='End date')
    medicament_ids = fields.One2many(comodel_name='product.medicament',
                                     inverse_name='medicament_id',
                                     string='Medicament')

    # @api.constrains('end_date')
    # def _verify_date_end(self):
    #     self.ensure_one()
    #     if self.start_date:
    #         if self.start_date < self.end_date:
    #             raise ValidationError(
    #                 _("End date must be bigger that start date"))

    # saving this method for later
    # @api.model
    # def _check_timetable(self):
    #     # This code is an atrocity, fix it next time
    #     patients = self.env['therapy.reminder'].search([])
    #     for rec in patients:
    #         for med in rec.medicament_ids:
    #             for hours in med.timetable_ids:
    #                 print(hours.hour)

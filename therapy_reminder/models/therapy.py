# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class TherapyPrescription(models.Model):
    _name = 'therapy.prescription'
    _description = 'Prescription'

    def _default_user_id(self):
        return self.env.user

    # name will be a computed field with a serial number + patient_id
    name = fields.Char(string='Therapy reference')
    patient_id = fields.Many2one(comodel_name='res.users',
                                 string='User',
                                 default=_default_user_id)
    start_date = fields.Date(string='Start date')
    end_date = fields.Date(string='End date')
    medicament_ids = fields.One2many(comodel_name='product.medicament',
                                     inverse_name='medicament_id',
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

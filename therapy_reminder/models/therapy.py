# -*- coding: utf-8 -*-

from odoo import _, api, fields, models
import datetime


class TherapyTimetable(models.Model):
    _name = 'therapy.timetable'
    _description = 'Timetable'

    hour = fields.Float(string='Hour')
    done = fields.Boolean(string='Done')
    medicate_time_ids = fields.Many2many(
        comodel_name='therapy.prescription',
        relation='rel_therapy_prescription_timetable',
        column1='timetable_ids',
        column2='therapy_id',
        string='Medicaments')


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
    medicament_ids = fields.One2many(comodel_name='product.template',
                                     inverse_name='name',
                                     string='Medicament')

    # timetable_ids will be in a table joining patient and product
    # timetable_ids = fields.Many2many(
    #     comodel_name='therapy.timetable',
    #     relation='rel_therapy_prescription_timetable',
    #     column1='therapy_id',
    #     column2='timetable_ids',
    #     string='Timetable')

    # saving this method for later
    # @api.model
    # def _check_timetable(self):
    #     # This code is an atrocity, fix it next time
    #     patients = self.env['therapy.reminder'].search([])
    #     for rec in patients:
    #         for med in rec.medicament_ids:
    #             for hours in med.timetable_ids:
    #                 print(hours.hour)

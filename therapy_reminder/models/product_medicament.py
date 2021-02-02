from odoo import api, fields, models


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


class ProductMedicament(models.Model):
    _name = 'product.medicament'
    _inherits = {'product.template': 'product_tmpl_id'}
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char(string='Name', )

    timetable_ids = fields.Many2many(
        comodel_name='therapy.timetable',
        relation='rel_therapy_prescription_timetable',
        column1='therapy_id',
        column2='timetable_ids',
        string='Timetable')
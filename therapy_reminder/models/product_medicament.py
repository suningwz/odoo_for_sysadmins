from odoo import api, fields, models


class TherapyTimetable(models.Model):
    _name = 'therapy.timetable'
    _description = 'Timetable'

    hour = fields.Float(string='Hour')
    done = fields.Boolean(string='Done')
    therapy_id = fields.Many2one(comodel_name='product.medicament',
                                 string='Therapy')


class ProductMedicament(models.Model):
    _name = 'product.medicament'
    _description = 'Medicament'
    _inherits = {'product.template': 'product_tmpl_id'}
    _inherit = ['mail.thread', 'mail.activity.mixin']

    medicament_id = fields.Char(string='Medicament')
    timetable_ids = fields.One2many(comodel_name='therapy.timetable',
                                    inverse_name='therapy_id',
                                    string='Timetable')

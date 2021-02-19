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

    name = fields.Char(string='Therapy reference',
                       compute='_therapy_name',
                       store=True)
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

    @api.depends('patient_id', 'start_date')
    def _therapy_name(self):
        for rec in self:
            date_name = ''
            if rec.start_date:
                date_name = rec.start_date.strftime("%Y-%m-%d")
            else:
                date_name = datetime.now().strftime("%Y-%m-%d")
            rec.name = '%s-%s' % (date_name, rec.patient_id.name)

    @api.constrains('end_date')
    def _verify_date_end(self):
        self.ensure_one()
        if self.end_date:
            if self.start_date > self.end_date:
                raise ValidationError(
                    _("End date must be bigger that start date"))

    @api.model
    def _check_timetable(self):
        patients = self.env['therapy.prescription'].search([])
        now_time = datetime.now().time()
        now_is = (now_time.hour + 1) + now_time.minute / 60
        administrator = self.env['res.users'].search([('id', '=', '1')])
        for rec in patients:
            for med in rec.medicament_ids:
                for hours in med.timetable_ids:
                    if round(hours.hour, 2) == round(now_is, 2):
                        print("bingo")
                        # notification_ids = [(0, 0, {
                        #     'res_partner_id': rec.id,
                        #     'notification_type': 'inbox'
                        # })]
                        # self.message_post(
                        #     body="It's time to take your medicament: %s" %
                        #     med.name,
                        #     message_type="notification",
                        #     subtype="mail.mt_comment",
                        #     author_id=administrator,
                        #     notification_ids=notification_ids)

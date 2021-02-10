from odoo import api, fields, models
import os


class ModuleName(models.Model):
    _inherit = 'res.partner'

    check_domain = fields.Boolean(string='Check domain?')
    domain_status = fields.Boolean(string='Domain status', default=True)

    def _check_domain_health(self):
        partners = self.env['res.partner'].search([('is_company', '=', True)])
        for rec in partners:
            if rec.check_domain:
                comp = self.env['res.company'].search([('id', '=', 1)])[0]
                if rec.website:
                    not_response = os.system('ping -c 1 ' +
                                             rec.website.split("//")[1])
                    if not_response:
                        if rec.domain_status:
                            rec.domain_status = False
                            template_id = self.env.ref(
                                'domain_health_status.domain_health_status_alert_email_template'
                            ).id

                            self.env['mail.template'].browse(
                                template_id).send_mail(rec.id,
                                                       force_send=True,
                                                       raise_exception=True,
                                                       email_values={
                                                           'email_from':
                                                           comp.email,
                                                       })

                    if not not_response and not rec.domain_status:
                        rec.domain_status = True
                        template_id = self.env.ref(
                            'domain_health_status.domain_health_status_notification_email_template'
                        ).id

                        self.env['mail.template'].browse(
                            template_id).send_mail(rec.id,
                                                   force_send=True,
                                                   raise_exception=True,
                                                   email_values={
                                                       'email_from':
                                                       comp.email,
                                                   })

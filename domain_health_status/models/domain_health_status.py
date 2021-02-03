from odoo import api, fields, models
import os


class ModuleName(models.Model):
    _inherit = 'res.partner'

    check_domain = fields.Boolean(string='Check domain?')
    domain_status = fields.Boolean(string='Domain status', readonly=True)

    def _check_domain_health(self):
        partners = self.env['res.partner'].search([('is_company', '=', True)])
        for rec in partners:
            if rec.check_domain:
                if rec.website:
                    not_response = os.system('ping -c 1 ' +
                                             rec.website.split("//")[1])
                    if not_response:
                        print("Mal asunto")

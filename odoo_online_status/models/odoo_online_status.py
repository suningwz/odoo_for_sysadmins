from odoo import models, fields, api
from datetime import datetime
import requests


class OdooOnlineStatus(models.Model):
    _name = 'odoo_online_status'
    _description = 'odoo_online_status'

    service_name = fields.Char(required=True)
    url = fields.Char(required=True)
    service_status = fields.Boolean(default=False, readonly=True)
    last_update = fields.DateTime(readonly=True)

    @api.model
    def run(self):
        """ This method will be called from a cronjob """
        services = self.env['odoo_online_status'].search()
        for service in services:
            if isinstance(service.service_name, str) and isinstance(service.url, str):
                status = requests.get(service.url)
                if status.ok:
                    if not service.service_status:
                        service.service_status = True
                else:
                    service.service_status = False
                service.last_update = datetime.now()

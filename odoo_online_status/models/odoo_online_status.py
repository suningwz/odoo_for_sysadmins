-*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
import requests


class odoo_online_status(models.Model):
    _name = 'odoo_online_status'
    _description = 'odoo_online_status'

    service_name = fields.Char(required=True)
    url = fields.Char(required=True)
    service_status = fields.Boolean(default=False)
    last_update = fields.DateTime()

    @api.model
    def run(self):
        """ This method will be called from a cronjob """
        services = self.env['odoo_online_status'].search()
        for service in services:
            if isinstance(service.service_name, basestring) and isinstance(service.url, basestring):
                status = requests.get(service.url)
                if status == 200:
                    if not service.service_status:
                        service.service_status = True
                else:
                    service.service_status = False
                service.last_update = datetime.now()

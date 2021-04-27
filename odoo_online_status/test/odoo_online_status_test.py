from odoo.tests import TransactionCase
from datetime import datetime


class TestOdooOnlineStatus(TransactionCase):

    def setUp(self):
        record = self.env['odoo_online_status'].create(
            {
                'service_name': 'healthchecks.io',
                'url': 'https://hc-ping.com/4148b61d-430c-422c-9f1b-3d883c76f1f9',
            }
        )
        record.run()
        data_now = datetime.now()

    def test_00(self):
        self.assertEqual(
            self.record.service_status,
            self.data_now
        )

        self.assertTrue(
            self.record.last_update
        )

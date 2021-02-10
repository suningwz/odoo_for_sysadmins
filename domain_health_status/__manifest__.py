# -*- coding: utf-8 -*-
{
    'name':
    "domain_health_status",
    'summary':
    """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description':
    """
        Long description of module's purpose
    """,
    'author':
    "My Company",
    'website':
    "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category':
    'Uncategorized',
    'version':
    '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mail'],

    # external dependency jingtrang

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/mail_alert_cron.xml',
        'data/mail_alert.xml',
        'data/mail_notification.xml',
        'views/domain_health_status.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

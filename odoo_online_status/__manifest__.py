# -*- coding: utf-8 -*-
{
    'name': "odoo_online_status",

    'summary': """
        Module to send notifications to https://healthchecks.io/ or similar services""",

    'author': "raistdev",
    'website': "https://raist.dev",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '13.0.1.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/odoo_online_status_cron.xml',
        'views/odoo_online_status_views.xml',
    ],
}

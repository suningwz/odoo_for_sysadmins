# -*- coding: utf-8 -*-
{
    'name': "data_pwned",

    'summary': """
        Check if data or mobile phone numbers are in a leak through https://haveibeenpwned.com/""",

    'author': "raistdev",
    'website': "https://raist.dev",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '13.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/data_pwned_views.xml',
    ],
}

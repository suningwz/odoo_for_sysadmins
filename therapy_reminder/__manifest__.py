{
    'name':
    'Therapy reminder',
    'version':
    '13.0.1.1.0',
    'summary':
    '''This app allows to set the personal therapy
     and get notifications to take it''',
    'category':
    '',
    'author':
    'Raistdev',
    'maintainer':
    'Raistdev',
    'website':
    'https://raist.dev',
    'license':
    'AGPL-3',
    'contributors': [
        'juanma raistdev',
    ],
    'depends': [
        'base',
        'purchase',
        'purchase_product_matrix',
        'mail',
    ],
    'data': [
        'security/therapy_security.xml',
        'security/ir.model.access.csv',
        'views/prescription.xml',
        'views/medicament.xml',
        'views/timetable.xml',
        'data/therapy_data.xml',
    ],
    'installable':
    True,
    'auto_install':
    False,
    'application':
    True,
}

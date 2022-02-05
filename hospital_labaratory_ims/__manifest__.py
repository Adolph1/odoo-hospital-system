# -*- coding: utf-8 -*-

{
    'name': 'Laboratory Information Management System',
    'version': '13.0.1.1.0',
    'category': 'Generic Modules/Hospital management systems',
    'summary': """
        For Laboratory Tests
    """,
    'description': """Odoo13 Lab tests, OPD""",
    'author': 'Adotech Company Limited',
    'company': 'Adotech Company Limited',
    'maintainer': 'Adotech Company Limited',
    'website': 'https://www.adotech.co.tz',
    'depends': [],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/lab_tests.xml',
        'views/requests.xml',
        'views/main_menu.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'AGPL-3',
}
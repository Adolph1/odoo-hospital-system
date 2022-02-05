# -*- coding: utf-8 -*-

{
    'name': 'Hospital Management System',
    'version': '13.0.1.1.0',
    'category': 'Generic Modules/Hospital magement systems',
    'summary': """
        For Hospitals and Farmacy
    """,
    'description': """Odoo13 Patients management, Lab tests, OPD""",
    'author': 'Adotech Company Limited',
    'company': 'Adotech Company Limited',
    'maintainer': 'Adotech Company Limited',
    'website': 'https://www.adotech.co.tz',
    'depends': ['hr','account'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/patient_billing.xml',
        'views/new_bill.xml',
        'views/patient_file.xml',
        'views/patient_billing_line.xml',
        'views/new_patient.xml',
        'views/view_patient.xml',
        'views/patient.xml',
        'data/sequence.xml',
        'views/clinic.xml',
        'views/department.xml',
        'views/service_line.xml',
        'views/patient_file_laboratory.xml',
        'reports/patient_billing.xml',
        'reports/report.xml',
        'wizard/hospital_appointments_invoice_wizard.xml',
        'views/appointment.xml',
        'views/physician.xml',
        'views/main_menu.xml',



    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'AGPL-3',
}
{
    'name': 'Practice',
    'version': '15.0.1.2.1',
    'category': 'Education',
    'author': 'Candidroot',
    'sequence': '-100',
    'website': "www.www.www",
    'summary': 'Record Student Details',
    "description": """Practice""",
    'depends': ['mail'],
    'application': True,
    'installable': True,
    'data': [
        '/home/erp/odoo/custom/practices_module/security/ir.model.access.csv',
        '/home/erp/odoo/custom/practices_module/views/patient_views.xml',
        '/home/erp/odoo/custom/practices_module/views/appointment_views.xml',
    ],
    'demo': [
        ],

}
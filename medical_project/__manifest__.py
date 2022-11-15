# -*- coding: utf-8 -*-

{
    'name': 'Medical Project',
    'version': '15.0.1.2.1',
    'category': 'sales and Invoicing',
    'author': 'Candidroot',
    'sequence': '10',
    'website': "www.www.www",
    'summary': 'Medical Project will help in the management',
    "description": """Medical Project will help in the management""",
    'depends': ['payment','base'],
    'application': True,
    'installable': True,
    'data': [
        '/home/erp/odoo/custom/medical_project/security/hospital_security.xml',
        '/home/erp/odoo/custom/medical_project/security/ir.model.access.csv',
        '/home/erp/odoo/custom/medical_project/wizard/create_opd_view.xml',
        '/home/erp/odoo/custom/medical_project/views/doctor_view.xml',
        '/home/erp/odoo/custom/medical_project/views/opd_view.xml',
        '/home/erp/odoo/custom/medical_project/views/patient_view.xml',
        '/home/erp/odoo/custom/medical_project/views/department_view.xml',
        '/home/erp/odoo/custom/medical_project/views/medicine_view.xml',
        '/home/erp/odoo/custom/medical_project/views/medicine_pharmacy_view.xml',
        '/home/erp/odoo/custom/medical_project/report/opd_report.xml',


    ],
    'demo': [
        '/home/erp/odoo/custom/medical_project/demo/patient_demo.xml',
        '/home/erp/odoo/custom/medical_project/demo/department_demo.xml',
        '/home/erp/odoo/custom/medical_project/demo/doctor_demo.xml',
    ],

}
# -*- coding: utf-8 -*-
{
    'name': "Educational academy management",

    'summary': "Create and manage students for your academy",

    'description': """
Create and manage students for your academy.
    """,

    'author': "Javier Diez",
    'website': "https://javierdiez.netlify.app/",
    'license': 'AGPL-3',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Education',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/school_student_views.xml',
        'views/students_tag_views.xml',
        'views/carreers_views.xml',
        'views/subjects_views.xml',
        'views/alias_partner_views.xml',
        'views/school_student_menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "images": ['static/images/banner.png', 'static/description/icon.png'],
    'installable': True,
    'application': True,  # Esto indica que tu módulo es una aplicación.
    'auto_install': False,
}


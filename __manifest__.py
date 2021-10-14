# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Gym ERP',
    'version': '1.0',
    'author': 'Vatsal Thore',
    'category': 'Gym',
    'summary': 'Gym member info',
    'description': "Gym",
    'website': 'https://www.odoo.com',
    'depends': [
        'base','stock','sale'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/gym_schedule_views.xml',
        'views/transfer_info_views.xml',
        'wizard/update_phone_views.xml',
        'wizard/update_order_line_views.xml',
        'views/button_wizard_views.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

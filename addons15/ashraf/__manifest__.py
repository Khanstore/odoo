# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'product custom attribute',
    'version': '1.1',
    'category': 'customisation',
    'depends' : ['base','product'],
    'description': """
Module for custom attribute for product and contact.
===============================================

In Odoo, analytic accounts are linked to general accounts but are treated
totally independently. So, you can enter various different analytic operations
that have no counterpart in the general financial accounts.
    """,
    'data': [
        # 'security/analytic_security.xml',
        'security/ir.model.access.csv',
        'views/product_custom_attribute.xml',
        'views/partner_custom_attribute.xml',
    ],
    'demo': [
        # 'data/analytic_demo.xml',
        # 'data/analytic_account_demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

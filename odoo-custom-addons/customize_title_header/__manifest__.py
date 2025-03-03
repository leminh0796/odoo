# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Customize Title Header',
    'summary': """
        Custom shortcut title, Odoo Favicon Title, Odoo Title and Favicon, Odoo Backend Title Favicon, Odoo Web Favicon Title,
        Odoo Web Title, Odoo Customize Title Header, Odoo Browser Header, Odoo Header Favicon, Odoo Header Title, Web Window Title,
        Web Backend Title, Odoo Backend Title, Web Responsive Title, Remove Odoo Favicon Header, Remove Odoo Title, Hide Odoo Title,
        Remove Favicon Header, Web Odoo Shortcut Favicon Shortcut Odoo Shortcut, Odoo Backend Favicon Odoo Backend Title Odoo Browser,
        Customization Favicon Title Customization, Configutable Favicon Title Configutable, Configution Favicon Title Configution,
        Web Shortcut Customization Shortcut Editable Favicon Editable Shortcut Favicon Setup Title Header Title Browser Title Navigator
    """,
    'description': "Choose your own Title to display on the browser header.",
    'author': 'Innoway',
    'website': 'https://innoway-solutions.com',
    'license': 'LGPL-3',
    'category': 'Uncategorized',
    'version': '0.1',
    'installable': True,
    'application': True,
    'depends': [
        'web'
    ],
    'data': [

    ],
    'assets': {
        'web.assets_backend': [
            'customize_title_header/static/src/js/favicon.js',
        ],
    },
    'demo': [

    ],
    'qweb': [

    ],
}

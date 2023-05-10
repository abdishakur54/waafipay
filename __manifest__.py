# -*- coding: utf-8 -*-
{
    'name': "Waafipay",

    'summary': """WaafiPay Payment Gateway allows businesses and eCommerce to accept credit cards, mobile money and other payment methods securely and with easy integration.""",

    'description': """Waafipay Payment Acquirer""",

    'author': "Safarifone Inc",
    'website': "https://www.waafipay.net",
 

    'category': 'Accounting/Payment Acquirers',
    'version': '16.0.1.2',
    'depends': ['payment'],

    # always loaded
    'data': [
        'views/views.xml',
        'views/methode.xml',
        'views/assets.xml',
        'views/templates.xml',
        'demo/demo.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
    'price': '0.00',
    'currency': 'USD',
    'installable': True,
    'images': ['static/description/LOGO MiIG- icon.png'],

}

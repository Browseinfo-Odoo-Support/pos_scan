# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    "name" : "POS Mobile Barcode Scanner | POS Mobile QRCode Scanner",
    "version" : "14.0.0.2",
    "category" : "",
    'summary': 'POS Mobile Barcode Scanner | POS Mobile QRCode Scanner',
    "description": """
    
   Description of the module. 
    
    """,
    "author": "BrowseInfo",
    "website" : "www.browseinfo.in",
    "price": 000,
    "currency": 'EUR',
    "depends" : ['base', 'point_of_sale','bi_qr_generator'],
    "data": [
        'views/pos_assets.xml',
        'views/pos_config_view.xml',
    ],
    'qweb': ['static/src/xml/pos.xml'
    ],
    "auto_install": False,
    "installable": True,
    "live_test_url":'youtube link',
    "images":["static/description/Banner.png"],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

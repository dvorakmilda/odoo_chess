{
    'name': 'O4 CHESS',
    'version': '14.0.1.1.0',
    "sequence": 1,
    'category': 'Games',
    'summary': 'Generate chess board from char FEN',
    'website': 'https://www.optimal4.cz',
    'author': 'Optimal4',
    'company': 'Optimal4',
    'description': """
Odoo chess board generator
=================
- Picture generator from char field wiht FEN text to picture.

For more information about service and revenew contact info@cribis.cz or visit https://www.cribis.cz

For more information about plugin contact info@optimal4.cz or visit https://www.optimal4.cz

    """,
    'images': [],
    'depends': ['website_slides',

    ],
    'demo': [
    ],

    'data': [ './views/slide_slide_views.xml',
    ],

    'external_dependencies': {'python': ['python-chess','Pillow', 'CairoSVG',]},
    'installable': True,
    'auto_install': False,
    'application': False,
    'licence': ''
}

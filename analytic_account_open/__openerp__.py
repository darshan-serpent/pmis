# -*- coding: utf-8 -*-
# © 2017 Eficent - Jordi Ballester Alomar
# © 2017 Serpent Consulting Services Pvt. Ltd. - Sudhir Arya
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Analytic Account Open',
    'version': '9.0.1.0.0',
    'summary': 'Opens a single project/analytic account, or the whole WBS',
    'author':   'Eficent, '
                'Project Expert Team',
    'contributors': [
        'Jordi Ballester <jordi.ballester@eficent.com>',
        'Matjaž Mozetič <m.mozetic@matmoz.si>',
    ],
    'website': 'http://project.expert',
    'category': 'Project Management',
    'license': 'AGPL-3',
    'depends': ['account', 'analytic'],
    'data': [
        'wizards/analytic_account_open_view.xml',
    ],
    'installable': True,
}

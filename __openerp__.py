# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2015 - Oy Tawasta Technologies Ltd. (http://www.tawasta.fi)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Account Invoice Internal Invoicing',
    'category': 'Account',
    'version': '0.1',
    'author': 'Oy Tawasta Technologies Ltd.',
    'website': 'http://www.tawasta.fi',
    'depends': ['account'],
    'description': '''
Account Invoice Internal Invoicing
--------------------------

Allows different income and expense accounts to be used when
invoicing within the company group.

Features
--------

* Adds internal income and expense accounts for products
* Adds a possibility to create an internal invoice
''',
    'data': [
        'view/account_invoice_form.xml',
    ],
}

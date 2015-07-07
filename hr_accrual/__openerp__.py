# -*- coding: utf-8 -*-
# Python source code encoding : https://www.python.org/dev/peps/pep-0263/
##############################################################################
#
#    OpenERP, Odoo Source Management Solution
#    Copyright (C) 2013 Michael Telahun Makonnen <mmakonnen@gmail.com>.
#                       Endika Iglesias <endika2@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Accrual',
    'version': '1.0',
    'category': 'Generic Modules/Human Resources',
    'author': "Michael Telahun Makonnen <mmakonnen@gmail.com>, "
              "Endika Iglesias <endika2@gmail.com>, "
              "Odoo Community Association (OCA)",
    'website': 'http://miketelahun.wordpress.com',
    'license': 'AGPL-3',
    'depends': [
        'hr',
        'hr_holidays',
        'hr_holidays_extension',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_accrual_view.xml',
    ],
    'installable': False,
}

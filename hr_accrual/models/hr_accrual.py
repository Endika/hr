# -*- coding: utf-8 -*-
# Python source code encoding : https://www.python.org/dev/peps/pep-0263/
##############################################################################
#
#    OpenERP, Odoo Source Management Solution
#    Copyright (C) 2013 Michael Telahun Makonnen <mmakonnen@gmail.com>
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

import time

from openerp.tools import DEFAULT_SERVER_DATE_FORMAT as OE_DATEFORMAT
from openerp import models, fields


class hr_accrual(models.Model):
    _name = 'hr.accrual'
    _description = 'Accrual'

    name = fields.Char(string='Name', size=128, required=True)
    holiday_status_id = fields.Many2one(
        comodel_name='hr.holidays.status', string='Leave')
    line_ids = fields.One2many(
        comodel_name='hr.accrual.line', inverse_name='accrual_id',
        string='Accrual Lines', readonly=True)

    def get_balance(self, ids, employee_id, date=None):
        if date is None:
            date = time.strftime(OE_DATEFORMAT)
        res = 0.0
        result = self.env['hr_accrual_line'].search(
            [('accrual_id', 'in', tuple(ids)),
             ('employee_id', '=', employee_id),
             ('date', '<=', date)])
        for hr_line in result:
            res += hr_line.amount
        return res


class hr_accrual_line(models.Model):
    _name = 'hr.accrual.line'
    _description = 'Accrual Line'

    date = fields.Date(
        string='Date', required=True, default=time.strftime(OE_DATEFORMAT))
    accrual_id = fields.Many2one(
        comodel_name='hr.accrual', string='Accrual', required=True)
    employee_id = fields.Many2one(
        comodel_name='hr.employee', string='Employee', required=True)
    amount = fields.Float(string='Amount', required=True)

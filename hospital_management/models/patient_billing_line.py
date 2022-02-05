# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import date,datetime
from dateutil.relativedelta import relativedelta


class PatientBillingLine(models.Model):
    _name = 'patient.billing.line'
    _description = 'Patient Billing Items'

    name = fields.Many2one('patient.billing', 'Billing')
    department_id = fields.Many2one('hospital.department', 'Department')
    quantity = fields.Float('Quantity', default=1)
    item_id = fields.Many2one('product.product', 'Services')
    price = fields.Float(related='item_id.lst_price', string='Price')
    total = fields.Float(compute='_compute_total', string='Total', help="Total", store=True)

    tax_line_id = fields.Many2one('account.tax', string='Tax', ondelete='restrict', store=True,
                                   help="Indicates that this journal item is a tax line")

    @api.depends('quantity', 'price','tax_line_id')
    def _compute_total(self):
        for line in self:
            line.total = float(line.quantity) * line.price

    @api.onchange('department_id')
    def _onchange_name(self):
        departments = []
        for department in self.department_id:
            departments.append(department.id)
        return {'domain': {'service_line_ids': [('department_id', 'in', departments)]}}
















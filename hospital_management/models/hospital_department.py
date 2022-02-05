# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import date,datetime
from dateutil.relativedelta import relativedelta

class HospitalDepartment(models.Model):
    _name = 'hospital.department'
    _description = 'Hospital Department'

    name = fields.Char('Name')
    bill_ref_no = fields.Char('Name')
    manager = fields.Char('Manager')
    service_line_ids = fields.One2many('hospital.department.service.line', 'name', 'Service')



class HospitalDepartmentServiceLine(models.Model):
    _name = 'hospital.department.service.line'
    _description = 'Hospital Department Services'

    @api.onchange('name')
    def _onchange_name(self):
        departments = []
        for department in self.name:
            departments.append(department.id)
        return {'domain': {'service_line_ids': [('name', 'in', departments)]}}

    name = fields.Many2one('hospital.department', 'Department')
    item_id = fields.Many2one('product.product', string='Service')
    price = fields.Float(related='item_id.lst_price', string='Price')
    service_code = fields.Char('Code')


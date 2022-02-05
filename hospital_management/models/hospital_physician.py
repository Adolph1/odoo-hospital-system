# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class hospital_physician(models.Model):
    _name="hospital.physician"

    name = fields.Many2one('res.partner','Physician', required=True)
    clinic_id = fields.Many2one('hospital.clinic',string='Health Center')
    code = fields.Char('Code')
    info = fields.Text('Extra Info')

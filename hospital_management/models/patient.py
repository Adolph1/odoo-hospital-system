# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import date,datetime
from dateutil.relativedelta import relativedelta
import re

class Patient(models.Model):
    _name = 'patient'
    _description = 'Patient'
    _rec_name = 'full_name'

    @api.depends('first_name', 'last_name')
    def _full_name(self):
        for name in self:
            name.full_name = name.first_name + ' ' + name.last_name


    @api.depends('date_of_birth')
    def onchange_age(self):
        for rec in self:
            if rec.date_of_birth:
                d1 = rec.date_of_birth
                d2 = datetime.today().date()
                rd = relativedelta(d2, d1)
                rec.age = str(rd.years) + "y" +" "+ str(rd.months) + "m" +" "+ str(rd.days) + "d"
            else:
                rec.age = "No Date Of Birth!!"

    clinic_id = fields.Many2one('hospital.clinic', string="Clinic", required=True)
    first_name = fields.Char(string='First Name', required=True)
    middle_name = fields.Char(string='Middle Name')
    last_name = fields.Char(string='Last Name', required=True)
    full_name = fields.Char(string='Full Name', compute='_full_name')
    date_of_birth = fields.Date(string="Date of Birth")
    gender = fields.Selection([('m', 'Male'), ('f', 'Female')], string="Gender")
    age = fields.Char(compute=onchange_age, string="Patient Age", store=True)
    patient_contact = fields.Char(string="Patient's contact", required=True)
    next_of_kin = fields.Char(string="Next of kin")
    photo = fields.Binary(string="Picture")
    marital_status = fields.Selection(
        [('s', 'Single'), ('m', 'Married'), ('w', 'Widowed'), ('d', 'Divorced'), ('x', 'Separated')],
        string='Marital Status', required=True)
    area = fields.Char(string='Area', required=True)
    occupation = fields.Char(string='Occupation')
    residential_address = fields.Char(string='Residential', required=True)
    patient_medical_number = fields.Char(string='Medical Record #', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))
    files_count = fields.Integer(string='Files', compute='get_files_count')
    bills_count = fields.Integer(string='Bills', compute='get_bills_count')


    @api.model
    def create(self, vals):
        if vals.get('patient_medical_number', _('New')) == _('New'):
            vals['patient_medical_number'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')
        result = super(Patient, self).create(vals)
        return result

    def get_files_count(self):
        count = self.env['patient.file'].search_count([('patient_id', '=', self.id)])
        self.files_count = count

    def get_bills_count(self):
        count = self.env['patient.billing'].search_count([('patient_id', '=', self.id)])
        self.bills_count = count

    def open_patient_files(self):
        return {
            'name': _('Patient Visits'),
            'domain': [('patient_id', '=', self.id)],
            'view_type': 'form',
            'res_model': 'patient.file',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def open_patient_bills(self):
        return {
            'name': _('Patient Bills'),
            'domain': [('patient_id', '=', self.id)],
            'view_type': 'form',
            'res_model': 'patient.billing',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }



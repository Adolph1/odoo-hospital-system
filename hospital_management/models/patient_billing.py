# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import date,datetime
from dateutil.relativedelta import relativedelta


class PatientBilling(models.Model):
    _name = 'patient.billing'
    _description = 'Patient Billing'
    _rec_name = 'bill_ref_no'

    patient_id = fields.Many2one('patient', string="Patient", required=True)
    billing_date = fields.Date(string="Billing Date", required=True)
    bill_ref_no = fields.Char(string='Billing #', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))
    billing_line_ids = fields.One2many('patient.billing.line','name','Service')
    # billing_line_ids_new = fields.One2many('hospital.department.service.line','name','Services')
    journal_id = fields.Many2one('account.journal', 'Billing Journal', help="Journal")
    # department_id = fields.Many2one('hospital.department', 'Department', help="Department")
    mr_number = fields.Char(string='MR Number', required=True)
    patient_name = fields.Char(string='Patient Name', compute='_onchange_mr_number',store=False)
    gender = fields.Char(string='Gender', compute='_onchange_mr_number',store=False)
    age = fields.Char(string='Age', compute='_onchange_mr_number',store=False)
    contact = fields.Char(string='Patient Contact', compute='_onchange_mr_number',store=False)
    date_of_birth = fields.Char(string='Date of birth', compute='_onchange_mr_number',store=False)
    total_amount = fields.Float('Total Amount', compute='_compute_total')
    pt_id = fields.Integer(compute='_onchange_mr_number', string="Patient")

    @api.onchange('mr_number')
    def _onchange_mr_number(self):
        if self.mr_number:
            patient_model = self.env['patient'].search([('patient_medical_number', '=', self.mr_number)])
            self.patient_name = patient_model.first_name + ' ' + patient_model.last_name
            self.patient_id = patient_model.id
            self.pt_id = patient_model.id
            self.gender = patient_model.gender
            self.contact = patient_model.patient_contact
            self.age = patient_model.age
            self.date_of_birth = patient_model.date_of_birth

        else:
            self.patient_name = ''

    payment_type = fields.Selection([
        ('cash', 'Cash'),
        ('credit', 'Credit'),
        ('out-patient', 'Off Patient'),
    ], string='Payment Types', index=True, default='cash',
        help="Defines the payment type.")

    @api.model
    def create(self, vals):
        if vals.get('bill_ref_no', _('New')) == _('New'):
            vals['bill_ref_no'] = self.env['ir.sequence'].next_by_code('hospital.patient.billing.sequence') or _(
                'New')
        result = super(PatientBilling, self).create(vals)
        if result:

            patient_file = self.env['patient.file']
            patient_file.create({
                'patient_id': vals['patient_id'],
                'file_ref_no': self.env['ir.sequence'].next_by_code('hospital.patient.file.sequence') or _('New'),
                'opening_date': vals['billing_date'],

            })
        return result

    @api.depends('billing_line_ids.total')
    def _compute_total(self):
        for record in self:
            record.total_amount = sum(record.billing_line_ids.mapped('total'))

    def print_report(self):
        return self.env.ref('hospital_management.report_patient_billing_details').report_action(self)

    # @api.depends('department_id')
    # def get_services(self):
    #     services = self.env['hospital.department.service.line'].search([('id', '=', self.department_id.id)])
    #     if services:
    #         self.billing_line_ids_new = services







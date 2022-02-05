# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import date,datetime
from dateutil.relativedelta import relativedelta


class PatientFile(models.Model):
    _name = 'patient.file'
    _description = 'Patient File'
    _rec_name = 'file_ref_no'

    patient_id = fields.Many2one('patient', string="Patient", required=True, readonly=True)
    file_ref_no = fields.Char(string='File #', readonly=True)
    mr_number = fields.Char(related='patient_id.patient_medical_number', string='Mr Number', readonly=True)
    opening_date = fields.Date(string='Opening Date')
    laboratory_lines = fields.One2many('patient.file.laboratory', 'name', 'Services')
    age = fields.Char(related='patient_id.age', store=False)
    contact = fields.Char(related='patient_id.patient_contact', store=False)
    state = fields.Selection([('opened', 'Opened'), ('virtual', 'Virtual'), ('doctor', 'Doctor')], readonly=True, default='opened')
    height = fields.Float('Height')
    weight = fields.Float('Weight')
    bmi = fields.Float('BMI')
    triage_time = fields.Char('Triage Time')
    bp_systolic = fields.Float('BP Systolic')
    bp_diastolic = fields.Float('BP Diastolic')
    pulse = fields.Float('Pulse')
    raspiratory_rate = fields.Float('Raspiratory Rate')
    spo = fields.Float('SPO')
    temp = fields.Float('Temperature')
    ambulation = fields.Float('Ambulation')
    infection_disease = fields.Char('Infection Diseases')
    consultant_name = fields.Many2one('hospital.physician', string="Consultant")

    # Doctor Form
    chief_complaint = fields.Text(string='Chief Complaint')
    present_illness_history = fields.Text(string='History of present illness')
    medication_allergies = fields.Text(string='Medications / Allergies')
    physical_examination = fields.Text(string='Physical Examination')
    provisional_diagnosis = fields.Text(string='Provisional Diagnosis')
    investigations = fields.Text(string='Investigations')
    final_diagnosis = fields.Text(string='Final Diagnosis')
    treatment_plan = fields.Text(string='Treatment Plans')

    def action_confirm(self):
        for rec in self:
            rec.state = 'virtual'


class PatientFileLaboratory(models.Model):
    _name = 'patient.file.laboratory'
    _description = 'Patient File Laboratory'

    name = fields.Many2one('patient.file', string="Patient", required=True)
    quantity = fields.Float('Quantity', default=1)
    item_id = fields.Many2one('product.product', 'Services')
    price = fields.Float(related='item_id.lst_price', string='Price')
    total = fields.Float(compute='_compute_total', string='Total', help="Total", store=True)

    @api.depends('quantity', 'price')
    def _compute_total(self):
        for line in self:
            line.total = float(line.quantity) * line.price

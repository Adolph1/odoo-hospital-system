# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
# from datetime import datetime, date
from datetime import datetime, timedelta
from odoo.exceptions import UserError


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = 'mail.thread'


    name = fields.Char(string="Appointment ID", readonly=True, copy=True)
    is_invoiced = fields.Boolean(copy=False, default=False)
    clinic_id = fields.Many2one('hospital.clinic', string="Health Center")
    patient_status = fields.Selection([
        ('ambulatory', 'Ambulatory'),
        ('outpatient', 'Outpatient'),
        ('inpatient', 'Inpatient'),
    ], 'Patient status', sort=False, default='outpatient')
    patient_id = fields.Many2one('patient', 'Patient', required=True)
    urgency_level = fields.Selection([
        ('a', 'Normal'),
        ('b', 'Urgent'),
        ('c', 'MedicalEmergency'),
    ], 'Urgency Level', sort=False, default="b")
    appointment_date = fields.Datetime('Appointment Date', required=True, default=fields.Datetime.now)
    appointment_end = fields.Datetime('Appointment End', required=True)
    doctor_id = fields.Many2one('hospital.physician', string='Doctor', required=True)
    no_invoice = fields.Boolean(string='Invoice exempt', default=True)
    validity_status = fields.Selection([
        ('invoice', 'Invoice'),
        ('tobe', 'To be Invoiced'),
    ], 'Status', sort=False, readonly=True, default='tobe')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or 'APT'
        msg_body = 'Appointment created'
        for msg in self:
            msg.message_post(body=msg_body)
        result = super(HospitalAppointment, self).create(vals)
        return result


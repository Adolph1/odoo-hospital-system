# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import date,datetime
from dateutil.relativedelta import relativedelta

class HospitalClinic(models.Model):
    _name = 'hospital.clinic'
    _description = 'Hospital Clinic'

    name = fields.Char('Name')
    location = fields.Char('Location')

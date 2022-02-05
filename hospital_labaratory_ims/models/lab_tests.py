# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import date,datetime
from dateutil.relativedelta import relativedelta
import re

class LaboratoryTest(models.Model):
    _name = 'laboratory.test'
    _description = 'Laboratory Test'

    name = fields.Char('Test Name')
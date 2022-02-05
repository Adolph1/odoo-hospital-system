# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import date,datetime
from dateutil.relativedelta import relativedelta
import re

class LaboratoryRequest(models.Model):
    _name = 'laboratory.request'
    _description = 'Laboratory Requests'

    name = fields.Char('Request')

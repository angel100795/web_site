# -*- coding: utf-8 -*-

from odoo import models, fields, api



class Teachers(models.Model):
    _name = 'college.teachers'

    name = fields.Char()



from odoo import models, fields


class MySchoolInscription(models.Model):
    _name = 'myschool.inscription'

    createdAt = fields.Char(string='Date', required=True)
    createdBy = fields.Char(string='Par', required=True)
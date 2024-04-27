

from odoo import models, fields


class MySchoolRapport(models.Model):
    _name = 'myschool.rapport'

    createdAt = fields.Char(string='Date', required=True)
    createdBy = fields.Char(string='Par', required=True)
    updateAt = fields.Char(string='DateMiseaJour', required=True)
    updateBy = fields.Char(string='MiseaJourPar', required=True)
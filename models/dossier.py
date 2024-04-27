from odoo import models, fields


class MySchoolDossier(models.Model):
    _name = 'myschool.dossier'

    createdAt = fields.Char(string='Date', required=True)
    createdBy = fields.Char(string='Par', required=True)
    updateAt = fields.Char(string='DateMiseaJour', required=True)
    updateBy = fields.Char(string='MiseaJourPar', required=True)
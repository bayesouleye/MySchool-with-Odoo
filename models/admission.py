

from odoo import models, fields

class MySchoolAdmission(models.Model):
    _name = 'myschool.admission'

    annee = fields.Char(string='Annee', required=True)

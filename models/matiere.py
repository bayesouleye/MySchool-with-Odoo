# matiere.py

from odoo import models, fields


class MySchoolMatiere(models.Model):
    _name = 'myschool.matiere'

    name = fields.Char(string='Nom', required=True)
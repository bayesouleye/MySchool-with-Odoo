
from odoo import models, fields

class MySchoolClasse(models.Model):
    _name = 'myschool.classe'

    name = fields.Char(string='Nom', required=True)
    effectif = fields.Char(string='Effectif', required=True)

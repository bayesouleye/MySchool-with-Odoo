# eleve.py

from odoo import models, fields


class MySchoolEleve(models.Model):
    _name = 'myschool.eleve'
    _description = 'Utilisateur de l\'application MySchool'

    user = fields.Many2one('myschool.user', string='user')

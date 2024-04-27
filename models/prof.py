# prof.py

from odoo import models, fields


class MySchoolProf(models.Model):
    _name = 'myschool.prof'
    _description = 'Utilisateur de l\'application MySchool'

    user = fields.Many2one('myschool.user', string='user')
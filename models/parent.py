# parent.py

from odoo import models, fields


class MySchoolParent(models.Model):
    _name = 'myschool.parent'
    _description = 'Utilisateur de l\'application MySchool'

    user = fields.Many2one('myschool.user', string='user')

# admin.py

from odoo import models, fields


class MySchoolAdmin(models.Model):
    _name = 'myschool.admin'
    _description = 'Utilisateur de l\'application MySchool'

    user = fields.Many2one('myschool.user',string = 'user')

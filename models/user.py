# user.py

from odoo import models, fields


class MySchoolUser(models.Model):
    _name = 'myschool.user'
    _description = 'Utilisateur de l\'application MySchool'

    name = fields.Char(string='Nom', required=True)
    first_name = fields.Char(string='Prénom', required=True)
    role = fields.Char(string='role', required=True)
    email = fields.Char(string='Email', required=True)
    phone_number = fields.Char(string='Numéro de téléphone')
    address = fields.Text(string='Adresse')
    password = fields.Char(string='Mot de passe', required=True)



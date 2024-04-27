# note.py

from odoo import models, fields


class MySchoolNote(models.Model):
    _name = 'myschool.note'

    valeur = fields.Integer(string='Note', required=True)

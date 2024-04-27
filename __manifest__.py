# __manifest__.py

{
    'name': 'MySchool',
    'version': '1.0',
    'summary': 'Module de gestion d\'utilisateurs pour une école',
    'description': 'Module pour la gestion des utilisateurs dans une école.',
    'author': 'Souleye Diago',
    'depends': ['base'],
    'data': [
'security/ir.model.access.csv',
        'views/views.xml',
        'demo/demo.xml'
        'groupe.xml'

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

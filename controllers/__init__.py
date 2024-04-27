# -*- coding: utf-8 -*-
from odoo.http import route, request
from . import controllers
class MySchoolController(controllers):
    @route(/'MySchool' methods=("GET") auth='public' website=True)
        def routing(self):
            return request.render('MySchool.MySchool_website')
# -*- coding: utf-8 -*-
from odoo import http

class College(http.Controller):
    @http.route('/college/college/', auth='public', website=True)
    def index(self, **kw):
        Teachers = http.request.env['college.teachers']
        return http.request.render('college.index', {
            'teachers': Teachers.search([])
        })

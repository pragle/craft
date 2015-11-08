#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'

from web.view import html, data


class RulesRouter:
    def __init__(self, app):
        self.app = app

        self.html = html.HTML(self.app)
        self.data = data.Data(self.app)

        self.prefix = ''

    def configure(self):
        self.app.add_url_rule(self.prefix+'/', 'index', self.html.index)
        self.app.add_url_rule(self.prefix+'/data', 'data', self.data.initial_data)
        self.app.add_url_rule(self.prefix+'/db/test', 'db_test', self.data.db_test, methods=['POST'])
        self.app.add_url_rule(self.prefix+'/code/generate', 'code_generate',
                              self.data.code_generate, methods=['POST'])

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
        self.app.add_url_rule(self.prefix+'/connection/test', 'connection_test', self.data.connection_test,
                              methods=['POST'])

#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'

from web.view import html, data, dbconnection


class RulesRouter:
    def __init__(self, app, db, cache):
        self.app = app
        self.db = db
        self.cache = cache

        self.html = html.HtmlRouter(self.app)
        self.data = data.DataRouter(self.app, self.db)
        self.dbdata = dbconnection.DBConnectionRouter(self.app, self.db, self.cache)

        self.prefix = ''

    def configure(self):
        self.app.add_url_rule(self.prefix+'/', 'index', self.html.index)
        self.app.add_url_rule(self.prefix+'/data', 'data', self.data.initial_data)
        self.app.add_url_rule(self.prefix+'/db/test', 'db_test', self.data.db_test, methods=['POST'])
        self.app.add_url_rule(self.prefix+'/code/generate', 'code_generate', self.data.code_generate, methods=['POST'])
        # dbconnection
        self.app.add_url_rule(self.prefix+'/db/connection/add', self.dbdata.add_connection, methods=['POST'])
        self.app.add_url_rule(self.prefix+'/db/connection/remove', self.dbdata.remove_connection, methods=['POST'])
        self.app.add_url_rule(self.prefix+'/db/connection/list/<name>', self.dbdata.list_connection, methods=['GET'])
        self.app.add_url_rule(self.prefix+'/db/connection/test', self.dbdata.test_connection, methods=['POST'])
        self.app.add_url_rule(self.prefix+'/db/query', self.dbdata.query, methods=['POST'])
        self.app.add_url_rule(self.prefix+'/db/structure/<name>', self.dbdata.db_structure, methods=['GET'])
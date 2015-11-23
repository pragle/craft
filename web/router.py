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
        self.dbconnection = dbconnection.DBConnectionRouter(self.app, self.db, self.cache)

        self.prefix = ''

    def configure(self):
        self.app.add_url_rule(self.prefix+'/', 'index', self.html.index)
        self.app.add_url_rule(self.prefix+'/data', 'data', self.data.initial_data)
        self.app.add_url_rule(self.prefix+'/db/test', 'db_test', self.data.db_test, methods=['POST'])
        self.app.add_url_rule(self.prefix+'/code/generate', 'code_generate', self.data.code_generate, methods=['POST'])
        # dbconnection
        self.app.add_url_rule(self.prefix+'/db/connection/add', 'db_connection_add',
                              self.dbconnection.add_connection, methods=['POST'])
        self.app.add_url_rule(self.prefix+'/db/connection/remove', 'db_connection_remove',
                              self.dbconnection.remove_connection, methods=['POST'])
        self.app.add_url_rule(self.prefix+'/db/connection/list', 'db_connection_list',
                              self.dbconnection.list_connection, methods=['GET'])
        self.app.add_url_rule(self.prefix+'/db/connection/test', 'db_connection_test',
                              self.dbconnection.test_connection, methods=['POST'])
        self.app.add_url_rule(self.prefix+'/db/query', 'db_query',
                              self.dbconnection.query, methods=['POST'])
        self.app.add_url_rule(self.prefix+'/db/structure', 'db_structure',
                              self.dbconnection.db_structure, methods=['GET'])

#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'

from craft import constraints

from flask import json, request


class DBConnectionRouter:

    def __init__(self, app, db, cache):
        self.app = app
        self.db = db
        self.cache = cache

    def configure(self, prefix):
        prefix += '/db'
        self.app.add_url_rule(prefix+'/connection/add', 'db_connection_add', self.add_connection, methods=['POST'])
        self.app.add_url_rule(prefix+'/connection/remove', 'db_connection_remove',
                              self.remove_connection, methods=['POST'])
        self.app.add_url_rule(prefix+'/connection/list', 'db_connection_list', self.list_connection, methods=['GET'])
        self.app.add_url_rule(prefix+'/connection/test', 'db_connection_test', self.test_connection, methods=['POST'])
        self.app.add_url_rule(prefix+'/query', 'db_query', self.query, methods=['POST'])
        self.app.add_url_rule(prefix+'/structure', 'db_structure', self.db_structure, methods=['GET'])

    def add_connection(self):
        data = json.loads(request.data)
        self.cache.conne
        return json.dumps({'code': -1, 'msg': 'TODO', 'time': 10000, 'data': None})

    def remove_connection(self):
        data = json.loads(request.data)
        return json.dumps({'code': -1, 'msg': 'TODO', 'time': 10000, 'data': None})

    def test_connection(self):
        data = json.loads(request.data)
        return json.dumps({'code': -1, 'msg': 'TODO', 'time': 10000, 'data': None})

    def list_connection(self):
        return json.dumps({'code': -1, 'msg': 'TODO', 'time': 10000, 'data': None})

    def query(self):
        data = json.loads(request.data)
        return json.dumps({'code': -1, 'msg': 'TODO', 'time': 10000, 'data': None})

    def db_structure(self):
        data = json.loads(request.data)
        return json.dumps({'code': -1, 'msg': 'TODO', 'time': constraints.POPUP_TIMEOUT, 'data': None})

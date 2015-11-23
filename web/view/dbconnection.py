#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'

from craft import constraints
from web.db import query_connection

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
        self.app.add_url_rule(prefix+'/structure', 'db_structure', self.db_structure, methods=['POST'])

    def add_connection(self):
        data = json.loads(request.data)
        result = query_connection.AddConnection(data, self.db, self.cache)
        return json.dumps({'code': result.code, 'msg': result.msg, 'time': result.time, 'data': result.data})

    def remove_connection(self):
        data = json.loads(request.data)
        result = query_connection.RemoveConnection(data, self.db, self.cache)
        return json.dumps({'code': result.code, 'msg': result.msg, 'time': result.time, 'data': result.data})

    def test_connection(self):
        data = json.loads(request.data)
        return json.dumps({'code': -1, 'msg': 'TODO', 'time': 10000, 'data': None})

    def list_connection(self):
        out = self.cache.connections.list()
        return json.dumps({'code': 0, 'msg': 'List connections', 'time': 5000, 'data': out})

    def query(self):
        data = json.loads(request.data)
        result = query_connection.QueryConnection(data, self.cache)
        return json.dumps({'code': result.code, 'msg': result.msg, 'time': result.time, 'data': result.data})

    def db_structure(self):
        data = json.loads(request.data)
        result = query_connection.DatabaseStructure(data, self.cache)
        return json.dumps({'code': result.code, 'msg': result.msg, 'time': result.time, 'data': result.data})

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

    def add_connection(self):
        data = json.loads(request.data)
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

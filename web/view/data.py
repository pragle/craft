#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Michal Szczepanski'


from craft import constraints
from flask import json, request


class Data:
    def __init__(self, app):
        self.app = app

    def initial_data(self):
        data = {
            'db': constraints.SQL_DB_TYPES,
            'framework': constraints.FRAMEWORKS
        }
        return json.dumps({'code': 0, 'msg': '', 'data': data})

    def connection_test(self):
        data = json.loads(request.data)
        return json.dumps({'code': 0, 'msg': 'Connection ok', 'data': None})
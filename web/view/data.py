#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Michal Szczepanski'


from craft import constraints
from craft.db.connector import DBConnector

from sqlalchemy.ext.declarative import declarative_base

from flask import json, request

Base = declarative_base()


class Data:
    def __init__(self, app):
        self.app = app

    def initial_data(self):
        data = {
            'db': constraints.SQL_DB_TYPES,
            'framework': constraints.FRAMEWORKS,
            'separator': constraints.SEPARATORS
        }
        return json.dumps({'code': 0, 'msg': '', 'data': data})

    def connection_test(self):
        data = json.loads(request.data)
        db = DBConnector({
            'path': 'sqlite:///'+data['host'],
            'echo': True,
        })
        db.create_session()
        # reset database
        Base.metadata.drop_all(db._engine)
        Base.metadata.create_all(db._engine)
        return json.dumps({'code': 0, 'msg': 'Connection ok', 'time': constraints.POPUP_TIMEOUT, 'data': None})
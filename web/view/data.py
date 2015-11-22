#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Michal Szczepanski'

import logging

from craft import constraints, model_factory, model
from craft.db.connector import DBConnector
from craft.generator import Generator
from web import model as web_model

from sqlalchemy.ext.declarative import declarative_base

from flask import json, request

Base = declarative_base()

logger = logging.getLogger()


class DataRouter:
    def __init__(self, app, db):
        self.app = app
        self.db = db

    def initial_data(self):
        data = {
            'db': constraints.SQL_DB_TYPES,
            'orm': constraints.ORM,
            'separator': constraints.SEPARATORS
        }
        return json.dumps({'code': 0, 'msg': '', 'data': data})

    def db_test(self):
        data = json.loads(request.data)
        config = model.DBConfig(data)
        db = DBConnector(config)
        db.create_session()
        return json.dumps({'code': 0, 'msg': 'Connection ok', 'time': constraints.POPUP_TIMEOUT, 'data': None})

    def code_generate(self):
        data = json.loads(request.data)
        config = model_factory.create_config(data)
        generator = Generator(config)
        out = generator.generate()
        logger.info('code generate : %s' % request.data)
        return json.dumps({'code': 0, 'msg': '', 'time': constraints.POPUP_TIMEOUT, 'data': out})

    def get_tables(self):
        return 'siema'

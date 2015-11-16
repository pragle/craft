#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Michal Szczepanski'

import logging

from craft import constraints, model_factory
from craft.db.connector import DBConnector
from craft.generator import Generator

from sqlalchemy.ext.declarative import declarative_base

from flask import json, request

Base = declarative_base()

logger = logging.getLogger()


class Data:
    def __init__(self, app):
        self.app = app

    def initial_data(self):
        data = {
            'db': constraints.SQL_DB_TYPES,
            'orm': constraints.ORM,
            'separator': constraints.SEPARATORS
        }
        return json.dumps({'code': 0, 'msg': '', 'data': data})

    def db_test(self):
        data = json.loads(request.data)
        db = DBConnector({
            'path': 'sqlite:///'+data['host'],
            'echo': True,
        })
        db.create_session()
        return json.dumps({'code': 0, 'msg': 'Connection ok', 'time': constraints.POPUP_TIMEOUT, 'data': None})

    def code_generate(self):
        data = json.loads(request.data)
        config = model_factory.create_config(data)
        generator = Generator(config)
        out = generator.generate()
        logger.info('code generate : %s' % request.data)
        return json.dumps({'code': 0, 'msg': 'TODO', 'time': constraints.POPUP_TIMEOUT, 'data': out})
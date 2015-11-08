#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Michal Szczepanski'

import logging

from craft import constraints
from craft.db.connector import DBConnector
from craft.db.parser import DBParser
from craft.generator import Generator, GenConfig

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
            'framework': constraints.FRAMEWORKS,
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
        db = DBConnector({
            'path': 'sqlite:///'+data['db']['host'],
            'echo': True,
        })
        db.create_session()
        parser = DBParser()
        structure = parser.parsetables(db.get_metadata(), db.dbversion)
        conf = {
            'name': data['framework']['name'],
            'language': data['language'],
            'tabulation': data['tabulation'],
            'separator': data['separator']['sep'],
            'file': data['framework']['file'],
        }
        generator = Generator(conf)
        generator.generate(structure)
        logger.info('code generate : %s' % request.data)
        return json.dumps({'code': 0, 'msg': 'TODO', 'time': constraints.POPUP_TIMEOUT, 'data': None})
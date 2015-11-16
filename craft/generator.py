#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'

import logging

from craft.db.parser import DBParser
from craft.db.connector import DBConnector

from craft.gen.sqldb.sqlalchemy import SQLAlchemyGenerator
from craft.gen.sqldb.hibernate import HibernateGenerator
from craft.gen.sqldb.django import DjangoGenerator

logger = logging.getLogger()


class Generator:

    def __init__(self, config):
        self.config = config

        self.db = DBConnector({
            'path': config.get_db_path(),
            'echo': True,
        })
        self.db.create_session()
        self.parser = DBParser()
        self.structure = self.parser.parsetables(self.db.get_metadata(), self.db.dbversion)

        name = self.config.orm['name']
        if name == 'sqlalchemy':
            self.generator = SQLAlchemyGenerator(config, self.structure)
        elif name == 'django':
            self.generator = DjangoGenerator(config, self.structure)
        elif name == 'hibernate':
            self.generator = HibernateGenerator(config, self.structure)
        else:
            self.generator = None

    def generate(self):
        if self.generator is not None:
            self.generator.generate()
        else:
            logger.warn('no such generator')

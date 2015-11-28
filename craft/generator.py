#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'

import logging

from craft.db.parser import DBParser
from craft.db.connector import DBConnector

from craft.gen.sqldb.sqlalchemy import SQLAlchemyGenerator
from craft.gen.sqldb.hibernate import HibernateGenerator
from craft.gen.sqldb.django import DjangoGenerator
from craft.gen.sqldb.bookshelfjs import BookshelfJS
from craft.gen.sqldb.base import GeneratorOutput
from craft.gen.sqldb.base import BaseGenerator

logger = logging.getLogger()


class Generator:

    def __init__(self, config):
        self.config = config

        self.db = DBConnector(config)
        self.db.create_session()
        self.parser = DBParser()
        self.structure = self.parser.parsetables(self.db.get_metadata(), self.db.dbversion)

        name = self.config.orm['name']
        if name == 'sqlalchemy':
            self.orm = SQLAlchemyGenerator(config, self.structure)
        elif name == 'django':
            self.orm = DjangoGenerator(config, self.structure)
        elif name == 'hibernate':
            self.orm = HibernateGenerator(config, self.structure)
        elif name == 'bookshelfjs':
            self.orm = BookshelfJS(config, self.structure)
        else:
            self.orm = BaseGenerator(config, self.structure)

    def generate(self):
        output = GeneratorOutput()
        self.orm.generate(output)
        return output.serialize()

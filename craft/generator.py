#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'

import logging
from craft.gen.sqldb.sqlalchemy import SQLAlchemyGenerator
from craft.gen.sqldb.hibernate import HibernateGenerator
from craft.gen.sqldb.django import DjangoGenerator
from utils.conf import GenConfig

logger = logging.getLogger()


class Generator:

    def __init__(self, conf):
        self.conf = GenConfig(conf)
        if self.conf.name == 'sqlalchemy':
            self.generator = SQLAlchemyGenerator()
        elif self.conf.name == 'django':
            self.generator = DjangoGenerator()
        elif self.conf.name == 'hibernate':
            self.generator = HibernateGenerator()

    def generate(self, structure):
        if self.generator is not None:
            self.generator.generate(structure=structure, conf=self.conf)
        else:
            logger.warn('no such generator')
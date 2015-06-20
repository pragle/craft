#!/usr/bin/python
# -*- codding: utf-8 -*--
__author__ = 'Michal Szczepanski'

from craft.gen.sqlalchemy import SQLAlchemyGenerator
from craft.gen.hibernate import HibernateGenerator
from craft.gen.django import DjangoGenerator
from craft.conf import GenConfig


class Generator():

    def __init__(self, conf):
        self.conf = GenConfig(conf)
        if self.conf.name == 'sqlalchemy':
            self.generator = SQLAlchemyGenerator()
        elif self.conf.name == 'django':
            self.generator = DjangoGenerator()
        elif self.conf.name == 'hibernate':
            self.generator = HibernateGenerator()

    def generate(self, tables):
        if self.generator is not None:
            self.generator.generate(tables=tables, conf=self.conf)
        else:
            print('no such generator')
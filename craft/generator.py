#!/usr/bin/python
# -*- codding: utf-8 -*--
__author__ = 'Michal Szczepanski'

from craft.gen.sqldb.sqlalchemy import SQLAlchemyGenerator
from craft.gen.sqldb.hibernate import HibernateGenerator
from craft.gen.sqldb.django import DjangoGenerator
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

    def generate(self, structure):
        if self.generator is not None:
            self.generator.generate(structure=structure, conf=self.conf)
        else:
            print('no such generator')
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'

from craft import broker
from craft import util
from craft.gen.sqldb.base import BaseGenerator


class DjangoGenerator(BaseGenerator):

    def generate(self):
        SEP = self.config.separator
        code = open(self.config.orm['file'], 'w+')
        out = ''
        out += self.header()
        out += 'from django.db import models'+SEP
        out += SEP
        for one in self.structure.tables:
            out += Table(one, self.config).get()
            out += SEP
        out = out[:len(out)-1]
        code.write(out)

    def header(self):
        SEP = self.config.separator
        out = '#!/usr/bin/env python'+SEP
        out += '# -*- coding: utf-8 -*-'+SEP
        out += '"""'+SEP
        out += 'THIS CODE WAS GENERATED AUTOMATICALY'+SEP
        out += 'MODIFICATIONS AT YOUR OWN RISK !!!'+SEP
        out += '"""'+SEP
        out += '__author__ = \'craft generator\''+SEP
        out += SEP
        return out


class Table(broker.Table):

    def __init__(self, parent, config):
        self.__dict__ = parent.__dict__
        self.config = config

    def get(self):
        SEP = self.config.separator
        TAB = self.config.tabulation
        out = ''+SEP
        clazz = util.name_to_camelcase(self.name, '_')
        out += 'class '+clazz+'(models.Model):'+SEP
        for one in self.columns:
            out += TAB+Column(one).get()+SEP
        return out


class Column(broker.Column):

    def __init__(self, parent):
        self.__dict__ = parent.__dict__

    def get(self):
        out = ''
        out += self.name
        out += ' = '
        out += Type(self.type).get()
        out += '('
        if self.primary:
            #if self.sequence_name:
            #    out += 'Sequence(\''+self.sequence_name+'\')'
            out += 'primary_key=True'
        #if self.foreignkey is not None:
        #    out += ', ForeignKey(\''+ForeignKey(self.foreignkey).get()+'\')'
        #if not self.nullable:
        #    out += ', null=True'
        if self.unique:
            out += ', unique=True'
        out += ')'
        return out


class ForeignKey(broker.ForeignKey):

    def __init__(self, parent):
        self.__dict__ = parent.__dict__

    def get(self):
        return self.fullname


class Type(broker.Type):

    def __init__(self, parent):
        self.__dict__ = parent.__dict__

    def get(self):
        if self.name == 'INTEGER':
            return 'models.IntegerField'
        elif self.name == 'SMALLINT':
            return 'models.PositiveSmallIntegerField'
        elif self.name == 'BOOLEAN':
            return 'models.BooleanField'
        elif self.name == 'TIMESTAMP':
            return 'models.DateTimeField'
        elif self.name == 'DOUBLE_PRECISION':
            return 'models.DecimalField'
        elif self.name == 'VARCHAR':
            return 'models.CharField'
        elif self.name == 'TEXT':
            return 'models.TextField'
        elif self.name == 'NullType':
            return 'models.Field'

    def imp(self):
        if self.version == 'sql':
            return 'from sqlalchemy.types import '+self.name
        elif self.version == 'psql':
            return 'from sqlalchemy.dialects.postgres import '+self.name
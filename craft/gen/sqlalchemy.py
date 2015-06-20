#!/usr/bin/python
# -*- codding: utf-8 -*--
__author__ = 'Michal Szczepanski'

from craft import broker, util
from craft.conf import GenConfig

'''
Generates SQLAlchemyCode in pep8 compatibile format
'''
class SQLAlchemyGenerator(object):

    def generate(self, tables, conf):
        code = open(conf.file, 'w+')
        out = ''
        out += self.header()
        out += self.resolve_import(tables)
        for one in tables:
            out += Table(one).get()
            out += GenConfig.SEP
        out = out[:len(out)-1]
        code.write(out)

    def header(self):
        SEP = GenConfig.SEP
        out = '#!/usr/bin/python'+SEP
        out += '# -*- codding: utf-8 -*--'+SEP
        out += '"""'+SEP
        out += 'THIS CODE WAS GENERATED AUTOMATICALY'+SEP
        out += 'MODIFICATIONS AT YOUR OWN RISK !!!'+SEP
        out += '"""'+SEP
        out += '__author__ = \'craft generator\''+SEP
        out += SEP
        return out

    def resolve_import(self, tables):
        SEP = GenConfig.SEP
        imp = set()
        for one in tables:
            for two in one.columns:
                t = Type(two.type)
                imp.add(t.imp())
        out = ''
        out += 'from sqlalchemy.sql.schema import Column, ForeignKey, Sequence'+SEP
        out += 'from sqlalchemy.ext.declarative import declarative_base'+SEP
        for one in imp:
            out+= one+SEP
        out += SEP
        out += 'Base = declarative_base()'
        out += SEP
        out += SEP
        return out


class Table(broker.Table):

    def __init__(self, parent):
        self.__dict__ = parent.__dict__

    def get(self):
        SEP = GenConfig.SEP
        TAB = GenConfig.TAB
        out = ''+SEP
        clazz = util.name_to_camelcase(self.name, '_')
        out += 'class '+clazz+'(Base):'+SEP
        out += TAB+'__tablename__ = \''+self.name+'\''+SEP
        out += TAB+SEP
        for one in self.columns:
            out += TAB+Column(one).get()+SEP
        return out


class Column(broker.Column):

    def __init__(self, parent):
        self.__dict__ = parent.__dict__

    def get(self):
        out = ''
        out += self.name
        out += ' = Column('
        out += Type(self.type).get()
        if self.primary:
            if self.sequence_name:
                out += ', Sequence(\''+self.sequence_name+'\')'
            out += ', primary_key=True'
        if self.foreignkey is not None:
            out += ', ForeignKey(\''+ForeignKey(self.foreignkey).get()+'\')'
        if not self.nullable:
            out += ', nullable=True'
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
        return self.name

    def imp(self):
        if self.version == 'sql':
            return 'from sqlalchemy.types import '+self.name
        elif self.version == 'psql':
            return 'from sqlalchemy.dialects.postgres import '+self.name
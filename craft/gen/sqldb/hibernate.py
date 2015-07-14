#!/usr/bin/python
# -*- codding: utf-8 -*--
__author__ = 'Michal Szczepanski'

import os
import shutil
from craft.conf import GenConfig
from craft import broker
from craft import util

class HibernateGenerator():

    def generate(self, structure, conf):
        dir = os.sep.join(conf.file.split('.'))
        if os.path.exists(dir):
           shutil.rmtree(dir)
        os.makedirs(dir)
        for one in structure.tables:
            clazz = util.name_to_camelcase(one.name, '_')
            with open(dir+os.sep+clazz+'.java', 'w+') as f:
                out = ''
                out += self.file_header(conf.file)
                out += Table(one).get()
                out += '}'
                f.write(out)


    def file_header(self, file):
        SEP = GenConfig.SEP
        out = ''
        out += 'package '+file+';'+SEP
        out += SEP
        out += 'import java.io.Serializable;'+SEP
        out += 'import javax.persistence.Table;'+SEP
        out += 'import javax.persistence.Column;'+SEP
        out += 'import javax.persistence.Entity;'+SEP
        out += 'import javax.persistence.GeneratedValue;'+SEP
        out += 'import javax.persistence.Id;'+SEP
        out += SEP
        return out

class Table(broker.Table):

    def __init__(self, parent):
        self.__dict__ = parent.__dict__

    def get(self):
        clazz = util.name_to_camelcase(self.name, '_')
        SEP = GenConfig.SEP
        out = ''
        out += '/**'+SEP
        out += '* @author craft generated'+SEP
        out += '*/'+SEP
        out += '@Entity'+SEP
        out += '@Table( name="'+self.name+'")'+SEP
        out += 'public class '+clazz+' implements Serializable {'+SEP
        out += SEP
        for one in self.columns:
            out += Column(one).get()
        for one in self.columns:
            out += Column(one).getset()
        return out


class Column(broker.Column):

    def __init__(self, parent):
        self.__dict__ = parent.__dict__

    def get(self):
        SEP = GenConfig.SEP
        TAB = GenConfig.TAB
        out = ''
        if self.primary:
            out += TAB+'@Id'+SEP
            if self.sequence_name:
                out += TAB+'@GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "idGenerator")'+SEP
                out += TAB+'@SequenceGenerator(name = "idGenerator", sequenceName = "'
                out += self.sequence_name+'", allocationSize = 50)'+SEP
            else:
                out += TAB+'@GeneratedValue'+SEP
        out += TAB+'@Column(name="'+self.name+'"'
        if not self.nullable:
            out += ', nullable=false'
        if self.type.length is not None:
            out += ', length= %d' % self.type.length
        if self.type.precision is not None:
            out += ', precision=%d' % self.type.precision
        if self.unique:
            out = ', unique=true'
        out +=')'+SEP
        out += TAB+'private '+Type(self.type).get()+' '+self.name+';'+SEP
        out += SEP
        return out

    def getset(self):
        SEP = GenConfig.SEP
        TAB = GenConfig.TAB
        one = Type(self.type).get()
        out = ''
        out += TAB+'public '+one+' get'
        out += util.upper_first(self.name)+'() {'+SEP
        out += TAB+TAB
        out += 'return '+self.name+';'+SEP
        out += TAB+'}'+SEP
        out += SEP
        out += TAB+'public '+one+' set'
        out += util.upper_first(self.name)+'('+one+' value) {'+SEP
        out += TAB+TAB
        out += 'this.'+self.name+' = value;'+SEP
        out += TAB+'}'+SEP
        out += SEP
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
        if self.name == 'INTEGER' or self.name == 'SMALLINT':
            return 'Integer'
        elif self.name == 'BOOLEAN':
            return 'Boolean'
        elif self.name == 'TIMESTAMP':
            return 'Long'
        elif self.name == 'DOUBLE_PRECISION':
            return 'Double'
        elif self.name == 'VARCHAR' or self.name == 'TEXT':
            return 'String'
        elif self.name == 'NullType':
            return 'Object'

    def imp(self):
        return ''
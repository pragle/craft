#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'

from craft import broker, util
from craft.gen.sqldb import base

'''
Generates bookshelfjs code
'''
class BookshelfJS(base.BaseGenerator):

    def generate(self, output):
        code = base.GeneratorOutputFile(self.config.orm['file'])
        code.data += self.header()
        #code.data += self.resolve_import(self.structure.tables)
        for one in self.structure.tables:
            code.data += Table(one, self.config).get()
            code.data += self.config.separator
        code.data = code.data[:len(code.data)-1]
        output.orm.append(code)

    def header(self):
        SEP = self.config.separator
        out = """var bookshelf = require('bookshelf')(knex);"""+SEP
        out += '/*'+SEP
        out += ' * THIS CODE WAS GENERATED AUTOMATICALY'+SEP
        out += ' * MODIFICATIONS AT YOUR OWN RISK !!!'+SEP
        out += ' * @author \'craft generator\''+SEP
        out += ' */'+SEP
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
        out += 'var '+clazz+' = bookshelf.Model.extend({'+SEP
        out += TAB+'tablename: \''+self.name+'\''+SEP
        out += '});'
        out += TAB+SEP
        '''
        for one in self.columns:
            out += TAB+Column(one).get()+SEP
        '''
        return out
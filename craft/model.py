#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'


class Config:

    def __init__(self, data):
        self.db = data[0]
        self.language = data[1]
        self.orm = data[2]
        self.separator = data[3]
        self.tabulation = data[4]

    def get_db_path(self):
        out = None
        if self.db['name'] == 'sqlite':
            out = ('sqlite:///%s' % self.db['host'])
        elif self.db['name'] == 'postgresql':
            out = ('postgresql://%s:%s@%s:%s/%s' %
                   (self.db['username'], self.db['password'], self.db['host'], self.db['port'], self.db['name']))
        return out

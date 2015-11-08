#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'

import json


class GenType:
    SQL = 'sql'
    PSQL = 'psql'


class GenConfig:

    SEP = '\n'
    TAB = '\t'

    def __init__(self, data):
        self.language = data['language']
        self.name = data['name']
        self.file = data['file']
        GenConfig.TAB = data['tabulation']
        GenConfig.SEP = data['separator']


class Config:

    @staticmethod
    def parse(filename):
        f = open(filename)
        data = json.load(f)
        return data
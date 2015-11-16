#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'

from craft import model


def create_config(data):
    db = data['db']
    orm = data['orm']
    separator = data['separator']
    tabulation = data['tabulation']
    if tabulation == '\\t':
        tabulation = '\t'
    params = [db, data['language'], orm, separator['sep'], tabulation]
    config = model.Config(params)
    return config
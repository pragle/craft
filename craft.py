#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'

import logging
import logging.config
from web import server
from flask import json


def start():
    '''
    data = Config.parse('conf.json')
    db = DBConnector(conf=data['db'])
    parser = DBParser()
    structure = parser.parsetables(db.get_metadata(), db.dbversion)
    for one in data['generator']:
        generator = Generator(one)
        generator.generate(structure=structure)
    '''
    # load logging configuration
    logging.config.fileConfig('conf/logging.ini')
    # load server configuration
    conf = json.load(open('conf/www.json'))
    www = conf['www']
    # start web server
    web = server.WebApp(www)
    web.start()


if __name__ == '__main__':

    start()
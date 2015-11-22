#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'

import logging
import logging.config
from web import server
from flask import json


def start():
    # load logging configuration
    logging.config.fileConfig('conf/logging.ini')
    # load server configuration
    conf = json.load(open('conf/www.json'))
    www = conf['www']
    db_path = conf['database']
    # start web server
    web = server.WebApp(www, db_path)
    web.start()


if __name__ == '__main__':

    start()
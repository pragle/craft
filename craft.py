#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'

import os
import logging
import logging.config
from web import server
from flask import json


def init_logging(directory):
    # check log directory exists
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except:
            raise RuntimeError('Cannot create directory for logs : %s' % directory)
    # load logging configuration
    logging.config.fileConfig('conf/logging.ini', defaults={
        'logdirectory': directory
    })


def start():
    conf = json.load(open('conf/www.json'))
    init_logging(conf['logging']['directory'])
    # load server configuration

    www = conf['www']
    db_path = conf['database']
    # start web server
    web = server.WebApp(www, db_path)
    web.start()


if __name__ == '__main__':

    start()
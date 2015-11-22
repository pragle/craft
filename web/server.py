#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'

import logging
from flask import Flask, request
from utils import dependencies
from web import router, db_connector, cache

logger = logging.getLogger()


class WebApp:
    def __init__(self, www, db_path):
        self.www = www
        self.db = db_connector.DB(db_path)
        self.html_dependencies()
        self.cache = cache.Cache()

    def start(self):
        host = self.www['host']
        port = self.www['port']
        static_folder = self.www['static_folder']
        template_folder = self.www['template_folder']
        debug = self.www['debug']

        self.app = Flask(__name__,
                         static_folder=static_folder,
                         template_folder=template_folder)

        router.RulesRouter(self.app, self.db, self.cache).configure()

        logger.info('craft-server-start')
        self.app.run(host=host, port=port, debug=debug, use_reloader=False)

    def stop(self):
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            logger.error('craft-server-stop-error')
            raise RuntimeError('Not running with the Werkzeug Server')
        func()
        logger.info('craft-server-stop')

    def html_dependencies(self):
        deps = self.www['ext']
        dependencies.download(deps['path'], deps['file'])


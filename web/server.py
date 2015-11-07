#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'

import logging
from flask import Flask, request
from utils import dependencies
from web import router

logger = logging.getLogger()


class WebApp:
    def __init__(self, www):
        self.www = www
        self.html_dependencies()

    def start(self):
        host = self.www['host']
        port = self.www['port']
        static_folder = self.www['static_folder']
        template_folder = self.www['template_folder']
        debug = self.www['debug']

        self.app = Flask(__name__,
                         static_folder=static_folder,
                         template_folder=template_folder)

        router.RulesRouter(self.app).configure()

        logger.info('craft-server-start')
        self.app.run(host=host, port=port, debug=debug, use_reloader=True)

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


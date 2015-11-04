#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'

from flask import Flask, render_template, json


class WebApp:
    def __init__(self, host, port, debug, static_folder, template_folder):

        self.app = Flask(__name__,
                         static_folder=static_folder,
                         template_folder=template_folder)

        self.app.add_url_rule('/', 'index', self.__index)

        self.app.run(host=host, port=port, debug=debug, use_reloader=False)


    def resolve_dependencies(self):
        data = json.load(open('conf/html.json', 'r'))

    def __index(self):
        return render_template('index.html')

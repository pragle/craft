#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'


class HTML:
    def __init__(self, app):
        self.app = app

    def index(self):
        return self.app.send_static_file('html/index.html')
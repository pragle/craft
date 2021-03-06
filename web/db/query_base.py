#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'


class QueryBase:
    def __init__(self):
        self.msg = 'TODO'
        self.code = -1
        self.data = None
        self.time = 10000

    def out_success_green(self, data, msg, time):
        self.code = 0
        self.data = data
        self.msg = msg
        self.time = time

    def out_success_blue(self, data, msg, time):
        self.out_success_green(data, msg,time)
        self.code = 100

    def out_error(self, msg):
        self.code = 300
        self.msg = msg

    def out_warning(self, msg):
        self.code = 200
        self.msg = msg

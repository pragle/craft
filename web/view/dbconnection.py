#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'

from flask import json, request

class DBConnectionRouter:

    def __init__(self, app, db, cache):
        self.app = app
        self.db = db
        self.cache = cache

    def add_connection(self):
        data = json.loads(request.data)
        return 'TODO'


    def remove_connection(self):
        data = json.loads(request.data)
        return 'TODO'

    def test_connection(self):
        data = json.loads(request.data)
        return 'TODO'

    def execute_query(self):
        data = json.loads(request.data)
        return 'TODO'

    def get_last_queries(self):
        data = json.loads(request.data)
        return 'TODO'

    def get_db_structure(self):
        data = json.loads(request.data)
        return 'TODO'

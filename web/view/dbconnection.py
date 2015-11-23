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

    def list_connection(self):
        return 'TODO'

    def query(self):
        data = json.loads(request.data)
        return 'TODO'

    def db_structure(self):
        data = json.loads(request.data)
        return 'TODO'

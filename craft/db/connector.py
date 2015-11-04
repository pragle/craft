#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker


class DBConnector():

    sqldb = [
        'drizzle',
        'firebird',
        'mssql',
        'mysql',
        'oracle',
        'postgresql',
        'sqlite',
        'sybase'
    ]

    def __init__(self, conf):
        self._engine = create_engine(conf['path'], echo=conf['echo'])
        self._maker = sessionmaker(bind=self._engine, autocommit=False)
        self.dbversion = None
        self._resolve_version(conf['path'])

    def create_session(self):
        return self._maker()

    def get_metadata(self):
        meta = MetaData()
        meta.reflect(bind=self._engine)
        return meta

    def _resolve_version(self, path):
        for one in self.sqldb:
            if path.startswith(one):
                self.dbversion = one
                break

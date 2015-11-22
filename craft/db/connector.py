#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'

from sqlalchemy import create_engine, MetaData
from sqlalchemy import pool
from sqlalchemy.orm import sessionmaker, scoped_session

from craft import constraints


class DBConnector:
    """DBConnector
    connects to the databse based on version you provided
    """
    def __init__(self, config):
        self._engine = create_engine(config.get_db_path(), echo_pool=True, echo=True, pool_recycle=10)
        #self.pool = pool.QueuePool(self._engine, pool_size=10, timeout=10, echo=True)
        self._maker = scoped_session(sessionmaker(bind=self._engine, autocommit=False))
        self.dbversion = None
        self._resolve_version(config.get_db_path())

    def create_session(self):
        return self._maker()

    def get_metadata(self):
        meta = MetaData()
        meta.reflect(bind=self._engine)
        return meta

    def execute(self, query):
        return self._engine.execute(query)

    def _resolve_version(self, path):
        for one in constraints.SQL_DB_TYPES:
            if path.startswith(one['name']):
                self.dbversion = one['name']
                break

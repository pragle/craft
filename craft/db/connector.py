#!/usr/bin/python
# -*- codding: utf-8 -*--
__author__ = 'Michal Szczepanski'

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker


class DBConnector():

    def __init__(self, conf):
        self._engine = create_engine(conf['path'], echo=conf['echo'])
        self._maker = sessionmaker(bind=self._engine, autocommit=False)

    def create_session(self):
        return self._maker()

    def get_metadata(self):
        meta = MetaData()
        meta.reflect(bind=self._engine)
        return meta

#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from web.model import db_model


class DB:
    def __init__(self, path):
        self._engine = create_engine(path['path'], echo_pool=True, echo=True, pool_recycle=10)
        self._session = scoped_session(sessionmaker(bind=self._engine))
        db_model.Base.metadata.create_all(self._engine)

    def session(self):
        return self._session()

    def drop(self):
        db_model.Base.metadata.drop_all(self._engine)

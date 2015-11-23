#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'

import logging
from web.model import db_model

logger = logging.getLogger()


class Cache:

    def __init__(self, db):
        self.connections = Connections()
        self.prepare_connections(db)
        logger.info('cache init complete')

    def prepare_connections(self, db):
        session = db.session()
        try:
            query = session.query(db_model.DatabaseConnection)
            for one in query:
                data = {
                    'auth': False,
                    'connection_name': one.connection_name,
                    'db': one.database,
                    'name': one.name,
                    'host': one.host,
                    'port': one.port,
                }
                if one.username is not None:
                    data['auth'] = True
                    data['username'] = one.username
                    data['password'] = one.password
                self.connections.add(one.connection_name, data)
        finally:
            session.close()


class Connections:
    def __init__(self):
        self.data = {}
        # TODO should store actual connections
        self.connections = {}

    def add(self, name, connection):
        if self.data.has_key(name):
            logger.info('cache - has connection %s' % name)
            return False
        logger.info('cache - add connection %s' % name)
        self.data[name] = connection
        return True

    def remove(self, name):
        if self.data.has_key(name):
            logger.info('cache - remove connection %s' % name)
            del self.data[name]
            return True
        logger.info('cache - cannot remove connection %s' % name)
        return False

    def get(self, name):
        return self.data.get(name, None)

    def list(self):
        out = []
        for one in self.data:
            out.append(self.data[one])
        logger.info('cache - list connections')
        return out

    def connect(self, data):
        pass

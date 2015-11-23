#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'

from web.model import db_model
from web.db.query_base import QueryBase


class AddConnection(QueryBase):
    def __init__(self, data, db, cache):
        QueryBase.__init__(self)
        session = db.session()
        try:
            conn = self.make_db_connection(data)
            session.add(conn)
            session.commit()
            cache.connections.add(data['connection_name'], data)
            m = 'Added %s connection' % conn.connection_name
            self.out_success(conn.connection_name, m, 5000)
        except Exception, e:
            self.out_error(e.message)
        finally:
            session.close()

    def make_db_connection(self, data):
        out = db_model.DatabaseConnection()
        out.name = data['name']
        out.host = data['host']
        out.port = data['port']
        if data['auth']:
            out.username = data['username']
            out.password = data['password']
        out.database = data['db']
        out.connection_name = data['connection_name']
        return out


class RemoveConnection(QueryBase):

    def __init__(self, data, db, cache):
        QueryBase.__init__(self)
        session = db.session()
        try:
            session.delete(data['connection_name'])
            session.commit()
            cache.connections.remove(data['connection_name'])
            m = 'Added %s connection' % data['connection_name']
            self.out_success(data['connection_name'], m, 5000)
        except Exception, e:
            self.out_error(e.message)
        finally:
            session.close()

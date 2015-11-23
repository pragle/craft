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
            self.out_success_green(conn.connection_name, m, 5000)
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
            name = data['connection_name']
            query = session.query(db_model.DatabaseConnection)\
                .filter(db_model.DatabaseConnection.connection_name == name).first()
            session.delete(query)
            session.commit()
            cache.connections.remove(name)
            m = 'Removed %s connection' % name
            self.out_success_blue(name, m, 5000)
        except Exception, e:
            self.out_error(e.message)
        finally:
            session.close()


class QueryConnection(QueryBase):

    def __init__(self, data, cache):
        QueryBase.__init__(self)
        try:
            name = data['connection_name']
            query = data['query']
            conn = cache.connections.get(name)
            # TODO simplify move parts to cache
            from craft import model
            from craft.db.connector import DBConnector
            config = model.DBConfig(conn)
            db = DBConnector(config)
            result = db.execute(query)
            m = 'Query %s : %s' % (name, query)
            out = {
                'titles':result._metadata.keys,
                'data':[],
            }
            for one in result:
                out['data'].append(one._row)
            self.out_success_green(out, m, 5000)
        except Exception, e:
            self.out_error(e.message)


class DatabaseStructure(QueryBase):

    def __init__(self, data, cache):
        QueryBase.__init__(self)
        try:
            name = data['connection_name']
            conn = cache.connections.get(name)
            # TODO simplify move parts to cache
            from craft.db.parser import DBParser
            from craft import model
            from craft.db.connector import DBConnector
            config = model.DBConfig(conn)
            db = DBConnector(config)
            parser = DBParser()
            structure = parser.parsetables(db.get_metadata(), db.dbversion)
            m = 'DatabaseStructure : %s' % name
            self.out_success_green(self.serialize(structure), m, 5000)
        except Exception, e:
            self.out_error(e.message)

    def serialize(self, structure):
        return {}

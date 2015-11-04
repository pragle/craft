#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'

from sqlalchemy.dialects import postgresql

types = [
    postgresql.INTEGER.__name__,
    postgresql.BIGINT.__name__,
    postgresql.SMALLINT.__name__,
    postgresql.VARCHAR.__name__,
    postgresql.CHAR.__name__,
    postgresql.TEXT.__name__,
    postgresql.NUMERIC.__name__,
    postgresql.FLOAT.__name__,
    postgresql.REAL.__name__,
    postgresql.INET.__name__,
    postgresql.CIDR.__name__,
    postgresql.UUID.__name__,
    postgresql.BIT.__name__,
    postgresql.MACADDR.__name__,
    postgresql.OID.__name__,
    postgresql.DOUBLE_PRECISION.__name__,
    postgresql.TIMESTAMP.__name__,
    postgresql.TIME.__name__,
    postgresql.DATE.__name__,
    postgresql.BYTEA.__name__,
    postgresql.BOOLEAN.__name__,
    postgresql.INTERVAL.__name__,
    postgresql.ARRAY.__name__,
    postgresql.ENUM.__name__,
    postgresql.TSVECTOR.__name__,
    #next
    postgresql.HSTORE.__name__,
    postgresql.TSRANGE.__name__,
    postgresql.TSTZRANGE.__name__,
    postgresql.json.__name__,
    postgresql.JSON.__name__,
    postgresql.JSONB.__name__,
    postgresql.JSONElement.__name__,
]

# https://dev.mysql.com/doc/workbench/en/wb-migration-database-postgresql-typemapping.html
mysql_translate = [

]
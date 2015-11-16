#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'

from sqlalchemy.sql import sqltypes as typesql

from craft import broker
from craft.db.sql import postgres, mysql


class DBParser(object):

    def parsetables(self, metadata, dbversion):
        self.dbversion = dbversion
        meta = metadata.tables
        tables = []
        for key in meta:
            sqltable = broker.Table(key)
            table = meta[key]
            columns = []
            for one in table.columns:
                data = self.resolve_column(one, key)
                columns.append(data)
            sqltable.columns = columns
            tables.append(sqltable)
        deps = self.resolve_dependencies(tables)
        return broker.Structure(tables, deps)

    def resolve_dependencies(self, tables):
        deps = {}
        for one in tables:
            for col in one.columns:
                key = col.foreignkey
                if key:
                    if not deps.has_key(one.name):
                        deps[one.name] = []
                    deps[one.name].append(key.table)
        return deps

    def resolve_column(self, column, table):
        out = broker.Column(name=column.name, autoincrement=column.autoincrement, primary=column.primary_key,
                            nullable=column.nullable, unique=column.unique, type=self.resolve_type(column.type))
        # check sequence
        if column.primary_key and column.server_default is not None \
                and column.server_default.arg is not None:
            seq = column.server_default.arg.text.split('\'')[1]
            out.sequence_name = seq
            # match foreign key
        if len(column.foreign_keys) > 0:
            for foreign in column.foreign_keys:
                col = foreign.column
                out.foreignkey = broker.ForeignKey(table=col.table.name,
                                                   column=col.description,
                                                   name=foreign.target_fullname)
                break
        return out

    def resolve_type(self, type):
        name = type.__class__.__name__
        out = broker.Type(name=name, parsed=True, version='sql')

        if name == typesql.TIMESTAMP.__name__:
            out.timezone = type.timezone
        elif name == typesql.VARCHAR.__name__:
            if type.length is not None:
                out.length = type.length
        # cannot parse this one
        elif name == typesql.NullType:
            out.parsed = False
        # psql specific
        elif name in postgres.types and self.dbversion is 'postgresql':
            out.version = 'psql'
            if name == postgres.postgresql.DOUBLE_PRECISION.__name__:
                if type.precision is not None:
                    out.precision = type.precision
            elif name == postgres.postgresql.ARRAY.__name__:
                out.item_type = str(type.item_type)
        elif name in mysql.types and self.dbversion is 'mysql':
            out.version = 'mysql'
        return out
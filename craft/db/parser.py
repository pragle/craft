#!/usr/bin/python
# -*- codding: utf-8 -*--
__author__ = 'Michal Szczepanski'

from sqlalchemy.sql import sqltypes as typesql
from sqlalchemy.dialects import postgres as typepsql

from craft import broker


class DBParser(object):

    def parsetables(self, metadata):
        tables = metadata.tables
        out = []
        for key in tables:
            sqltable = broker.Table(key)
            table = tables[key]
            columns = []
            for one in table.columns:
                data = self.resolve_column(one, key)
                columns.append(data)
            sqltable.columns = columns
            out.append(sqltable)
        return out

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
                if foreign.parent.table.name == table:
                    out.foreignkey = broker.ForeignKey(name=foreign.name, fullname=foreign.target_fullname)
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
        elif name == typepsql.DOUBLE_PRECISION.__name__:
            out.version = 'psql'
            if type.precision is not None:
                out.precision = type.precision
        elif name == typepsql.SMALLINT:
            out.version = 'psql'
        return out
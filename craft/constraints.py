#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'

SQL_DB_TYPES = [
    {
        'name':'drizzle',
        'host':'127.0.0.1',
        'port':123
    },
    {
        'name':'firebird',
        'host':'127.0.0.1',
        'port':123
    },
    {
        'name':'mssql',
        'host':'127.0.0.1',
        'port':123
    },
    {
        'name':'mysql',
        'host':'127.0.0.1',
        'port':123
    },
    {
        'name':'oracle',
        'host':'127.0.0.1',
        'port':123
    },
    {
        'name':'postgresql',
        'host':'127.0.0.1',
        'port':123
    },
    {
        'name':'sqlite',
        'host':'127.0.0.1',
        'port':123
    },
    {
        'name':'sybase',
        'host':'127.0.0.1',
        'port':123
    },
]

FRAMEWORKS = {
    'python':['Django', 'SQLAlchemy'],
    'java':['Hibernate'],
}
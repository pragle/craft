#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'

SQL_DB_TYPES = [
    {
        'name': 'drizzle',
        'host': '127.0.0.1',
        'port': 123
    },
    {
        'name': 'firebird',
        'host': '127.0.0.1',
        'port': 123
    },
    {
        'name': 'mssql',
        'host': '127.0.0.1',
        'port': 123
    },
    {
        'name': 'mysql',
        'host': '127.0.0.1',
        'port': 123
    },
    {
        'name': 'oracle',
        'host': '127.0.0.1',
        'port': 123
    },
    {
        'name': 'postgresql',
        'host': '127.0.0.1',
        'port': 123
    },
    {
        'name': 'sqlite',
        'host': 'test.db',
        'port': None
    },
    {
        'name': 'sybase',
        'host': '127.0.0.1',
        'port': 123
    },
]

FRAMEWORKS = [
    {
        'language': 'python',
        'framework': [
            {
                'name':'django',
                'file':'models.py'
            },
            {
                'name':'SQLAlchemy',
                'file':'model.py'
            },
        ],
        'tabulation': '    ',
    },
    {
        'language': 'java',
        'framework': [
            {
                'name':'Hibernate',
                'file':'com.test'
            }
        ],
        'tabulation': '\\t'
    },
]

SEPARATORS = [
    {
        'name': 'Unix / OS X ( \\n )',
        'sep': '\n'
    },
    {
        'name': 'Classic Mac ( \\r )',
        'sep': '\r'
    },
    {
        'name': 'Windows ( \\r\\n )',
        'sep': '\r\n'
    },
]

POPUP_TIMEOUT = 1000
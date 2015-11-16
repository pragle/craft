#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'

SQL_DB_TYPES = [
    {
        'name': 'drizzle',
        'host': '127.0.0.1',
        'port': 4427,
        'auth': True
    },
    {
        'name': 'firebird',
        'host': '127.0.0.1',
        'port': 3050,
        'auth': True
    },
    {
        'name': 'mssql',
        'host': '127.0.0.1',
        'port': 1433,
        'auth': True
    },
    {
        'name': 'mysql',
        'host': '127.0.0.1',
        'port': 3306,
        'auth': True
    },
    {
        'name': 'oracle',
        'host': '127.0.0.1',
        'port': 1521,
        'auth': True
    },
    {
        'name': 'postgresql',
        'host': '127.0.0.1',
        'port': 5432,
        'auth': True
    },
    {
        'name': 'sqlite',
        'host': 'test.db',
        'port': None,
        'auth': False
    },
    {
        'name': 'sybase',
        'host': '127.0.0.1',
        'port': 2638,
        'auth': True
    },
]

ORM = [
    {
        'language': 'python',
        'orm': [
            {
                'name': 'django',
                'file': 'models.py'
            },
            {
                'name': 'sqlalchemy',
                'file': 'model.py'
            },
        ],
        'tabulation': '    ',
    },
    {
        'language': 'java',
        'orm': [
            {
                'name': 'hibernate',
                'package': 'com.test'
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

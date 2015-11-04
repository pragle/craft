#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'

from sqlalchemy.dialects import mysql

'''
GRANT ALL PRIVILEGES ON *.* TO 'USERNAME'@'IP' IDENTIFIED BY 'PASSWORD';
FLUSH PRIVILEGES;

USE DATABASE 'DATABASENAME'
SHOW DATABASES
SHOW TABLES;
'''

types = [

    mysql.BIGINT.__name__,
    mysql.BIT.__name__,
#    mysql.CHAR.__name__,
#    mysql.DATETIME.__name__,
#    mysql.DECIMAL.__name__,
#    mysql.DOUBLE.__name__,
    mysql.ENUM.__name__,
#    mysql.FLOAT.__name__,
#    mysql.INTEGER.__name__,
    mysql.LONGBLOB.__name__,
    mysql.LONGTEXT.__name__,
    mysql.MEDIUMBLOB.__name__,
    mysql.MEDIUMINT.__name__,
    mysql.MEDIUMTEXT.__name__,
    mysql.NCHAR.__name__,
    mysql.NUMERIC.__name__,
    mysql.NVARCHAR.__name__,
    mysql.REAL.__name__,
    mysql.SET.__name__,
    mysql.SMALLINT.__name__,
#    mysql.TEXT.__name__,
#    mysql.TIMESTAMP.__name__,
    mysql.TINYBLOB.__name__,
    mysql.TINYINT.__name__,
    mysql.TINYTEXT.__name__,
    mysql.YEAR.__name__,

]
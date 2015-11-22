#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'


from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Boolean, Binary

Base = declarative_base()


class DatabaseConnection(Base):

    __tablename__ = 'database_connection'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    host = Column(String)
    port = Column(Integer)
    username = Column(String)
    password = Column(String)

    tables = relationship('DatabaseName', lazy='subquery')


class DatabaseName(Base):

    __tablename__ = 'database_name'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    connection_id = Column(ForeignKey('database_connection.id'))


'''
class SSHConnection(Base):

    __tablename__ = 'ssh_connection'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    host = Column(String)
    port = Column(String)
    auth_id = Column(Integer, ForeignKey('ssh_connection_auth.id'))


class SSHConnectionAuth(Base):

    __tablename__ = 'ssh_connection_auth'

    id = Column(Integer, primary_key=True)
    key = Column(Boolean, default=False)
    key_data = Column(Binary)
    username = Column(String)
    password = Column(String)

    connections = relationship('SSHConnection')
'''

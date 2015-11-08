#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'

from craft.db.connector import DBConnector

from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, Boolean

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=100))
    surname = Column(String(length=100))

    address = relationship('Address', uselist=False, backref="parent")


class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True, autoincrement=True)

    person = Column(Integer, ForeignKey('address.id'))


def start(conf):
    db = DBConnector(conf)
    db.create_session()
    # reset database
    Base.metadata.drop_all(db._engine)
    Base.metadata.create_all(db._engine)

if __name__ == '__main__':
    conf = {
        'path': 'sqlite:///test.db',
        'echo': True
    }
    start(conf)

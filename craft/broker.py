#!/usr/bin/python
# -*- codding: utf-8 -*--
__author__ = 'Michal Szczepanski'


class Table():
    def __init__(self, name):
        self.name = name
        self.columns = []


class Column():
    def __init__(self, name, autoincrement, primary, nullable, unique, type):
        self.name = name
        self.autoincrement = autoincrement
        self.primary = primary
        self.nullable = nullable
        self.unique = unique
        self.type = type
        self.foreignkey = None
        self.sequence_name = None


class ForeignKey():
    def __init__(self, name, fullname):
        self.name = name
        self.fullname = fullname


class Type():
    def __init__(self, name, parsed, version):
        self.name = name
        self.parsed = parsed
        self.version = version
        self.timezone = None
        self.precision = None
        self.length = None
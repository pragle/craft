#!/usr/bin/python
# -*- codding: utf-8 -*--
__author__ = 'Michal Szczepanski'

from craft.db.parser import DBParser
from craft.db.connector import DBConnector
from craft.generator import Generator
from craft.conf import Config


def start():
    data = Config.parse('conf.json')
    db = DBConnector(conf=data['db'])
    parser = DBParser()
    structure = parser.parsetables(db.get_metadata(), db.dbversion)
    for one in data['generator']:
        generator = Generator(one)
        generator.generate(structure=structure)

if __name__ == '__main__':
    start()
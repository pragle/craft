#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'

from web import server


def start():
    '''
    data = Config.parse('conf.json')
    db = DBConnector(conf=data['db'])
    parser = DBParser()
    structure = parser.parsetables(db.get_metadata(), db.dbversion)
    for one in data['generator']:
        generator = Generator(one)
        generator.generate(structure=structure)
    '''
    sf = 'html/static'
    tf = 'html/templates'
    web = server.WebApp(host='127.0.0.1', port=7070, debug=True, static_folder=sf, template_folder=tf)


if __name__ == '__main__':
    start()
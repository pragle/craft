#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'


class BaseGenerator:

    def __init__(self, config, structure):
        self.config = config
        self.structure = structure

    def generate(self, output):
        raise RuntimeError('BaseGenerator.generate is abstract method')


class GeneratorOutput:
    def __init__(self):
        self.orm = []

    def serialize(self):
        out = []
        for one in self.orm:
            out.append(one.serialize())
        return {'orm': out}


class GeneratorOutputFile:
    def __init__(self, path):
        self.path = path
        self.data = ''

    def serialize(self):
        return {'path': self.path, 'data': self.data}

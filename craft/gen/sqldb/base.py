#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'


class BaseGenerator:

    def __init__(self, config, structure):
        self.config = config
        self.structure = structure

    def generate(self):
        raise RuntimeError('BaseGenerator.generate is abstract method')

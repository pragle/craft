#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Michal Szczepanski'

import  os, shutil


def name_to_camelcase(name, sep):
    out = ''
    a = name.split(sep)
    for one in a:
        out += one[0].upper()+one[1:]
    return out


def upper_first(name):
    return name[0].upper()+name[1:]


def make_dirs(name, separator):
    dir = os.sep.join(name.split(separator))
    if os.path.exists(dir):
        shutil.rmtree(dir)
    os.makedirs(dir)
    return dir
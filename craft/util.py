#!/usr/bin/python
# -*- codding: utf-8 -*--
__author__ = 'Michal Szczepanski'


def name_to_camelcase(name, sep):
    out = ''
    a = name.split(sep)
    for one in a:
        out += one[0].upper()+one[1:]
    return out

def upper_first(name):
    return name[0].upper()+name[1:]
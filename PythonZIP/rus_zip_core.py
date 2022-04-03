# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 09:55:14 2022

@author: Владислав
"""


def record_by_zip(data, zipcode: int):
    for line in data:
        if line[0] == zipcode:
            return line
    return


def record_by_name(data, name: str):
    for line in data:
        if line[1] == name:
            return line
    return

# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 18:53:18 2022

@author: Владислав
"""


def load_data():
    data = []
    with open(get_key_value('FILENAME'), encoding='utf-8') as file:
        filecontent = file.read().split("\n")
        # print(len(filecontent))
        header = filecontent[0].split(get_key_value('DATASEPARATOR'))
        indices = header.index(get_key_value('POSTALCODE')),\
            header.index(get_key_value('OFFICENAME')),\
            header.index(get_key_value('POSX')),\
            header.index(get_key_value('POSY')),
        isheader = True
        for line in filecontent:
            linecontent = line.split(get_key_value('DATASEPARATOR'))
            if len(linecontent) < max(indices):
                break
            if isheader is True:
                isheader = False
                continue
            dataline = []
            dataline.append(int(linecontent[indices[0]]))
            dataline.append(linecontent[indices[1]])
            dataline.append(float(linecontent[indices[2]].replace(
                get_key_value('FLOATSEPARATOR'), '.')))
            dataline.append(float(linecontent[indices[3]].replace(
                get_key_value('FLOATSEPARATOR'), '.')))
            data.append(dataline)
        return data


def get_key_value(key):
    keywords = []
    with open('keywords.txt', encoding='utf-8') as file:
        filecontent = file.read().split("\n")
        for line in filecontent:
            keypair = line.split('=')
            if not keypair[0] == '':
                keywords.append(keypair)
        for item in keywords:
            if item[0] == key:
                return item[1]
        return

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 11:06:14 2022

@author: Владислав
"""

import sqlite3 as sq
import csv
import os

def create_table_comments():
    conn = sq.connect(keyval('DBNAME'))
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS Comments')
    conn.commit()
    command = 'CREATE TABLE Comments(MarketID INTEGER NULL, PersonName TEXT NULL, Comment TEXT NULL, Rating INTEGER NULL)'
    cur.execute(command)
    conn.commit()
    conn.close()


def fill_table_comments():
    conn = sq.connect(keyval('DBNAME'))
    cur = conn.cursor()
    with open(keyval('COMMENTSFILENAME'), encoding=keyval('COMMENTSENCODING')) as file:
        filecontent = file.read().split("\n")
        isheader = True
        for line in filecontent:
            linecontent = line.split('\t')
            if len(linecontent) < 1:
                break
            if isheader is True:
                isheader = False
                continue
            command = f"""INSERT INTO Comments VALUES ({int(linecontent[0])}, '{linecontent[1]}', '{linecontent[2]}', {int(linecontent[3])});"""
            cur.execute(command)
            conn.commit()
    conn.close()


# Создает таблицу Markets, возвращает лист с названиями заголовков
def create_table_markets():
    conn = sq.connect(keyval('DBNAME'))
    cur = conn.cursor()
    command = ''
    with open(keyval('FILENAME'), encoding=keyval('ENCODING')) as file:
        filecontent = file.read().replace('"', "'").split("\n")
        # filecontent[0] - table header
        header = filecontent[0].split(keyval('DATASEPARATOR'))
        header = list(map(str.strip, header))
        # Creating table
        cur.execute('DROP TABLE IF EXISTS Markets')
        cur.execute(command)
        conn.commit()
        command = 'CREATE TABLE Markets(FMID INTEGER PRIMARY KEY,'
        for n in range(1, 11):
            command += f'{header[n]} TEXT NULL,'
        command += f'{header[11]} INT NULL,'
        for n in range(12, 20):
            command += f'{header[n]} TEXT NULL,'
        command += f'{header[20]} FLOAT, {header[21]} FLOAT,'
        command += f'{header[22]} TEXT NULL,'
        for n in range(23, 58):
            command += f'{header[n]} TEXT NULL,'
        command += f'{header[58]} TEXT NULL);'
        cur.execute(command)
        conn.commit()
        conn.close()
    # Fill table
    fill_table_markets(header)


def fill_table_markets(header):
    conn = sq.connect(keyval('DBNAME'))
    cur = conn.cursor()
    with open(keyval('FILENAME'), encoding=keyval('ENCODING')) as file:
        filecontent = file.read().replace('"', "'")
        with open('tmpcontent.csv', 'w', encoding=keyval('ENCODING')) as target:
            target.write(filecontent)
    with open('tmpcontent.csv', encoding=keyval('ENCODING')) as file:
        reader = csv.DictReader(file)
        # print(header)
        # for row in reader:
        #     print(row[f'{header[1]}'])
        for row in reader:
            command = ''
            command = f"""INSERT INTO Markets VALUES ({int(row[f"{header[0]}"])},"""
            for n in range(1, 11):
                command += f""""{str(row[f"{header[n]}"])}","""
            try:
                command += f"""{int(row[f"{header[11]}"])},"""
            except Exception as e:
                # print('Some data is corrupted, ignoring')
                command += """"","""
            for n in range(12, 20):
                command += f""""{str(row[f"{header[n]}"])}","""
            try:
                command += f"""{float(row[f"{header[20]}"])},{float(row[f"{header[21]}"])},"""
            except Exception as e:
                # print('Some data is corrupted, ignoring')
                command += """"","","""
            command += f""""{str(row[f"{header[22]}"])}","""
            for n in range(23, 58):
                command += f""""{str(row[f"{header[n]}"])}","""
            command += f""""{str(row[f"{header[58]}"])}");"""
            # print(command)
            cur.execute(command)
            conn.commit()
        conn.close()
    os.remove('tmpcontent.csv')


# Функция возвращает значение из файла, связанное с ключом
def keyval(key):
    keywords = []
    with open('import_keywords.txt', encoding='utf-8') as file:
        filecontent = file.read().split("\n")
        for line in filecontent:
            keypair = line.split('=')
            if not keypair[0] == '':
                keywords.append(keypair)
        for item in keywords:
            if item[0] == key:
                return item[1]
        return


if __name__ == '__main__':
    print('Creating DB...')
    create_table_markets()
    create_table_comments()
    fill_table_comments()
    print('DB created! You can run application now')
    input('Press any key...')
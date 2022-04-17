# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 09:44:04 2022

@author: Владислав
"""

import sqlite3

conn = sqlite3.connect('orders.db')
# conn = sqlite3.connect(r'ПУТЬ-К-ПАПКИ/orders.db'
# conn = sqlite3.connect(:memory:) - создание бд в памяти
# Создаем курсор
cur = conn.cursor()
# Далее при помощи курсора выполняем запросы
#cur.execute("ВАШ-SQL-ЗАПРОС-ЗДЕСЬ;")
cur.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INT PRIMARY KEY,
   fname TEXT,
   lname TEXT,
   gender TEXT);
""")
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS orders(
   orderid INT PRIMARY KEY,
   date TEXT,
   userid TEXT,
   total TEXT);
""")
conn.commit()

cur.execute("""INSERT INTO users(userid, fname, lname, gender) 
   VALUES('00001', 'Alex', 'Smith', 'male');""")
conn.commit()
user = ('00002', 'Lois', 'Lane', 'Female')
cur.execute("INSERT INTO users VALUES(?, ?, ?, ?);", user)
conn.commit()
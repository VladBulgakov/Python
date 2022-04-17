# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 12:31:11 2022

@author: Владислав
"""


import confreader as cr
import sqlite3 as sq
import csv
import math
from geopy.distance import geodesic


class MarketInstance:
    # Класс 'ярмарка': строка из таблицы Markets
    def __init__(self, markets_table_record = [None for x in range(0,22)]):
        self.FMID = markets_table_record[0]
        self.MarketName = markets_table_record[1]
        self.Website = markets_table_record[2]
        self.Facebook = markets_table_record[3]
        self.Twitter = markets_table_record[4]
        self.Youtube = markets_table_record[5]
        self.Street = markets_table_record[7]
        self.City = markets_table_record[8]
        self.Country = markets_table_record[9]
        self.State = markets_table_record[10]
        self.zip = markets_table_record[11]
        self.x = markets_table_record[20]
        self.y = markets_table_record[21]
    
    def __str__(self):
        return f'Market instance {self.FMID}: {self.MarketName}'

class CommentInstance:
    # Класс 'комментарий'
    def __init__(self, comments_table_record = [None for x in range(0,5)]):
        self.MarketID = comments_table_record[0]
        self.PersonName = comments_table_record[1]
        self.Comment = comments_table_record[2]
        self.Rating = comments_table_record[3]
        self.CommentID = comments_table_record[4]
    
    def __str__(self):
        return f'Comment instance {self.CommentID} for market {self.MarketID}: {self.Comment}'


def LoadMarketComments(market_instance):
    conn = sq.connect(cr.keyval('DBNAME'))
    cur = conn.cursor()
    command = f'SELECT MarketID, PersonName, Comment, Rating, Comments.rowid FROM Comments JOIN Markets ON Comments.MarketID = Markets.FMID WHERE Markets.FMID = {market_instance.FMID};'
    cur.execute(command)
    records = cur.fetchall()
    #conn.commit()
    conn.close()
    comments = [CommentInstance(x) for x in records]
    # for item in comments:
        # print(item)
    return comments

def GetMarketAvgRating(market_instance):
    conn = sq.connect(cr.keyval('DBNAME'))
    cur = conn.cursor()
    command = f'SELECT AVG(Rating) FROM Markets JOIN Comments ON Comments.MarketID = Markets.FMID WHERE Markets.FMID = {market_instance.FMID};'
    cur.execute(command)
    value = cur.fetchone()
    #conn.commit()
    conn.close()
    avgr = float(value[0]) if value[0] else None
    return avgr

def DeleteMarketInstance(market_instance):
    conn = sq.connect(cr.keyval('DBNAME'))
    cur = conn.cursor()
    command = f'DELETE FROM Markets WHERE Markets.FMID = {market_instance.FMID};'
    cur.execute(command)
    conn.commit()
    conn.close()

def AddCommentInstance(comment_instance):
    conn = sq.connect(cr.keyval('DBNAME'))
    cur = conn.cursor()
    command = f'INSERT INTO Comments VALUES ({comment_instance.MarketID}, "{comment_instance.PersonName}", "{comment_instance.Comment}", "{comment_instance.Rating}");'
    cur.execute(command)
    conn.commit()
    conn.close()
    
def DeleteCommentInstance(comment_instance):
    conn = sq.connect(cr.keyval('DBNAME'))
    cur = conn.cursor()
    command = f'DELETE FROM Comments WHERE Comments.rowid = {comment_instance.CommentID};'
    cur.execute(command)
    conn.commit()
    conn.close()

def LoadMarketsList(search_text = '',
                    search_field = 'MarketName',
                    sorting_field = 'FMID',
                    sorting_direction = 'ASC',
                    page=1, pagesize=20,
                    search_range=None,
                    userxy=[cr.keyval('USERPOSX'), cr.keyval('USERPOSY')]):
    if sorting_field == 'Rating':
        sorting_field = 'AVG(COALESCE(Rating,0))'

    conn = sq.connect(cr.keyval('DBNAME'))
    cur = conn.cursor()

    # Убираем из выборки ярмарки, которые не попадают в радиус поиска, 
    # если радиус задан:
    if search_range is None:
        command = 'SELECT FMID FROM Markets;'
        cur.execute(command)
        records_iter1 = [int(x[0]) for x in cur.fetchall()]
    else:
        command = 'SELECT FMID,x,y FROM Markets;'
        cur.execute(command)
        records = cur.fetchall()
        # Убираем записи, в которых нет x или y:
        tmp = [x for x in records if x[1] != '' and x[2] != '']
        # Получаем лист int с идентификаторами нужных нам ярмарок
        records_iter1 = [int(x[0]) for x in tmp if distance(userxy,x[1:3]) <= search_range]

    # Получаем лист ID записей, которые удовлетворяют требованию радиуса,
    # если таковое было. records_iter1

    tmp = '('
    for item in records_iter1:
        tmp += str(item) + ','
    ids = tmp[:-1] + ')'

    command = f'SELECT * FROM Markets LEFT JOIN Comments ON Markets.FMID = Comments.MarketID WHERE Markets.FMID IN {ids} '
    if search_text != '':
        command += f'AND {search_field} LIKE "%{search_text}%" COLLATE NOCASE '
    command += f'GROUP BY Markets.FMID ORDER BY {sorting_field} {sorting_direction} LIMIT {pagesize} OFFSET {pagesize*(page-1)};'
    # Если в радиусе ничего не оказалось, то критерий нужно удалить из строки:
    if len(records_iter1) == 0:
        command = command.replace(f'Markets.FMID IN {ids}', '1=0')

    cur.execute(command)
    records = cur.fetchall()
    conn.close()
    markets = [MarketInstance(x[:22]) for x in list(records)]
    return markets


def distance(uxy, mxy):
    ucoord = list(map(float, [uxy[1], uxy[0]]))
    mcoord = list(map(float, [mxy[1], mxy[0]]))
    return geodesic(ucoord, mcoord).km


if __name__ == '__main__':
    markets = LoadMarketsList(search_text='Market',
                                    search_field='MarketName',
                                    sorting_field='FMID',
                                    sorting_direction='ASC',
                                    page=1,
                                    search_range=150)
    for item in markets:
        print(item)
    
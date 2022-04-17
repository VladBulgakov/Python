# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 14:04:39 2022

@author: Владислав
"""

import tkinter as tk
import datalayer as dal
import confreader as cr


class MarketItemDetailed(tk.Frame):
    def __init__(self, parent, controller, market_instance):
        tk.Frame.__init__(self, parent)
        
        name = tk.Label(self, text=f'{market_instance.MarketName}')
        state = tk.Label(self, text=f'State: {market_instance.State}')
        country = tk.Label(self, text=f'Country: {market_instance.Country}')
        city = tk.Label(self, text=f'City: {market_instance.City}')
        street = tk.Label(self, text=f'Street: {market_instance.Street}')
        zipcode = tk.Label(self, text=f'zip: {market_instance.zip}')
        geos = tk.Label(self, text=f'Geo coordinates: x = {market_instance.x}, y = {market_instance.y}')

        self.grid_columnconfigure(0, weight=1)

        name.grid(row=0, column=0, padx=10, pady=5, sticky='ew')
        state.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        country.grid(row=2, column=0, padx=10, pady=5, sticky='w')
        city.grid(row=3, column=0, padx=10, pady=5, sticky='w')
        street.grid(row=4, column=0, padx=10, pady=5, sticky='w')
        zipcode.grid(row=5, column=0, padx=10, pady=5, sticky='w')
        geos.grid(row=6, column=0, padx=10, pady=5, sticky='w')


class MarketItemSmall(tk.Frame):
    def __init__(self, parent, controller, market_instance):
        tk.Frame.__init__(self, parent, relief='solid', borderwidth=2)

        label = tk.Label(self, text=f'{market_instance.MarketName}')
        btn_more = tk.Button(self, text='Подробности', command=lambda: controller.show_details(market_instance))
        btn_del = tk.Button(self, text='Удалить', command=lambda: controller.remove_market(market_instance))

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=0)
        self.grid_columnconfigure(3, weight=0)

        label.grid(row=0, column=0, padx=10, pady=5, sticky='w')
        if cr.keyval('ADMIN') == 'YES':
            btn_del.grid(row=0, column=1, padx=10, sticky='ew')
        btn_more.grid(row=0, column=2, padx=10, sticky='ew')
        rating = dal.GetMarketAvgRating(market_instance)
        lbl_rating = tk.Label(self, text=stars(rating))
        lbl_rating.grid(row=0, column=3, padx=10, sticky='e')


class MarketItemList(tk.Frame):
    def __init__(self, parent, controller, market_list):
        tk.Frame.__init__(self, parent)
        i = 0
        for item in market_list:
            market = MarketItemSmall(self, controller, item)
            market.grid(row=i, column=0, pady=5, sticky='ew')
            i += 1


class CommentItem(tk.Frame):
    def __init__(self, parent, controller, comment_instance):
        tk.Frame.__init__(self, parent, relief='solid', borderwidth=1)

        title = tk.Label(self, text=f'{comment_instance.PersonName}')
        rating = tk.Label(self, text=stars(comment_instance.Rating))
        text = tk.Text(self, height=5)
        text.insert('1.0',f'{comment_instance.Comment}')
        btn_del = tk.Button(self, text='Удалить', command=lambda: controller.remove_comment(comment_instance))

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=0)

        title.grid(row=0, column=0, padx=10, pady=5, sticky='w')
        text.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        rating.grid(row=0, column=1, padx=10, pady=5, sticky='e')
        if cr.keyval('ADMIN') == 'YES':
            btn_del.grid(row=1, column=1, padx=10, sticky='e')


class CommentItemList(tk.Frame):
    def __init__(self, parent, controller, comment_list):
        tk.Frame.__init__(self, parent)
        i = 0
        for item in comment_list:
            comment = CommentItem(self, controller, item)
            comment.grid(row=i, column=0, pady=5, sticky='ew')
            i += 1

def stars(val):
    st = ''
    if val is not None:
        for i in range(0,round(val)):
            st += '\u2605'
        for i in range(round(val),5):
            st += '\u2606'  
    else:
        st = '\u2606\u2606\u2606\u2606\u2606'
    return st
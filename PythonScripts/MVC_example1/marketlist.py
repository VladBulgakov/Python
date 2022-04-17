# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 12:34:12 2022

@author: Владислав
"""

import tkinter as tk
import datalayer as dal


class MarketItem(tk.Frame):
    def __init__(self, parent, controller, content):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=f'Shop: {content}')
        button = tk.Button(self, text='Подробности', command=lambda: controller.btntest(content))
        label.pack(padx=5, pady=5, side=tk.LEFT)
        button.pack(padx=5, pady=5, side=tk.RIGHT)
        


class MarketList(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)    
        data = dal.GetShopStrList()
        i = 0
        for item in data:
            shop = MarketItem(self, controller, item)
            shop.grid(row=i, column=0)
            i += 1
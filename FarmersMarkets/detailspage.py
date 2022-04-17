# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 08:05:59 2022

@author: Владислав
"""

import tkinter as tk
from tkinter import ttk
import mainpage as mp
import datalayer as dal
import views as v


class DetailsPage(tk.Frame):
    def __init__(self, parent, controller, *market_instance):
        tk.Frame.__init__(self, parent)
        tk.Frame.grid_columnconfigure(self, 0, weight=1)
        tk.Frame.grid_rowconfigure(self, 1, weight=1)
        self.controller = controller
        self.market_instance = market_instance if market_instance else None
        self.rating_options = (0, 1, 2, 3, 4, 5)
        self.user_rating = tk.StringVar(self)
        self.user_rating.set('Выберите оценку...')

    def details(self, market_instance):
        self.market_instance = market_instance
        # label = tk.Label(master=self, text=self.market_instance.MarketName)
        # label.pack(pady=20, padx=20)
        mid = v.MarketItemDetailed(self, self.controller, market_instance)
        mid.grid(row=0, column=0, columnspan=2, sticky='ew')

        # Поле комментариев
        outer_com_frame = tk.Frame(self, relief=tk.RIDGE, borderwidth=5)
        outer_com_frame.grid(row=1, column=0, columnspan=2, sticky='nsew')
        com_canvas = tk.Canvas(master=outer_com_frame)
        com_scrollbar_y = tk.Scrollbar(master=outer_com_frame, orient=tk.VERTICAL, command=com_canvas.yview)
        com_scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        com_canvas.configure(yscrollcommand=com_scrollbar_y.set)
        com_canvas.bind('<Configure>', lambda e: com_canvas.configure(scrollregion = com_canvas.bbox('all')))
        com_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        # Фрейм на холсте
        self.comments_frame = tk.Frame(master=com_canvas)
        com_canvas.create_window((0,0), window=self.comments_frame, anchor='nw')
        #Список комментариев в поле с прокруткой
        self.comment_list(self.controller)

        #Поле для комментария пользователя
        self.usrcom = tk.Label(self, text=f'Оставьте комментарий')
        self.uname_field = tk.Entry(self, text=f'Имя')
        self.utext_field = tk.Text(self, height=5)
        self.rating_dropdown = tk.OptionMenu(self,
                                             self.user_rating,
                                             *self.rating_options)
        ubtn_send = tk.Button(self, text='Отправить', command=lambda: self.make_comment())

        self.usrcom.grid(row=3, column=0, columnspan=2, sticky='w')
        self.uname_field.grid(row=4, column=0, padx=5, columnspan=1, sticky='w')
        self.rating_dropdown.grid(row=4, column=1, columnspan=1, sticky='ew')
        self.utext_field.grid(row=5, column=0, padx=5, columnspan=1, sticky='ew')
        ubtn_send.grid(row=5, column=1, padx=5, columnspan=1, sticky='ew')
        # Кнопка перехода в главное окно
        btn1 = ttk.Button(master=self, text='На главную',
                          command=lambda: self.controller.show_frame(mp.MainPage))
        btn1.grid(row=6, column=0, columnspan=2, sticky='ew')

    def comment_list(self, controller):
        for content in self.comments_frame.winfo_children():
            content.destroy()
        comments = dal.LoadMarketComments(self.market_instance)
        clist = v.CommentItemList(self.comments_frame, controller, comments)
        clist.pack(side='top', fill='both', expand='true')

    def make_comment(self):
        if self.uname_field.get() == '':
            self.usrcom['text']='Пожалуйста, представьтесь'
            return
        if self.user_rating.get() == 'Выберите оценку...':
            self.usrcom['text']='Пожалуйста, укажите оценку'
            return
        comment = dal.CommentInstance()
        comment.MarketID = self.market_instance.FMID
        comment.PersonName = self.uname_field.get()
        comment.Comment = self.utext_field.get(1.0, "end-1c")
        comment.Rating = int(self.user_rating.get())
        self.controller.add_comment(comment)

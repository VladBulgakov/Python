# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 09:40:11 2022

@author: Владислав
"""

import confreader as cr
import tkinter as tk
import mainpage as mp
import detailspage as dp
import datalayer as dal
import logging


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self, default='clienticon.ico')
        tk.Tk.wm_title(self, 'Farmers Markets')
        tk.Tk.wm_minsize(self, 1000, 600)

        container = tk.Frame(master=self)
        container.pack(side='top', fill='both', expand='true')
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Cловарь со страницами приложения
        self.frames = {}
        for F in (mp.MainPage, dp.DetailsPage):
            # master для страницы - фрейм-контейнер
            # ее контроллер - self, то есть приложения
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(mp.MainPage)

    def show_frame(self, fr):
        frame = self.frames[fr]
        frame.tkraise()

    def show_details(self, market_instance):
        self.frames[dp.DetailsPage].details(market_instance)
        self.show_frame(dp.DetailsPage)
        logging.info(f'Подробности о {market_instance}')

    def remove_market(self, market_instance):
        dal.DeleteMarketInstance(market_instance)
        self.frames[mp.MainPage].market_list(self)
        logging.info(f'Ярмарка {market_instance} удалена')
    
    def remove_comment(self, comment_instance):
        dal.DeleteCommentInstance(comment_instance)
        self.frames[dp.DetailsPage].comment_list(self)
        self.frames[mp.MainPage].market_list(self)
        logging.info(f'Комментарий {comment_instance} удален')
        
    def add_comment(self, comment_instance):
        dal.AddCommentInstance(comment_instance)
        self.frames[dp.DetailsPage].comment_list(self)
        self.frames[mp.MainPage].market_list(self)
        logging.info(f'Комментарий {comment_instance} добавлен')

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
                        datefmt='%d.%m.%Y %H:%M:%S',
                        filename='log.txt', encoding='utf-8',
                        level=logging.DEBUG, filemode='w')
    logging.debug('Приложение запущено')
    app = Application()
    app.mainloop()

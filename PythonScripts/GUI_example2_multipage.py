# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 09:40:11 2022

@author: Владислав
"""

import tkinter as tk
from tkinter import ttk


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self, default='clienticon.ico')
        tk.Tk.wm_title(self, 'Farmers Markets')
        tk.Tk.wm_minsize(self, 800, 600)

        container = tk.Frame(master=self)
        container.pack(side='top', fill='both', expand='true')
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}  # Cловарь с фреймами
        for F in (MainPage, DetailsPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(master=self, text='Main page')
        label.pack(pady=20, padx=20)
        # Нужно использовать lambda, так как если писать напрямую
        # command = controller.show_frame(DetailsPage) произойдет вызов
        # метода show_frame с аргументом, которого не существует
        btn1 = tk.Button(master=self, text='Show details',
                         command=lambda: controller.show_frame(DetailsPage))
        btn1.pack()


class DetailsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(master=self, text='Details page')
        label.pack(pady=20, padx=20)
        btn1 = ttk.Button(master=self, text='Go to main',
                         command=lambda: controller.show_frame(MainPage))
        btn1.pack()

def entry():
    app = Application()
    app.mainloop()


if __name__ == '__main__':
    entry()
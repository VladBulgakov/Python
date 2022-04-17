# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 17:11:33 2022

@author: Владислав
"""

import tkinter as tk

window = tk.Tk()
fr = tk.Frame(master=window, relief = tk.RIDGE, borderwidth=5)
entfield = tk.Entry(master=fr, foreground='red', width=50)
entfield.insert(0,'hi')
entfield.pack()
for i in range(0,10):
    lbl = tk.Label(master=fr, text=f'Label {i}')
    lbl.pack(side=tk.TOP)
fr.grid(column=0, row=0, sticky=tk.EW)
scrbar = tk.Scrollbar(master=window, orient=tk.VERTICAL)
scrbar.grid(column=1, row=0, sticky=tk.NS)
#scrollbar binding
window.config(yscrollcommand=scrbar.set)
window.mainloop()
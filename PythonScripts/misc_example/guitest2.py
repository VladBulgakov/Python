# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 13:38:35 2022

@author: Владислав
"""

import tkinter as tk
 
window = tk.Tk()
window.columnconfigure(0, weight=1, minsize=150)
window.rowconfigure(0, weight=1, minsize=150)
for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        #frame.grid(row=i, column=j, padx=5, pady=10) #отступы от фрейма (между ними), sticky - привязка (n,w,s,e)
        frame.grid(row=i, column=j, sticky="nsew")
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack(padx=20, pady=20) #отступы от лейбла до краев фрейма
 
window.mainloop()
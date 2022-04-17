# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 13:34:16 2022

@author: Владислав
"""

import tkinter as tk
 
window = tk.Tk()
 
for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()
 
window.mainloop()
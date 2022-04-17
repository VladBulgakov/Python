# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 14:59:24 2022

@author: Владислав
"""


import tkinter as tk
 
window = tk.Tk()
window.title("Простой текстовый редактор")
 
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
 
txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window)
btn_open = tk.Button(fr_buttons, text="Открыть")
btn_save = tk.Button(fr_buttons, text="Сохранить как...")
 
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
 
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")
 
window.mainloop()
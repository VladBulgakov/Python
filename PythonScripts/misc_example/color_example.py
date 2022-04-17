# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 16:43:29 2022

@author: Владислав
"""

from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x300')
ws.config(bg='#F26849')

def change_color(choice):
    choice = variable.get()
    ws.config(bg=choice)


# color choices available.
color_list = ['red', 'green', 'yellow', 'blue', 'pink']

# setting variable for Integers
variable = StringVar()

# creating widget
dropdown = OptionMenu(
    ws,
    variable,
    *color_list,
    command=change_color
)
# positioning widget
dropdown.pack(expand=True)

# infinite loop 
ws.mainloop()
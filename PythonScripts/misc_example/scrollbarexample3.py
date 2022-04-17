# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 18:01:04 2022

@author: Владислав
"""

import tkinter as tk

# creating and placing scrollbar
sb = Scrollbar(
    ws,
    orient=VERTICAL
)
sb.pack()


# binding scrollbar with other widget (Text, Listbox, Frame, etc)

<other_widget>.config(yscrollcommand=sb.set)
sb.config(command=<other_widget>.yview)
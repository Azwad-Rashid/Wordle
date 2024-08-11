'''Creates and places a series of labels'''

import tkinter as tk

from custom_font import custom_font
from custom_color import custom_color as colors

def end_labels(master: tk.Frame, labels: list[str], start: int = 0) -> None:
    '''Creates and places a series of labels
    
    :param master: The frame in which the labels are to be placed
    :type master: tk.Frame
    :param labels: A list of labels to place onto the master
    :type labels: list[str]
    :param start: The starting row number
    :type start: int 
    
    :rtype: None
    '''

    for row, label in enumerate(labels, start):
        tk.Label(
            master=master,
            text=label,
            width=30,
            font=custom_font(15),
            foreground=colors("white"),
            background=colors("background")
        ).grid(
            row=row,
            column=0,
            padx=5,
            pady=5
        )

def color_labels(master: tk.Frame, color_list: list[str], label_list: list[str], start: int) -> None:
    '''Creates and places the info for colors

    :param master: The frame in which the labels are to be placed
    :type master: tk.Frame
    :param color_list: A list of colors to place onto the master
    :type color_list: list[str]
    :param label_list: A list of labels containing info about the corresponding color
    :type label_list: list[str] 
    :param start: The starting row number
    :type start: int 
    '''

    for i in range(len(color_list)):
        tk.Label(
            master=master,
            text=" " * 5, # Five spaces make the color boxes be square for some reason
            background=colors(color_list[i]),
            highlightcolor=colors("white"),
            highlightthickness=2 # Arbitrary number for the looks
        ).grid(row=start + i, column=0, padx=5, pady=5, sticky="e")
        tk.Label(
            master=master,
            text=label_list[i],
            font=custom_font(10),
            foreground=colors("white"),
            background=colors("background")
        ).grid(row=start + i, column=1, padx=5, pady=5, sticky="w")
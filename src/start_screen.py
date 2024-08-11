'''Creates the starting screen for the game'''

import tkinter as tk

from WORDLE import WORDLE
from create_labels import color_labels
from custom_color import custom_color as colors
from custom_font import custom_font

def create_start_menu(master: WORDLE) -> None:
    '''Creates the start menu
    
    Components
    ----------
    - Intro & rules
    - Color descriptions
    - How to start'''

    add_title(master)

    add_intro(master)



def add_title(master: WORDLE) -> None:
    '''Adds the introductory info of the app

    :param master: The root widget
    :type master: WORDLE
    :param font: The font style to be used in the title
    :type font: Font
    :param colors: A dict containing the colours for the title
    :type colors: dict[str, str]
    
    Information added
    ---------------------
    - Name of the game, i.e, "WORDLE"
    - Name of the author (maybe)
    '''

    # The name of the game
    title = tk.Label(
        master=master,
        text="WORDLE",
        width=10,
        font=custom_font(50),
        foreground="#ffffff",
        background=colors("green")
    )
    title.grid(
        row=0,
        column=0,
        columnspan=2,
        padx=5,
        pady=5,
        sticky="ew"
    )

    master.widgets["title"] = title

def add_intro(master: WORDLE) -> None:
    '''Adds the introductory info of the app

    :param master: The root widget
    :type master: WORDLE
    :param font: The font style to be used in the title
    :type font: Font
    :param colors: A dict containing the colours for the title
    :type colors: dict[str, str]
    '''

    intro_frame: tk.Frame = tk.Frame(master, background=colors("background"))
    tk.Label(
        master=intro_frame,
        text="Guess the word in 6 or fewer tries",
        width=30,
        font=custom_font(15),
        foreground=colors("white"),
        background=colors("background"),
    ).grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    color_info = [
        "=> It's in the correct position",
        "=> It's in the wrong position",
        "=> It's not in the word",
        "=> It's not a valid word",
    ]
    color_labels(
        master=intro_frame,
        color_list=["green", "yellow", "grey", "red"],
        label_list=color_info,
        start=1
    )

    tk.Label(
        master=intro_frame,
        text="Press <SPACE> to start the game",
        width=30,
        font=custom_font(15),
        foreground=colors("white"),
        background=colors("background"),
    ).grid(row=len(color_info) + 1, column=0, columnspan=2, padx=5, pady=5)


    intro_frame.grid(row=1, column=0)

    master.widgets["frame"] = intro_frame

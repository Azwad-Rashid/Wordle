'''Creates the starting screen for the game'''

import tkinter as tk
from tkinter import font

from WORDLE import WORDLE
from load_config import config_data

def create_start_menu(master: WORDLE) -> None:
    
    # Gets the required config data to create widgets
    widget_font = font.Font(
        master=master,
        font=(config_data["WIDGETS"].get("font_family", "Arial"), config_data["WIDGETS"]["font_size"], "normal")
    )
    widget_hex: dict[str, str] = {
        "background": config_data["WINDOW"]["background"],
        "black": config_data["COLORS"]["black"],
        "grey": config_data["COLORS"]["grey"],
        "yellow": config_data["COLORS"]["yellow"],
        "green": config_data["COLORS"]["green"],
        "red": config_data["COLORS"]["red"]
    }

    add_title(master, widget_font, widget_hex)

    add_intro(master, widget_font, widget_hex)



def add_title(master: WORDLE, font: font.Font, colors: dict[str, str]) -> None:
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

    # Frame to contain the info
    title_frame = tk.Frame(
        master=master,
        background=colors["green"]
    )

    # The name of the game
    title_font = font.copy()
    title_font.config(weight="bold", size=50)
    tk.Label(
        master=title_frame,
        text=config_data["GENERAL"].get("app_name", "WORDLE"),
        width=10,
        font=title_font,
        foreground="#ffffff",
        background=colors["green"]
    ).grid(
        row=0,
        column=0,
        columnspan=2,
        sticky="ew"
    )

    title_frame.grid(
        row=0,
        column=0,
        sticky="ew",
        padx=5,
        pady=5
    )

    master.widgets["title"] = title_frame

def add_intro(master: WORDLE, font: font.Font, colors: dict[str, str]) -> None:
    '''Adds the introductory info of the app

    :param master: The root widget
    :type master: WORDLE
    :param font: The font style to be used in the title
    :type font: Font
    :param colors: A dict containing the colours for the title
    :type colors: dict[str, str]
    '''

    intro_font = font.copy()

    intro_font.config(size=15)
    intro_frame: tk.Frame = tk.Frame(master, background=colors["background"])
    tk.Label(
        master=intro_frame,
        text="Guess the word in 6 or fewer tries",
        width=30,
        font=intro_font,
        foreground="#ffffff",
        background=colors["background"],
    ).grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Colors description
    desc_font = font.copy()
    desc_font.config(size=10)

    # Green desc
    tk.Label(
        master=intro_frame,
        text="     ",
        background=colors["green"],
        highlightcolor="#ffffff",
        highlightthickness=2
    ).grid(row=1, column=0, padx=5, pady=5, sticky="e")
    tk.Label(
        master=intro_frame,
        text="=> It's in the correct position",
        font=desc_font,
        background=colors["background"],
        foreground="#ffffff"
    ).grid(row=1, column=1, padx=5, pady=5, sticky="w")

    # Yellow desc
    tk.Label(
        master=intro_frame,
        text="     ",
        background=colors["yellow"],
        highlightcolor="#ffffff",
        highlightthickness=2
    ).grid(row=2, column=0, padx=5, pady=5, sticky="e")
    tk.Label(
        master=intro_frame,
        text="=> It's in the wrong position",
        font=desc_font,
        background=colors["background"],
        foreground="#ffffff"
    ).grid(row=2, column=1, padx=5, pady=5, sticky="w")

    # Grey desc
    tk.Label(
        master=intro_frame,
        text="     ",
        background=colors["grey"],
        highlightcolor="#ffffff",
        highlightthickness=2
    ).grid(row=3, column=0, padx=5, pady=5, sticky="e")
    tk.Label(
        master=intro_frame,
        text="=> It's not in the word",
        font=desc_font,
        background=colors["background"],
        foreground="#ffffff"
    ).grid(row=3, column=1, padx=5, pady=5, sticky="w")

    # Red desc
    tk.Label(
        master=intro_frame,
        text="     ",
        background=colors["red"],
        highlightcolor="#ffffff",
        highlightthickness=2
    ).grid(row=4, column=0, padx=5, pady=5, sticky="e")
    tk.Label(
        master=intro_frame,
        text="=> It's not a valid word",
        font=desc_font,
        background=colors["background"],
        foreground="#ffffff"
    ).grid(row=4, column=1, padx=5, pady=5, sticky="w")

    tk.Label(
        master=intro_frame,
        text="Press <SPACE> to start!",
        width=30,
        font=intro_font,
        foreground="#ffffff",
        background=colors["background"],
    ).grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    intro_frame.grid(row=1, column=0)

    master.widgets["frame"] = intro_frame

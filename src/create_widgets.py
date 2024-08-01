'''Module used to create the necessary elements in the master window of WORDLE'''

import tkinter as tk
from tkinter import font

from WORDLE import WORDLE
from load_config import config_data

def create_widgets(master: WORDLE) -> None:
    '''Creates widgets for WORDLE

    :param master: The master or root widget of the tkinter application
    :type master: Tk
    :rtype: None
    '''

    # Gets the required config data to create widgets
    widget_font = font.Font(
        master=master,
        font=(config_data["WIDGETS"].get("font_family", "Arial"), config_data["WIDGETS"]["font_size"], "normal")
    )
    widget_hex: dict[str, str] = {
        "black": config_data["WIDGETS"]["black"],
        "grey": config_data["WIDGETS"]["grey"],
        "yellow": config_data["WIDGETS"]["yellow"],
        "green": config_data["WIDGETS"]["green"]
    }

    # TODO: Add the name on top as the title
    add_title(master, widget_font, widget_hex)
    # TODO: Add the board and its tiles
    # TODO: Add the keyboard










def add_title(master: WORDLE, font: font.Font, colors: dict[str, str]) -> None:
    '''Adds the introductory info of the app

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
    game_name = tk.Label(
        master=title_frame,
        text=config_data["GENERAL"].get("app_name", "WORDLE"),
        width=10,
        font=title_font,
        foreground="#ffffff",
        background=colors["green"]
    )
    game_name.grid(
        row=0,
        column=0,
        columnspan=2,
        sticky="ew"
    )

    # The author name
    author_name = tk.Label(
        master=title_frame,
        text=f"by {config_data["GENERAL"]["author"].split(" ")[0]}",
        font=font,
        foreground="#ffffff",
        background=colors["green"]
    )
    author_name.grid(
        row=1,
        column=1,
        sticky="e"
    )

    title_frame.grid(
        row=0,
        column=0,
        sticky="ew",
        padx=5,
        pady=5
    )




if __name__ == "__main__":
    root = tk.Tk()

    create_widgets(root)

    root.mainloop()
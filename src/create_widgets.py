'''Module used to create the necessary elements in the master window of WORDLE'''

import tkinter as tk
from tkinter import font

from WORDLE import WORDLE
from load_config import config_data

def create_widgets(master: WORDLE) -> None:
    '''Creates widgets for WORDLE

    :param master: The main widget of the app
    :type master: WORDLE
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

    # Add the name on top as the title
    add_title(master, widget_font, widget_hex)

    # Add the board and its tiles
    add_board(master, widget_font, widget_hex)

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

    title_frame.grid(
        row=0,
        column=0,
        sticky="ew",
        padx=5,
        pady=5
    )

    master.widgets["frames"].append(title_frame)

def add_board(master: WORDLE, font: font.Font, colors: dict[str, str]) -> None:
    '''Adds the playing board of the app

    :param font: The font style to be used in the title
    :type font: Font
    :param colors: A dict containing the colours for the title
    :type colors: dict[str, str]
    
    A 5x6 board is created in the window
    - The 6 rows represents the 6 tries the player has to guess the word
    - The 5 columns will each contain a letter of the player's guesses
    '''

    board_frame: tk.Frame = tk.Frame(
        master=master,
        background=colors["black"]
    )

    for row in range(6):
        for column in range(5):
            board_tile = tk.Label(
                master=board_frame,
                background=colors["black"],
                foreground="#ffffff",
                text=" ",
                font=font,
                highlightbackground=colors["grey"],
                highlightthickness=2,
                height=1, # Set it to 1 arbitrarily, seemed to work (idk why)
                width=4 # Set it to 4 arbitrarily, seemed to work (idk why)
            )
            
            board_tile.grid(
                row=row,
                column=column,
                padx=5,
                pady=5,
                sticky="ew"
            )

            master.widgets["board"][row].append(board_tile)

    board_frame.grid(
        row=1,
        column=0
    )

    master.widgets["frames"].append(board_frame)



if __name__ == "__main__":
    root = tk.Tk()

    create_widgets(root)

    root.mainloop()
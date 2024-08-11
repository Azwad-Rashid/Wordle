'''Module used to create the necessary elements in the master window of WORDLE'''

import tkinter as tk

from WORDLE import WORDLE
from custom_color import custom_color
from custom_font import custom_font

def create_widgets(master: WORDLE) -> None:
    '''Creates widgets for WORDLE

    :param master: The main widget of the app
    :type master: WORDLE
    '''

    # Add the board and its tiles
    add_board(master)

    # TODO: Add the keyboard

def add_board(master: WORDLE) -> None:
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
        background=custom_color("background")
    )

    for row in range(6):
        for column in range(5):
            board_tile = tk.Label(
                master=board_frame,
                background=custom_color("black"),
                foreground=custom_color("white"),
                text=" ", # Set it to a space as placeholder for letters in the future
                font=custom_font(20),
                highlightbackground=custom_color("grey"),
                highlightthickness=1,
                height=1, # Set it to 1 arbitrarily, seemed to work (idk why)
                width=4 # Set it to 4 arbitrarily, seemed to work (idk why)
            )
            
            board_tile.grid(row=row, column=column, padx=5, pady=5, sticky="ew")
            master.widgets["board"][row].append(board_tile)

    board_frame.grid(row=1, column=0) # Row is 1 to account for the "WORDLE" on the top

    master.widgets["frame"].destroy()
    master.widgets["frame"] = board_frame

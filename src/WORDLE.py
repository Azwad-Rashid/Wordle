'''Custom class to be the main widget of a WORDLE game'''

import tkinter as tk
from typing import Any

from random_word import random_word

class WORDLE(tk.Tk):
    '''Extension of classic Tk class for WORDLE
    
    Special attribute
    -----------------
    `widgets`: dict[str, Any]
    
    A collection of all it's widgets. Keys are:
    - frame: tk.Frame
    - board: [[tk.Label(s)],[tk.Label(s)],[tk.Label(s)],[tk.Label(s)],[tk.Label(s)],[tk.Label(s)]]

    `word`: str

    The word to guess for this game

    `status`: tk.StringVar

    A stringVar to store the current game state

    `var`: tk.StringVar

    A stringVar to store the currently guessed word

    `attempt_no`: int

    An int that stores the attempt count

    `win`: bool

    Whether the player has won or not
    '''

    def __init__(self) -> None:
        super().__init__()
        self.widgets: dict[str, list[Any]] = {
            "title": tk.Frame,
            "frame": tk.Frame,
            "board": [[],[],[],[],[],[]]
        }
        self.word: str = random_word
        self.status: tk.StringVar = tk.StringVar(self, "start")
        '''Values:
        - start
        - play
        - end
        '''

        self.var: tk.StringVar = tk.StringVar(self, "")
        self.attempt_no: int = 0
        self.win: bool = False

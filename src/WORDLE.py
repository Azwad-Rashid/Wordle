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
    - word: str
    - title: [tk.Frame(s)]
    - board: [[tk.Label(s)],[tk.Label(s)],[tk.Label(s)],[tk.Label(s)],[tk.Label(s)],[tk.Label(s)]]

    `var`: tk.StringVar

    A stringVar to store the currently guessed word

    `attempt_no`: int

    An int that stores the attempt count
    '''

    def __init__(self) -> None:
        super().__init__()
        self.widgets: dict[str, Any] = {
            "word": random_word,
            "frames": [],
            "board": [[],[],[],[],[],[]]
        }
        self.var: tk.StringVar = tk.StringVar(self, "")
        self.attempt_no: int = 1

    def listen(self):
        pass


'''Custom class to be the main widget of a WORDLE game'''

import tkinter as tk
from typing import Any

class WORDLE(tk.Tk):
    '''Extension of classic Tk class for WORDLE
    
    Special attribute
    -----------------
    `collection`: dict[str, Any]
    
    A collection of all it's widgets. Keys are:
    - title: [tk.Frame(s)]
    - board: [[tk.Label(s)],[tk.Label(s)],[tk.Label(s)],[tk.Label(s)],[tk.Label(s)],[tk.Label(s)]]
    '''

    def __init__(self) -> None:
        '''Extension of classic Tk class for WORDLE
        
        Special attribute
        -----------------
        `collection`: dict[str, Any]

        A collection of all it's widgets. Keys are:
        - title: [tk.Frame(s)]
        - board: [[tk.Label(s)],[tk.Label(s)],[tk.Label(s)],[tk.Label(s)],[tk.Label(s)],[tk.Label(s)]]
        '''

        super().__init__()
        self.collection: dict[str, Any] = {
            "frames": [],
            "board": [[],[],[],[],[],[]]
        }

    def add_title(self, label: tk.Label) -> None:
        '''Adds a title to the collection of widgets

        :param label: The label containing the title
        :type label: tk.Label
        '''

        self.collection["title"].append(label)
        
    def add_board(self, label: tk.Label) -> None:
        '''Adds a board tile to the collection of widgets

        :param label: The label containing a board tile
        :type label: tk.Label
        '''

        self.collection["title"].append(label)

    def add_key(self, btn: tk.Button) -> None:
        '''Adds a key to the collection of widgets

        :param label: The label containing a key(clickable)
        :type btn: tk.Button
        '''

        self.collection["title"].append(btn)


'''Handles user input to play the game'''

import keyboard as kb
from string import ascii_letters as letters

from WORDLE import WORDLE
from update_board import update_board

def handle_keypress(master: WORDLE, event: kb.KeyboardEvent) -> None:
    '''Handles user input
    
    :param master: The main widget of the app
    :type master: WORDLE
    :param event: The keypress event
    :type event: kb.KeyboardEvent
    
    :rtype: None'''

    if event.name in letters:
        current_guess: str = master.var.get()

        if len(current_guess) == 5: return # The word length is 5 letters

        # Updates the current guess with the new letter
        current_guess += event.name.upper()
        master.var.set(current_guess)
    elif event.name == "enter":
        if len(master.var.get()) == 5:
            master.attempt_no += 1
            master.var.set("")
    elif event.name == "backspace":
        master.var.set(master.var.get()[:len(master.var.get()) - 1])

    update_board(master)

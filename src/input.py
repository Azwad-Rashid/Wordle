'''Handles user input to play the game'''

import keyboard as kb
from string import ascii_letters as letters

from WORDLE import WORDLE
from update_board import update_letters
from validate import update_colors, invalid_word
from random_word import word_list

def handle_keypress(master: WORDLE, event: kb.KeyboardEvent) -> None:
    '''Handles user input
    
    :param master: The main widget of the app
    :type master: WORDLE
    :param event: The keypress event
    :type event: kb.KeyboardEvent
    
    :rtype: None'''

    if event.name == "esc":
        master.destroy()
        quit()

    if master.status.get() == "start":
        if event.name == "space":
            master.status.set("play")
    elif master.status.get() == "play":
        if event.name in letters:
            current_guess: str = master.var.get()

            if len(current_guess) == 5: return # Stops the word from having more than 5 letters

            # Updates the current guess with the new letter
            current_guess += event.name.upper()
            master.var.set(current_guess)
            update_letters(master)
        elif event.name == "enter":
            if len(master.var.get()) == 5:
                if master.var.get().lower() in word_list:
                    update_colors(master)
                    master.attempt_no += 1
                    master.var.set("")
                else:
                    invalid_word(master)
        elif event.name == "backspace":
            master.var.set(master.var.get()[:len(master.var.get()) - 1])
            update_letters(master)
    elif master.status.get() == "end":
        if event.name == "space":
            master.status.set("replay")


'''Updates the board according to user input'''

from WORDLE import WORDLE

def update_letters(master: WORDLE) -> None:
    '''Updates the board according to user input
    
    :param master: The main widget of the app
    :type master: WORDLE
    '''

    if master.attempt_no > 5: return

    current_guess: str = master.var.get()

    current_guess += " " * (5 - len(current_guess))

    for i, letter in enumerate(current_guess):
        master.widgets["board"][master.attempt_no][i].config(text=letter)
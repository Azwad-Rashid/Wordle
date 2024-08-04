'''Updates the board according to user input'''

from WORDLE import WORDLE

def update_board(master: WORDLE) -> None:
    '''Updates the board according to user input
    
    :param master: The main widget of the app
    :type master: WORDLE
    '''

    if master.attempt_no > 5: return

    for i, letter in enumerate(master.var.get()):
        master.widgets["board"][master.attempt_no][i].config(text=letter)
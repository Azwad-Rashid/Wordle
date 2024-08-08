'''Validates the current guess and updates tile colors accordingly'''

from time import sleep

from WORDLE import WORDLE
from load_config import config_data

def update_colors(master: WORDLE) -> None:
    '''Changes the color of the tiles
    
    :param master: The main widget of the app
    :type master: WORDLE

    Updates the color of board tiles corresponding to the current attempt
    '''

    if master.attempt_no > 5:
        return

    actual_word: str = master.word.upper()
    guessed_word: str = master.var.get()
    letters: list[str] = list(actual_word) # This list used to manage the yellow cells

    colors: dict[str, str] = {
        "black": config_data["COLORS"]["black"],
        "grey": config_data["COLORS"]["grey"],
        "yellow": config_data["COLORS"]["yellow"],
        "green": config_data["COLORS"]["green"]
    }

    for i in range(5):
        if guessed_word[i] == actual_word[i]:
            master.widgets["board"][master.attempt_no][i].config(background=colors["green"])
        elif guessed_word[i] in letters:
            if actual_word.count(actual_word[i]) >= guessed_word.count(guessed_word[i]):
                master.widgets["board"][master.attempt_no][i].config(background=colors["yellow"])
                letters.remove(guessed_word[i])
            else:
                master.widgets["board"][master.attempt_no][i].config(background=colors["grey"])
        else:
            master.widgets["board"][master.attempt_no][i].config(background=colors["grey"])
        sleep(0.3)

    if actual_word == guessed_word:
        master.win = True
        master.status.set("end")

    if master.attempt_no == 5:
        master.status.set("end")


def invalid_word(master: WORDLE) -> None:
    '''Shows an invalid word
    
    :param master: The main widget of the app
    :type master: WORDLE

    Flashes a red color if the current word is invalid
    '''

    colors: dict[str, str] = {
        "red": config_data["COLORS"]["red"],
        "black": config_data["COLORS"]["black"],
    }

    for i in range(5):
        master.widgets["board"][master.attempt_no][i].config(background=colors["red"])
    sleep(0.5)
    for i in range(5):
        master.widgets["board"][master.attempt_no][i].config(background=colors["black"])


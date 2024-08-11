'''Creates the ending screen for the game'''

import tkinter as tk

from WORDLE import WORDLE
from custom_color import custom_color as colors
from custom_font import custom_font
from create_labels import end_labels

def create_end_menu(master: WORDLE) -> None:
    '''Creates the end menu
    
    Components
    ----------
    - Score
    - The word
    - Replay?
    '''

    end_frame: tk.Frame = tk.Frame(master, background=colors("background"))
    tk.Label(
        master=end_frame,
        text="🎉CONGRATULATIONS🎉" if master.win else "GAME OVER",
        width=30,
        font=custom_font(15),
        foreground=colors("white"),
        background=colors("background")
    ).grid(row=0, column=0, padx=5, pady=5)

    end_labels(
        master=end_frame,
        labels=[
            f"You guessed {master.word.upper()} in {master.attempt_no + 1} {"tries" if master.attempt_no else "try"}!" if master.win else f"The word was: {master.word.upper()}",
            f"Win streak: {master.streak}{f" (was {master.last_streak})" if not master.win else ""}",
            "Press <SPACE> to play again",
        ],
        start=1
    )

    end_frame.grid(row=1, column=0) # Row is 1 to account for the "WORDLE" on the top

    master.widgets["frame"].destroy()
    master.widgets["frame"] = end_frame

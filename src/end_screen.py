'''Creates the ending screen for the game'''

import tkinter as tk
from tkinter import font

from WORDLE import WORDLE
from load_config import config_data

def create_end_menu(master: WORDLE) -> None:
    '''Creates the end menu
    
    Components
    ----------
    - Score
    - The word
    - Replay?
    '''

    # Gets the required config data to create widgets
    custom_font = font.Font(
        master=master,
        font=(config_data["WIDGETS"].get("font_family", "Arial"), 15, "normal")
    )
    colors: dict[str, str] = {
        "background": config_data["WINDOW"]["background"],
        "black": config_data["COLORS"]["black"],
        "grey": config_data["COLORS"]["grey"],
        "yellow": config_data["COLORS"]["yellow"],
        "green": config_data["COLORS"]["green"],
        "red": config_data["COLORS"]["red"]
    }

    end_frame: tk.Frame = tk.Frame(master, background=colors["background"])
    tk.Label(
        master=end_frame,
        text="🎉CONGRATULATIONS🎉" if master.win else "GAME OVER",
        width=30,
        font=custom_font,
        foreground="#ffffff",
        background=colors["background"]
    ).grid(row=0, column=0, padx=5, pady=5)

    desc_font = custom_font.copy()
    desc_font.config(size=10)

    tk.Label(
        master=end_frame,
        text=f"You guessed {master.word.upper()} in {master.attempt_no + 1} {"tries" if master.attempt_no else "try"}!" if master.win else f"The word was: {master.word.upper()}",
        width=30,
        font=desc_font,
        foreground="#ffffff",
        background=colors["background"]
    ).grid(row=1, column=0, padx=5, pady=5)
    
    tk.Label(
        master=end_frame,
        text="Press <SPACE> to play again",
        width=30,
        font=desc_font,
        foreground="#ffffff",
        background=colors["background"]
    ).grid(row=2, column=0, padx=5, pady=5)

    end_frame.grid(row=1, column=0)

    master.widgets["frame"].destroy()
    master.widgets["frame"] = end_frame

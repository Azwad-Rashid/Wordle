'''Module used to style the master window of WORDLE'''

import tkinter as tk

from WORDLE import WORDLE
from load_config import config_data

def style(master: WORDLE) -> None:
    '''Used to style a master window to play WORDLE
    
    :param master: The master or root widget of the tkinter application
    :type master: Tk
    :rtype: None
    '''

    # Sets the title of the window
    master.update_idletasks()
    master.title(f'{config_data["GENERAL"]["app_name"]} by {config_data["GENERAL"]["author"].split(" ")[0]}')

    # Centres the window on the screen
    ww = master.winfo_width()
    wh = master.winfo_height()

    sw = master.winfo_screenwidth()
    sh = master.winfo_screenheight()

    x_gap: int = (sw - ww) // 2
    y_gap: int = (sh-wh) // 2
    
    master.after(1, lambda: master.geometry(f"{ww}x{wh}+{x_gap}+{y_gap}"))

    # Sets the window to display over everything else
    master.attributes("-topmost", config_data["WINDOW"]["topmost"])

    # TODO: Add colours and decorations


if __name__ == "__main__":
    root = tk.Tk()

    style(root)

    root.mainloop()

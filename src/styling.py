'''Module used to style the master window of the app'''

import tkinter as tk

def style(master: tk.Tk) -> None:
    master.title("WORDLE")
    master.geometry("400x600")

    # TODO: Add colours and decorations


if __name__ == "__main__":
    root = tk.Tk()

    style(root)

    root.mainloop()

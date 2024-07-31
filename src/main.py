'''The entry point for the application'''

import tkinter as tk

from styling import style

def main() -> None:
    root = tk.Tk()
    '''
    `root` is the main tkinter window, where all the widgets and components will be placed
    '''

    style(root)

    root.mainloop()



if __name__ == "__main__":
    main()
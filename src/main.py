'''The entry point for the application'''

import keyboard as kb

from WORDLE import WORDLE
from create_widgets import create_widgets
from styling import style
from input import handle_keypress
from start_screen import create_start_menu

def main() -> None:
    # Create the main widget
    root = WORDLE()

    # Variable to track the current state of the game
    root.status.trace_add("write", lambda *_: update_screen(root))

    # Creates tjhe start menu
    create_start_menu(root)
    root.update_idletasks()
    style(root)

    # Handles the user input
    kb.on_press(lambda event: handle_keypress(root, event))

    # Run a continuos loop for the main widget
    root.mainloop()

def update_screen(master: WORDLE) -> None:
    if master.status.get() == "play":
        # Initialize the main widget
        create_widgets(master)
        master.update_idletasks()
        style(master)



if __name__ == "__main__":
    main()
'''The entry point for the application'''

import keyboard as kb

from WORDLE import WORDLE
from create_widgets import create_widgets
from styling import style
from input import handle_keypress
from start_screen import create_start_menu
from end_screen import create_end_menu

def main() -> None:
    # Create the main widget
    root = WORDLE()

    # Variable to track the current state of the game
    root.status.trace_add("write", lambda *_: update_screen(root))

    # Creates the start menu
    start(root)

    # Handles the user input
    kb.on_press(lambda event: handle_keypress(root, event))

    # Run a continuos loop for the main widget
    root.mainloop()

def update_screen(master: WORDLE) -> None:
    match master.status.get():
        case "play":
            create_widgets(master)
            master.update_idletasks()
            style(master)

        case "end":
            create_end_menu(master)
            master.update_idletasks()
            style(master)

        case "replay":
            master.reset()
            start(master)

def start(master: WORDLE) -> None:
    # Creates the start menu
    create_start_menu(master)
    master.update_idletasks()
    style(master)
    print(master.word)

if __name__ == "__main__":
    main()
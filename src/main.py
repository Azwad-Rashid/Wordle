'''The entry point for the application'''

from WORDLE import WORDLE
from create_widgets import create_widgets
from styling import style
import keyboard as kb

from input import handle_keypress

def main() -> None:
    # Create the main widget
    root = WORDLE()

    # Initialize the main widget
    create_widgets(root)
    style(root)

    # Handles the user input
    kb.on_press(lambda event: handle_keypress(root, event))

    # Run a continuos loop for the main widget
    root.mainloop()



if __name__ == "__main__":
    main()
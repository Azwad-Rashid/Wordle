'''The entry point for the application'''

from WORDLE import WORDLE
from create_widgets import create_widgets
from styling import style

def main() -> None:
    # Create the main widget
    root = WORDLE()

    # Initialize the main widget
    create_widgets(root)
    style(root)

    # Run a continuos loop for the main widget
    root.mainloop()



if __name__ == "__main__":
    main()
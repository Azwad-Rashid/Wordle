'''Get a random word to play WORDLE'''

import random

def get_random_word() -> str | None:
    '''Gets a random word
    
    :returns: A 5-letter word, suitable for playing WORDLE. Returns None if the word file could not be found
    :rtype: str | None'''

    try:
        with open("src/word_list.txt", "r") as word_file:
            word_list: list[str] = word_file.read().split("\n")

        return random.choice(word_list)
    except FileNotFoundError:
        print("The word file could not be found")
        return None

random_word: str = get_random_word()
'''A random 5-letter word'''


if __name__ == "__main__":
    print(random_word)
'''Get a random word to play WORDLE'''

import random

word_list: list[str] = []
with open("src/word_list.txt", "r") as word_file:
    word_list = word_file.read().split("\n")

random_word: str = random.choice(word_list)
'''A random 5-letter word'''


if __name__ == "__main__":
    print(random_word)
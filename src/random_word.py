'''Get a random word to play WORDLE'''

import random

word_list: list[str] = []
with open("src/word_list.txt", "r") as word_file:
    word_list = word_file.read().split("\n")

def get_random_word() -> str:
    return random.choice(word_list)

if __name__ == "__main__":
    print(get_random_word())
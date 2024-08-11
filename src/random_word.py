'''Get a random word to play WORDLE'''

import random

word_list: list[str] = []
'''The list of all valid words'''

with open("src/word_list.txt", "r") as word_file:
    word_list = word_file.read().split("\n")

def get_random_word() -> str:
    '''Returns a random word from the WORDLE word list'''
    return random.choice(word_list)

# -*- coding: utf-8 -*-
"""Transfer each letter into word in password."""

from functools import reduce


def letter_to_word(password: str) -> str:
    """List with the letters, which turns into the letters.
    
    Args:
    ----
        password: User password
    
    Return:
    ------
        A string of words which was created
        by transfer letter into word
    
    """
    switcher: dict[str, str] = {
        'a': 'apple',   'A': 'APPLE',
        'b': 'bestbuy', 'B': 'BESTBUY',
        'c': 'coffee',  'C': 'COFFEE',
        'd': 'drip',    'D': 'DRIP',
        'e': 'egg',     'E': 'EGG',
        'f': 'fruit',   'F': 'FRUIT',
        'g': 'golf',    'G': 'GOLF',
        'h': 'hulu',    'H': 'HULU',
        'i': 'iphone',  'I': 'IPHONE',
        'j': 'jack',    'J': 'JACK',
        'k': 'korean',  'K': 'KOREAN',
        'l': 'laptop',  'L': 'LAPTOP',
        'm': 'music',   'M': 'MUSIC',
        'n': 'nut',     'N': 'NUT',
        'o': 'omelet',  'O': 'OMELET',
        'p': 'park',    'P': 'PARK',
        'q': 'queen',   'Q': 'QUEEN',
        'r': 'rope',    'R': 'ROPE',
        's': 'skype',   'S': 'SKYPE',
        't': 'tokyo',   'T': 'TOKYO',
        'u': 'usa',     'U': 'USA',
        'v': 'visa',    'V': 'VISA',
        'w': 'walmart', 'W': 'WALMART',
        'x': 'xbox',    'X': 'XBOX',
        'y': 'yelp',    'Y': 'YELP',
        'z': 'zip',     'Z': 'ZIP',

        '0': '0', '1': '1', '2': '2', '3': '3', '4': '4',
        '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',

        '-': '-', '~': '~', '#': '#', '&': '&',
        '@': '@', '{': '{', '}': '}', '+': '+',
        ')': ')', ':': ':', '!': '!', '=': '=',
        '*': '*', '_': '_', '%': '%', '<': '<',
        '>': '>', '$': '$', '|': '|', '[': '[',
        ']': ']', '^': '^', '?': '?', ' ': ' ',
    }

    res = ' '.join([switcher[password[i]] for i in range(len(password))])

    return res.strip()


if __name__ == '__main__':
    print('u can run this file as main')

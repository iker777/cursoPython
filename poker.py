import numpy as np
import itertools


def build_deck():
    numbers = list(range(2, 15))
    suits = ['H', 'S', 'C', 'D']
    deck = []

    for i in numbers:
        for s in suits:
            card = s + str(i)
            deck.append(card)
    
    return deck


def combinations(arr, n):
    arr = np.asarray(arr)
    t = np.dtype([('', arr.dtype)]*n)
    result = np.fromiter(itertools.combinations(arr, n), t)
    
    return result.view(arr.dtype).reshape(-1, n)

# https://medium.com/swlh/poker-with-python-how-to-score-all-hands-in-texas-holdem-6fd750ef73d

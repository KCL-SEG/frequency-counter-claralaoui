"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        frequencies[str(item)] = items.count(item)
    return frequencies

list = [5, 5, 5, 7 ,7 , 'ab', 'ab', 'c']
frequencies(list)

"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}

    for item in items:
        count = 0
        for item2 in items:
            if str(item) == str(item2) :
                count = count + 1

        frequencies[str(item)] = count
    return frequencies


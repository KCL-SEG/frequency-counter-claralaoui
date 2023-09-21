"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
	frequencies[str(item)] = items.count(item)
    return frequencies



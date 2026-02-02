
"""
Problem 1 — Comprehension Practice
"""


def even_squares(nums):
    """
    Return a list containing the square of every even number in nums.

    You must use a list comprehension.
    """
    return [i * i for i in nums if i % 2 == 0]


def word_lengths(words):
    """
    Return a dictionary mapping each word to its length.

    You must use a dictionary comprehension.
    """
    return {word: len(word) for word in words}


def remove_private(data):
    """
    Return a new dictionary containing only entries whose keys
    do NOT start with '_'.

    You must use a dictionary comprehension.
    """
    return {k: data[k] for k in data if k[0] != "_"}


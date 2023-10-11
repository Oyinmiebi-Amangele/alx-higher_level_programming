#!/usr/bin/python3
"""Module that contains a function that appends a text to a file"""


def append_write(filename="", text=""):
    """function that appends a text to a file"""

    with open(filename, 'a', encoding='utf-8') as f:
        return (f.write(text))

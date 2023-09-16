#!/usr/bin/python3
"""Module that contains a function that writes to a text file"""


def write_file(filename="", text=""):
    """function that writes a text to a file"""

    with open(filename, 'w', encoding='utf-8') as f:
        return (f.write(text))

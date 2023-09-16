#!/usr/bin/python3
"""Function that reads a test file"""


def read_file(filename=""):
    """function that reads from a file
    Args:
        filename: filename
    Raises
        Exception: when the file can be opened
    """

    with open(filename, 'r', encoding="utf-8") as files:
        read_file = files.read()
        print(read_file, end='')

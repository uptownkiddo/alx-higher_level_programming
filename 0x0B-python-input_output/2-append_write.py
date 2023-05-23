#!/usr/bin/python3
"""module contains the function append_write"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file
    and returns the no. of characters added
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

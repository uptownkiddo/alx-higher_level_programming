#!/usr/bin/python3

def read_file(filename=""):
    """Reads a text file and prints its contents to stdout"""
    with open(filename, "r", encoding="utf8") as file:
        for line in file:
            print(line, end="")

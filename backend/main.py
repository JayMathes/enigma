#!/bin/python
from modules.rotator import Rotator

# currently just for testing purposes
if __name__ == "__main__":
    rotator: Rotator = Rotator()

    for i in range(26):
        print(rotator.get_char())

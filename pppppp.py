#!C:\Users\ovsia\PycharmProjects\andreysrepo\venv\Scripts\python.exe

import sys

try:
    assert len(sys.argv) == 3
    x, y = int(sys.argv[1]), int(sys.argv[2])
    print(x + y)
except (IndexError, AssertionError, ValueError):
    print(0)

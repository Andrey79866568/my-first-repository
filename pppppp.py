#!C:\Users\ovsia\PycharmProjects\andreysrepo\venv\Scripts\python.exe
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('file_from')
parser.add_argument('file_to')
parser.add_argument('--upper', action='store_true', default=False, dest='up_text')
parser.add_argument('--lines', type=int, default=-1)
args = parser.parse_args()
try:
    with open(args.file_from, 'r') as file_from:
        lines = file_from.readlines()
        n = args.lines
        if n == -1 or n > len(lines):
            n = len(lines)
        with open(args.file_to, 'w') as file_to:
            for i in range(n):
                if args.up_text:
                    file_to.write(''.join([j.upper() for j in lines[i]]))
                else:
                    file_to.write(lines[i])
except FileNotFoundError:
    print('error')

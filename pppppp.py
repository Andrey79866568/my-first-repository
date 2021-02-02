#!C:\Users\ovsia\PycharmProjects\andreysrepo\venv\Scripts\python.exe
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--barbie', type=int, default=50)
parser.add_argument('--cars', type=int, default=50)
parser.add_argument('--movie', choices=['melodrama', 'football', 'other'], default='other')
args = parser.parse_args()
movie = 50
barbie = args.barbie
cars = args.cars
if args.movie == 'melodrama':
    movie = 0
elif args.movie == 'football':
    movie = 100
if barbie > 100:
    barbie = 100
elif barbie < 0:
    barbie = 0
if cars > 100:
    cars = 100
elif cars < 0:
    cars = 0

boy = round((100 - barbie + cars + movie) / 3)
girl = 100 - boy
print(f'boy: {boy}')
print(f'girl: {girl}')

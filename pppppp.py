#!C:\Users\ovsia\PycharmProjects\andreysrepo\venv\Scripts\python.exe

import sys

dict_of_values = {i.split('=')[0]: i.split('=')[1] for i in sys.argv[1:] if i != '--sort'}
if '--sort' in sys.argv:
    dict_of_values = sorted(dict_of_values.items())
else:
    dict_of_values = dict_of_values.items()
for key, elem in dict_of_values:
    print(f'Key: {key} Value: {elem}')

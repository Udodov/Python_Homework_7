import os
from creating import creating_csv

path_csv = os.path.join('data_phonebook', 'Phonebook.csv')


def check():
    valid = os.path.exists(path_csv)
    if not valid:
        print('книга пуста')
        creating_csv(path_csv)

from start import path_csv
from new_contact import input_name
from read_phonebook import read_line_file


def search_cont():
    search_name = input_name(input('Введите имя или фамилию для поиска контакта: '))
    my_file = read_line_file(path_csv)
    value = False
    for i in my_file:
        if search_name in i:
            print(f'По вашему запросу найден контакт:\n  {i}')
            value = True
            break
    if not value:
        print(f'К сожалению контакт {search_name} в книге не найден.')

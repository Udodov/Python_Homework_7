from start import path_csv
from creating import creating_contact


def new():
    firstname = input_name(input('Введите имя: '))
    lastname = input_name(input('Введите фамилию: '))
    phone = input('Введите номер телефона: ')
    email = input('Введите E-mail: ')
    description = input('Добавьте описание к контакту: ')

    contact_details = (firstname + '   ' + lastname + ";  " + phone + ';  ' + email + '; ' + description + '\n')
    creating_contact(path_csv, contact_details)
    print(f'Новая запись в телефонной книге: \n {contact_details} успешно создана!')


def input_name(name):
    remains_name = name[1:]
    first_char = name[0]
    return first_char.upper() + remains_name

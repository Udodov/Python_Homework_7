from start import path_csv
from new_contact import input_name
from read_phonebook import read_line_file


def delete_contact_record():
    del_name = input_name(input('Введите имя или фамилию для удаления контакта: '))
    my_file = read_line_file(path_csv)
    value = False
    for line in my_file:
        if del_name in line:
            confirm = input(f'Вы уверены, что хотите удалить {del_name} y/n?: ')
            print(confirm)

            if confirm == 'y':
                del my_file[line]
                value = True
            elif not value:
                print('Этого контакта не существует! Вернитесь в главное меню, чтобы ввести контакт')

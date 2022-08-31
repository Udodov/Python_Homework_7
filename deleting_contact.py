from start import path_csv
from new_contact import input_name
from read_phonebook import read_line_file
from re import compile, escape


def delete_contact_record():
    del_name = input_name(input('Введите имя или фамилию для удаления контакта: '))
    my_file = read_line_file(path_csv)

    for line in range(len(my_file)):
        if del_name in my_file[line]:
            confirm = input(f'Вы уверены, что хотите удалить {del_name} y/n?: ')
            del_str = ''.join(my_file[line])

            if confirm == 'y':
                del_line = compile(escape(del_str))

                with open(path_csv, 'w', encoding='utf-8') as f:
                    for line_d in my_file:
                        result = del_line.search(line_d)
                        if result is None:
                            f.write(line_d)

                print(f'Вы удалили контакт {my_file[line]}\n и его больше нет в книге!')
                break

        else:
            print('Этого контакта не существует! Вернитесь в главное меню, чтобы ввести контакт')
            break

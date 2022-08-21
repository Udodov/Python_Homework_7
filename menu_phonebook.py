from start import path_csv
from read_phonebook import read_from_file
from new_contact import new
from search_contact import search_cont
from deleting_contact import delete_contact_record


def menu():
    while True:
        print('\nМЕНЮ Телефонной книги\n'
              '1. Просмотреть все существующие контакты\n'
              '2. Добавить новый контакт\n'
              '3. Найти существующий контакт\n'
              '4. Удалить существующий контакт\n'
              '5. Выход\n')
        choice = input('Выберите пункт меню: ')

        match choice:
            case '1':
                my_file = read_from_file(path_csv)
                print(my_file)
                input('Вернуться в меню? Нажмите Enter')
                continue
            case '2':
                new()
                input('Вернуться в меню? Нажмите Enter')
                continue
            case '3':
                search_cont()
                input('Вернуться в меню? Нажмите Enter')
                continue
            case '4':
                delete_contact_record()
                input('Вернуться в меню? Нажмите Enter')
                continue
            case '5':
                print('Спасибо, что используете эту телефонную книгу!')
                break
            case _:
                input('Нет такого пункта...\nДля продолжения нажмите Enter и повторите ввод\n')
                continue
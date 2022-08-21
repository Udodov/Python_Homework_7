def creating_csv(path_file: str):
    with open(path_file, 'a+', encoding='utf-8') as file:
        file.write(f'Фамилия;  Имя;  Номер телефона;  e-mail; Описание\n')


def creating_contact(path_file: str, data: str):
    with open(path_file, 'a+', encoding='utf-8') as file:
        file.write(data)
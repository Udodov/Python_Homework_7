def read_from_file(path_file: str) -> str:
    with open(path_file, 'r+', encoding='utf-8') as file:
        return file.read()


def read_line_file(path_file: str):
    with open(path_file, 'r+', encoding='utf-8') as file:
        return file.readlines()
# Создание тестового лог-файла
import datetime
import random
import string


def random_str(length=100):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def create_log_file(amount_rows: int = 100):
    with open('app.log', 'w') as f:
        for i in range(amount_rows + 1):
            level = random.choice(['ERROR', 'INFO', 'WARNING'])
            row = f'{datetime.datetime.now()} {level}: {random_str()}\n'
            f.write(row)


create_log_file()


def generator_filter_log_file(filename, level: str = 'ERROR'):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if level in line:
                yield line.strip()


lvl = 'ERROR'
with open('error_app.log', 'w') as file:
    for error_line in generator_filter_log_file(filename='app.log', level=lvl):
        print(error_line)
        file.write(error_line+'\n')
        ...



############################################################################
############# получение только чётных чисел ################################
############################################################################

def gen_even_numbers(limit: int):
    for num in range(limit + 1):
        if num % 2 == 0:
            yield num


evens_num_list = list(gen_even_numbers(14))
print(evens_num_list)


############################################################################
############# работа с файлами по чанкам ###################################
############################################################################

def create_file(n: int, file_name: str) -> None:
    with open(file_name, 'w+') as file:
        for i in range(n + 1):
            file.write(f'i={i}\n')


file = 'n_rows.txt'
create_file(n=100, file_name=file)


def gen_read_line_by_line_file(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()


# for line in gen_read_line_by_line_file(file_name=file):
#     print(line)

############################################################################
################### Свой аналог range(n) ###################################
############################################################################
def gen_my_range(start: int, stop: int | None = None, step: int = 1):
    if not stop:
        stop = start
        start = 0

    current = start
    while current < stop:
        yield current
        current += step


for i in gen_my_range(12):
    print(i)

# 5. Функция по обработке списка строк (15 баллов)
# Напишите функцию process_strings, которая принимает список строк и 
# возвращает новый список, где каждая строка переведена в верхний регистр 
# и удалены все пробелы в начале и в конце строки.

# Пример:
# print(process_strings([' hello ', ' world', 'python '])) 
# # ['HELLO', 'WORLD', 'PYTHON']


def process_strings(lst):
    new_list = []
    for i in lst:
        new_list. append(i.strip().swapcase())

    return new_list

print(process_strings([' hello ', ' world', 'python ']))
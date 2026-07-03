# 9. Функция генерации списка (5 баллов)
# Напишите функцию generate_list, которая принимает два числа — начало и 
# конец диапазона — и возвращает список всех чисел в этом диапазоне.
# 
# Пример:
# print(generate_list(1, 5)) # [1, 2, 3, 4, 5]


def generate_list(start, end):
    lst = []
    for i in range (start, end + 1):
        lst.append(i)
    
    return lst

print(generate_list(1, 5))
    

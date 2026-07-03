# 1. Функция сложения списка (10 баллов)
# Напишите функцию sum_list, которая принимает список 
# чисел и возвращает их сумму.
# 
# Пример:
# print(sum_list([1, 2, 3, 4])) # 10


def sum_list(lst: list):
    sum = 0
    for i in lst:
        sum += i
        
    return sum + i

print(sum_list([1, 2, 3, 4]))
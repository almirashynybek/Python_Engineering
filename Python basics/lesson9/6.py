# 6. Функция поиска среднего значения (10 баллов)
# Напишите функцию find_average, которая принимает список чисел и
# возвращает их среднее арифметическое.

# Пример:
# print(find_average([1, 2, 3, 4, 5])) # 3.0

def find_average(lst):
    sum = 0
    for i in lst:
        sum += i

    return sum/len(lst)

print(find_average([1, 2, 3, 4, 5]))
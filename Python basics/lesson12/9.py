# 9. Фильтрация элементов словаря (10 баллов)
# Напишите программу, которая принимает словарь и фильтрует его, оставляя только
# те пары, где значения больше заданного числа.
# Пример вывода:
# Входной словарь: {'a': 10, 'b': 5, 'c': 20}
# Порог: 10
# Отфильтрованный словарь: {'a': 10, 'c': 20}




dict1 = {'a': 10, 'b': 5, 'c': 20}
target = 10

def filtering_elements(dict1):
    new_dict = dict1.copy()

    for key, value in dict1.items():
        if value < 10:
            del new_dict[key]
    
    return new_dict

print(filtering_elements(dict1))
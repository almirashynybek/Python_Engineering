# 8. Объединение словарей (15 баллов)
# Напишите программу, которая объединяет два словаря в один. Если в обоих
# словарях есть одинаковые ключи, значения должны суммироваться (если это числа)
# или объединяться (если это строки).
# Пример вывода:
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}
# Объединенный словарь: {'a': 1, 'b': 5, 'c': 4}



def dict_union(dict1, dict2):
    merged_dict = dict1.copy()

    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value

        else:
            merged_dict[key] = value

    return merged_dict



dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

print(dict_union(dict1, dict2))

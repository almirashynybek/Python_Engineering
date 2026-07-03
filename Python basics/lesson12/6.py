# 6. Подсчет повторяющихся слов (10 баллов)
# Напишите программу, которая принимает строку от пользователя и создает словарь,
# где ключи — это слова из строки, а значения — количество их повторений.
# Пример вывода:
# Введите строку: "привет мир привет"
# Словарь повторений: {'привет': 2, 'мир': 1}



string = "привет мир привет"

def count_repeated_word(string):
    string = string.split()
    new_dict = {}

    for item in string:
        if item in new_dict:
            new_dict[item] += 1

        else:
            new_dict[item] = 1
            
    return new_dict

print(count_repeated_word(string))
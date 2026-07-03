# 10. Функция по нахождению количества символов в строке (10 баллов)
# Напишите функцию char_count, которая принимает строку и символ, и 
# возвращает количество вхождений этого символа в строке.
# 
# Пример:
# print(char_count("hello", "l")) # 2


def char_count(string, char):
    count = 0
    for i in string:
        if i == char:
            count += 1

    return count

print(char_count("hello", "l"))
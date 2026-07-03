# 9.Функция подсчета согласных (15 баллов)
# Напишите функцию count_consonants, которая принимает строку и 
# возвращаетколичество согласных букв в этой строке.
# 
# Пример:
# print(count_consonants("программирование")) # 10


def count_consonants(string):
    count = 0
    for char in string:
        if char in "ауоиэыюеё":
            continue

        else:
            count += 1
        
    return count

print(count_consonants("программирование"))
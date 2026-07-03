# 2. Функция проверки символа (10 баллов)
# Напишите функцию is_vowel, которая принимает один символ и 
# возвращает True,если это гласная буква, и False в противном случае.
# 
# Пример:
# print(is_vowel('a')) # True
# print(is_vowel('b')) # False


def is_vowel(char):
    if char in 'aeiou':
        return True 
    
    return False

print(is_vowel('a'))
print(is_vowel('b'))
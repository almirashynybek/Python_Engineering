# 7. Функция проверки делимости (10 баллов)
# Напишите функцию is_divisible, которая принимает два числа и возвращает True,
# если первое число делится на второе без остатка, и False в противном случае.

# Пример:
# print(is_divisible(10, 2)) # True
# print(is_divisible(10, 3)) # False


def is_divisible(a, b):
    if a % b == 0:
        return True
    return False
    
print(is_divisible(10, 2)) # True
print(is_divisible(10, 3)) # False
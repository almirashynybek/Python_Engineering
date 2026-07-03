# 9. leetcode 1
# Two Sum
# Описание: Даны массив nums и число target.
# Найдите индексы двух чисел, сумма которых равна target.

# Пример:
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]


def two_sum(lst, target):
    for i in range (len(lst)):
        if target - lst[i] in lst:
            return i, lst.index(target - lst[i])
        
print(two_sum([2, 7, 11, 15], 9))

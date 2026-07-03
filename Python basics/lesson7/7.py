string = input("Введите 5 чисел, разделенные пробелами: ")
list1 = string.split(' ')


list1 = [int(num) for num in list1] 

abs_sum = sum(abs(num) for num in list1)
print("Сумма абсолютных значений чисел:", abs_sum)
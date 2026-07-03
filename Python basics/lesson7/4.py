
string = input("Введите 5 чисел, разделенные пробелами: ")
list = string.split(' ')

max_value = max(list)
min_value = min(list)

print(f'max_value: {max_value}, min_value: {min_value}')
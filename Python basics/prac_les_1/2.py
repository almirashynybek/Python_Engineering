n_1 = int(input("1 number is "))
n_2 = int(input("2 number is "))
n_3 = int(input("3 number is "))
n_4 = int(input("4 number is "))
n_5 = int(input("5 number is "))

list = [n_1, n_2, n_3, n_4, n_5]
sum = 0
max_number = list[0]
min_number = list[1]

for i in list:
    sum += i
    if max_number < i:
        max_number = i

    if min_number > i:
        min_number = i

print(f"Сумма равно {sum}")
print(f"Среднее занчение равно {sum/5}")
print(f"Максимальное число равно {max_number}")
print(f"Минимальное число равно {min_number}")
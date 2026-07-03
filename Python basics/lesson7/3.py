#1 method
list1 = []

for i in range(10):
    num = int(input(f'Введите число {i+1}: '))
    list1.append(num)

for item in list1:
    if item > 5:
        print(item)

    else:
        continue


#2 method
string = input("Введите 10 чисел, разделенные пробелами: ")  
list2 = string.split(' ') 
list_result = []  

for item in list2:
    if item.isdigit():  # Check if the item is a digit
        num = int(item)  # Convert the string to an integer
        if num > 5:  
            list_result.append(num) 
    else:
        print('Error: Неверный ввод, не число:', item)  


print(list_result)

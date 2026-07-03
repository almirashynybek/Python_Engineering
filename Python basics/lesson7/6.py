string = input("Введите 5 чисел, разделенные пробелами: ")
list1 = string.split(' ')

# converting from string to int 
list1 = [int(num) for num in list1]

list1.sort(reverse = True)
print(list1)
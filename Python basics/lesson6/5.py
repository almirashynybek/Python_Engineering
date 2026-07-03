string = input("Введите строку: ")
list_1 = []


for i in string:
    result = ord(i)
    print(f'ASCII code of "{i}" is: {result}')
    list_1.append(result)

for element in list_1:
    result = chr(element)
    print(f'The element is: {result}')
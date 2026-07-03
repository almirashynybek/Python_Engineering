string = input("Введите строку: ")
len = len(string)

#in order to print every 3rd element, the step should be 2
for i in string[0:len + 1:2]:
    print(i)
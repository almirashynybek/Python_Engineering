string = input("Введите строку: ")

for i in string:
    if i in 'AEIOUYaeiout':
        # it will check does there any vowel char
        string = string.replace(i, '*')

    else:
        continue

# printes the replaced string
print(string)
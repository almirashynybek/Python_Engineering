string = input("Введите строку: ")
symbol_1 = input()
symbol_2 = input()

if not symbol_1 in string:
    print(f"{symbol_1} not in the string, please enter a correctbstring!")
else:
    print(string.replace(symbol_1, symbol_2))
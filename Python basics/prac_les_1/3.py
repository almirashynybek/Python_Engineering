n = int(input('Введите оценку: '))

if n in range(0, 101):
    if n in range(90, 101):
        print('A')
    elif n in range(80, 90):
        print('B')
    elif n in range(70, 80):
        print('C')
    elif n in range(60, 70):
        print('D')
    else:
        print('F')
    
else:
    print('Введите оценку от 0 до 100!')
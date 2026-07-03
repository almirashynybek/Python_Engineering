while True:  

    num1 = int(input('Введите первое число: '))
    num2 = int(input('Введите второе число: '))

    operation = input('Введите операцию (+, -, *, /): ')

    # Выполнение соответствующей операции
    if operation == '+':
        print(f'Результат: {num1 + num2}')
    elif operation == '-':
        print(f'Результат: {num1 - num2}')
    elif operation == '*':
        print(f'Результат: {num1 * num2}')
    elif operation == '/':
        if num2 != 0:
            print(f'Результат: {num1 / num2}')
        else:
            print('Ошибка: Деление на ноль невозможно.')
    else:
        print('Неправильная операция. Пожалуйста, попробуйте снова.')

    
    continue_input = input('Хотите продолжить? (да/нет): ')
    if continue_input.lower() == 'нет':
        print('Выход из программы...')
        break  

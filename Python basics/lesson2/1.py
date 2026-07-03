time = int(input())

if (0 <= time <=23):
    if (5 <= time <= 11):
        print('Morning')

    elif (12 <= time <= 17):
        print('Afternoon')

    elif (18 <= time <= 22):
        print('Evening')

    else:
        print('Night')

else:
    print('Error')
    
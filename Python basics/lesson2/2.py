year = int(input())

if(year % 4 == 0) and (year % 100 != 0):
     print(f'{year} год является високосным')

elif ((year % 4 == 0) and (year % 100 == 0) and (year % 400 == 0) ):
    print(f'{year} год является високосным')


elif(year % 100 == 0) and (year % 400 != 0):
    print(f'{year} год не является високосным')


elif(year % 100 == 0) and (year % 400 != 0):
     print(f'{year} год является високосным')



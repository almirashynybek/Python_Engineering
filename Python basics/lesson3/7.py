height = int(input('Enter please the height of triangle: '))

for i in range(1, height + 1):
    
    # Выводим пробелы для центрирования
    print(" " * (height - i), end='') 
    
    # как только пробел закончиться * cтавиться
    print("*" * (2 * i - 1)) #тут количества *

#   ,*,
#  ,***,
# ,*****,    height 3, but 7 symbols in each row


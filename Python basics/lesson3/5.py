n = int(input('Enter number: '))
sum = 0
for i in range (1, n+1):  #when n is included
    if (i % 3 == 0 and i % 5 ==0):
        sum += i

    else:
        pass

print(sum)
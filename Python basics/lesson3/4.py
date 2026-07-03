n = int(input('Enter number: '))
factorial = 1

#soluton with for loop
for i in range (1, n+1):
    factorial *= i

print(factorial)


#soluton with while 
i=1
while i <= n:
    factorial *= i
    i += 1

print(factorial)
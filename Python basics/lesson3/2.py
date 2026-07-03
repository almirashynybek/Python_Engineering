n = int(input('Enter number: '))

# 1st method
i = 1
while n >= i:
    print(n)
    n -= 2

# 2nd method with for loop 
for i in range (n, 0, -2):
    print(i)
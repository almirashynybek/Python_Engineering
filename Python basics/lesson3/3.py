number = int(input('Enter number: '))
#i had to initialize the stop iteration in for loop
# because, in loop imposible iterate the float 
stop = int(number/2) 
value = True

for i in range (2, stop):
    if number % i == 0:
        value = False
        break
    else:
        value = True
        pass

if value == True:
    print(f'The number {number} is prime')

else:
    print(f'The number {number} is not prime')
        

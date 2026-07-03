number = int(input()) 
 
if number < 0: 
    if number % 2 == 0: 
        print(f'Number {number} is negative and even') 
 
    else: 
        print(f'Number {number} is negative but not even') 
 
else: 
    print(f'Number {number} is positive')
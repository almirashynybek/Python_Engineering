i = 1
while i <= 5:
    print(i)
    i = i + 1   # i += 1

secret_num = 9
guess_count = 0

while guess_count < 3:
    guess = input('Guess number: ')
    guess_count += 1
    
    if guess.isdigit():
        if int(guess) == secret_num:
            print('you win!')
            break
    
    elif not guess.isdigit():
        print('Enter correct input ')

else:
    print('you lose!')



for item in 'python':
    print(item)


# print(stop)
# print(start, stop)
# print(start, stop, step)
    
for item in range(5):  #5 not included
    print(item)

for item in range(5, 9): # started at 5 and finished with 8
    print(item)

for item in range(5, 15, 2): #start 5 and next is 7, like through 2 ieration
    print(item)
    
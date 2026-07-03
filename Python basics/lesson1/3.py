#lets identify our variables
name = input('What is your name? ')
age = input('What is your age? ')

# by using f-string I call print function
# f-string help us to define our variables into the string
print(f'Hi {name}! You are {age} years old.')


#2nd way 
print('Hi',name,'! You are',age,'years old.')

#3rd way
print('Hi ' + name,'! You are ' + age + ' years old.')

# birth_year = int(input('birth year: '))
# age = 2024 - birth_year
# print(age)

# name = 'Almira'
# age = 20
# print ('name:' + name + 'age:' + str(age))

# # .format()
# print('name: {}, age: {}'.format(name, age))
# print(f'name: {name}, age: {age}')


# is_hot = True #which value is true, in console will those condition
# is_cold = False
# is_cold = True #here in terminal will appear 1st true value
# if is_hot:
#     print('сегодня жаркий день')
#     print('пьем больше воды')
# elif is_cold:
#     print('Сегодня холодно')
#     print('надеваем теплую одежду')
# else:
#     print('сегодня прекрасный день!')


#True and True -> True
#True and False -> False
# False and False -> False
# False and True -> False
x, y = 5, 10
print(x > 0 and y < 20)
print(x > 0 and x > 20)

#True or True -> True
#True or False -> True
# False or False -> False
# False or True -> True
print(x < 0 or y > 20)

x, y, z = 5, 10, 15
print(x > 0 and y < 20 or z == 15)
#order of sign 1)not   2)and   3)or

age = 16
has_passport = True
if age >= 18:
    if has_passport:
        print('Excellent')
    else:
        print('Sad')
else:
    print("you can't")


#isdigit работает только  когда age обозначено
age = input('Enter age: ')

if age.isdigit(): 
    print('Right!')
numbers = [5, -3, 8, -6, 0, 4, -2, 11]
even_numbers = []
odd_numbers = []
positive_numbers = []

for i in numbers:
    if i > 0:
        positive_numbers.append(i)

    if i % 2 == 0:
        even_numbers.append(i)

    else:
        odd_numbers.append(i)

even_numbers.sort()
odd_numbers.sort()
positive_numbers.sort()

print(f'even_numbers = {even_numbers}')
print(f'odd_numbers = {odd_numbers}')
print(f'positive_numbers = {positive_numbers}')

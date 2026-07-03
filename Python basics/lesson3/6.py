sum = 0

i = 1
while i <= 5:
    number = int(input(f'Enter number {i}: '))
    sum += number
    i += 1

result = float(sum/5)
print(f'The arithmetic mean is {result}')
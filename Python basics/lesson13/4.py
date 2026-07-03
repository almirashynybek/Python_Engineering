numbers1 = [1, 2, 3, 4, 5]
numbers2 = [1, -2, 3, -4, 5]

all_positive = all(map(lambda x: x > 0, numbers1))
# all_positive = all(map(lambda x: x > 0, numbers2))

all_positive1 = all(num > 0 for num in numbers1)

print(all_positive)
print(all_positive1)
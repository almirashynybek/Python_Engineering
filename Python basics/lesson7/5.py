fruits = ["яблоко", "банан", "вишня", "апельсин", "груша"]
string = input()

for i in fruits:
    if i == string:
        fruits.remove(i)

    else:
        continue

print(fruits)
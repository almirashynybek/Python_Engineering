fruits = ["apple", "banana", "pear", "kiwi"]

has_short_string = any(map(lambda x: len(x) < 5, fruits))

print(has_short_string)
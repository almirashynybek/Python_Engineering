fruits = ["apple", "banana", "pear", "kiwi"]

longest_word = max(fruits, key = lambda x: len(x))

print(longest_word)
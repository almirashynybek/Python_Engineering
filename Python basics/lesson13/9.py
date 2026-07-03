fruits1 = ["apple", "banana", "pear", "kiwi"]
fruits2 = ["apple", "banana123", "pear", "kiwi"]

all_alpha_1 = all(map(lambda x: x.isalpha(), fruits1))
all_alpha_2 = all(map(lambda x: x.isalpha(), fruits2))

print(all_alpha_1)
print(all_alpha_2)
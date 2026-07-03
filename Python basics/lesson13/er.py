words = ["cat", "elephant", "dog", "giraffe"]
long_words = filter(lambda x: len(x) > 4, words)
print(list(long_words))
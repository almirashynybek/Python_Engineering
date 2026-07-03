string = input("Введите строку: ")
cnt_vowel = 0
cnt_consonant = 0

for char in string:
    if char in "aeiouy":
        cnt_vowel += 1

    else:
        cnt_consonant += 1

print(f'Количество гласных: {cnt_vowel} и согласных: {cnt_consonant}')
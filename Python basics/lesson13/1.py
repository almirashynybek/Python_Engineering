# def get_even_numbers(numbers):
#     even = [i for i in numbers if i % 2 == 0 ]
#     return even
    


numbers = [1, 2, 3, 4, 5, 6]
get_even_numbers = list(filter(lambda x: x % 2 == 0, numbers))


# print(get_even_numbers(numbers))
print(get_even_numbers)
#1
list1 = list(range(1,11))
list2 = [i ** 2 for i in list1]

#2
list3 = []
for i in range (1, 11):
    list3.append(i**2)

print(list2)
print(list3)
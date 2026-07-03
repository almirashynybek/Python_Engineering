students = ["Aliya:90", "Boris:85", "Gulnara:78", "Erzhan:50", "Daniyar:100", "Aysultan:59"]
honor_students = []
good_students = []
fail_students = []

for i in students:
    name, point = i.split(':')
    point = int(point)

    if point in range(85, 101):
        honor_students.append(i)

    elif point in range(60, 85):
        good_students.append(i)

    else:
        fail_students.append(i)

honor_students.sort()
good_students.sort()
fail_students.sort()

print(f'honor_students: {honor_students}')
print(f'honor_students: {good_students}')
print(f'honor_students: {fail_students}')

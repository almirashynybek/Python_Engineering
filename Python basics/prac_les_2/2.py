data = [
    "Алия,25,Алматы",
    "Андрей,17,Нур-Султан",
    "Жанна,30,Шымкент",
    "Анастасия,19,Караганда",
    "Асел,16,Актобе"
]
result= []


for i in data:
    name, age, city = i.split(',')
    age = int(age)

    if age >= 18:
        #result.append(name + ',' + city)
        result.append(f'{name},{city}')

    else:
        continue

print(result)
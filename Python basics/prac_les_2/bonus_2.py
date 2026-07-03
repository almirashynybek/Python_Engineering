celsius = [0, 20, 30, 100]
fahrenheit = []

for i in celsius:
    i = int(i)
    f = float((i * 1.8) + 32)
    fahrenheit.append(f)

print(fahrenheit)
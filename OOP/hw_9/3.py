# Задание 3: Практика с MRO (Method Resolution Order)

class A:
    def perform(self):
        print("Выполняется действие A")

class B:
    def perform(self):
        print("Выполняется действие B")

class C:
    def perform(self):
        print("Выполняется действие C")
    
class D (B, C):
    pass

d = D()
d.perform()

# Вывод: Выполняется действие B  
# потому,  Порядок разрешения методов (D.__mro__) показывает, что
# Python будет искать метод perform в следующем порядке:
# 1. D    2. B    3. C    4. object
# Python находит его в классе B, так как B стоит раньше чем C
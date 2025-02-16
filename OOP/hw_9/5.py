# Задание 3: Конвертер температур
# метод статик позволяет написать функцию в классе не испоьзуя self, 
# то есть можем использовать атрибут на прямую

class TemperatureConverter:
    
    @staticmethod
    def celsius_to_fahrenheit( celsius):
        return ((celsius * 9//5) + 32)
    
    @staticmethod
    def fahrenheit_to_celsius( fahrenheit):
        return ((32 - fahrenheit) * 5//9)
    

result = TemperatureConverter()

print(result.celsius_to_fahrenheit(5))
print(result.fahrenheit_to_celsius(20))

# Задание 1: Класс для контроля температуры устройства

class Device:
    def __init__(self, temperature):
        self.__temperature = temperature

    def increase_temp(self, degree):
        # добавляющая степень не должна прeвышать 80
        if (self.__temperature + degree <= 80):
            self.__temperature += degree
            print(f"{degree} градусов добавлено")

        else:
            print("Температура не должна превышать 80 градусов")

        
    def decrease_temp(self, degree):
        if (self.__temperature - degree > 0):
            self.__temperature -= degree
            print(f"{degree} градусов отняли")

        else:
            print("Температура не должна опускаться ниже 0 градусов")


device = Device(20)
device.increase_temp(32)
device.decrease_temp(7)    
# Задание 1: Устройства с разными способами заряда

from abc import ABC, abstractmethod



class Device(ABC):

    @abstractmethod
    def charge(self):
        pass


class Phone(Device):
    def charge(self):
        print("Зарядка через USB")

class Laptop(Device):
    def charge(self):
        print("Зарядка через адаптер питания")

class WirelessEarbuds:
    def charge(self):
        print("Зарядка через беспроводной кейс")



def charge_devices(devices):
    return [item.charge() for item in devices]


devices = [Phone(), Laptop(), WirelessEarbuds()]
charge_devices(devices)
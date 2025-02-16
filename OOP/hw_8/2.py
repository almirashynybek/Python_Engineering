from abc import ABC, abstractmethod


class Appliance(ABC):

    @abstractmethod
    def turn_on(self):
        print("Switch on!")

    def turn_off(self):
        print("Switch off!")



class WashingMachine(Appliance):
    def turn_on(self):
        print("Machine still turning on!")



class Refrigerator(Appliance):
    def turn_on(self):
        print("Refrigerator must be turned on!")


wash = WashingMachine()
ref = Refrigerator()

wash.turn_on()
ref.turn_on()
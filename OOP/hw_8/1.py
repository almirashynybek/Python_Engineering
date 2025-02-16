class Vehicle:
    def __init__(self, speed):
        self.speed = speed
    
    def move(self):
        print(f"Vehicle moves with speed {self.speed} km/h ")

    
class Car(Vehicle):
    def move(self):
        print(f"Car moves with speed {self.speed} km/h ")


class Bicycle(Vehicle):
    def move (self):
        print(f"Bicycle moves with speed {self.speed} km/h ")


car = Car(25)   
bicycle = Bicycle(15)

car.move()
bicycle.move()
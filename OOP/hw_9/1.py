# Множественное наследование с ролями персонажей
# Задание 1: Персонажи с разными ролями

class Walker:
    def walk (self):
        print("Идет")

class Swimmer:
    def swim (self):
        print("Плавает")

class Flyer:
    def fly (self):
        print("Летит")


class Duck (Walker, Swimmer):
    pass
    
class Penguin(Walker, Swimmer):
    pass

class Superhero(Walker, Swimmer, Flyer):
    pass


duck = Duck()
duck.walk()
duck.swim()

penguin = Penguin()
penguin.walk()
penguin.swim()

superhero = Superhero()
superhero.walk()
superhero.swim()
superhero.fly()
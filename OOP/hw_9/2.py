# Задание 2: Множественное наследование с дополнительной логикой

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I'm {self.name}!")


class Worker:
    def work(self):
        print("Выполняет рабочие задачи")


class Student:
    def study(self):
        print("Изучает новые темы")



class Intern(Worker, Student):
    def daily_schedule(self):
        process_1 = Worker()
        process_1.work()

        process_2 = Student()
        process_2.study()
        

intern = Intern()
intern.daily_schedule()
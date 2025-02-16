# Задание 2: Сотрудники и различные способы работы

from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def perform_task(self):
        pass


class Developer(Employee):
    def perform_task(self):
        print("Пишет код")


class Designer(Employee):
    def perform_task(self):
        print("Создает макет")


class Manager(Employee):
    def perform_task(self):
        print("Проводит совещание")



def work_day(employees):
    return [item.perform_task() for item in employees]



employees = [Developer(), Designer(), Manager()]
work_day(employees)

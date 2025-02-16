# Управление банковским счетом с комиссией

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance


    def deposit(self, amount):

        # balance = self.__get_balance()
        # print(f'Баланс: {balance}')

        if amount > 0:
            self.__balance += amount
            print(f"{amount} добавлено на счет")

        else:
            print("Сумма должна быть положительной")



    def withdraw(self, amount):
        if (0 < amount <= self.__balance):
            result = amount + (amount * 0.02)
            self.__balance -= result
            print(f"{result} снято с счета")

        else:
            print("Недостаточно средств или неверная сумма")
    


account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
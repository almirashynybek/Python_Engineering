# Задание 2: Банковский счет

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, amount):
        return self.balance + amount 

    def __sub__(self, amount):
        return self.balance - amount
    
    def __bool__ (self):
        return self.balance > 0
    
    def __str__(self):
        return f"self.amount: {self.balance}"
    


account = BankAccount(100)
account += 50 # Пополнение
account -= 30 # Снятие средств

print(account) # Вывод: Баланс: 120
if account:
    print("На счете есть средства") 
else:
    print("Баланс нулевой")
# Задание 2: Заказ и оплата

class Order:
    def __init__(self):
        self.order:dict = {}

    def add_item(self, item:str, price:int):
        self.order[item] = price

    def calculate_total(self):
        return sum(self.order.values())
    

class PaymentProcessor:
    def process_payment(self, order:Order, total:int):
        print(f"Processing payment of {total} for the order.")
        print("Payment processed successfully!")


order = Order()
order.add_item("Книга", 20)
order.add_item("Ноутбук", 1000)

total = order.calculate_total()

payment_processor = PaymentProcessor()
payment_processor.process_payment(order, total)



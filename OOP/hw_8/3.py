class Product:
    def __init__(self, price, discount):
        self.price = price
        self.discount = discount


    @property
    def final_price(self):
        total = self.price - (self.price * self.discount//100)
        return total
    

product = Product(3000,20)
print(product.final_price)
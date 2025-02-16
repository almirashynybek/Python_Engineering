# Задание 1: Корзина покупок

class ShoppingCart:
    def __init__(self):
        self.__items = []

    def add_item(self, item: str):
        self.__items.append(item)  

    def __len__(self):
        print("Количество товаров в корзине:", end = '')
        return len(self.__items)  
    
    def __getitem__(self, index: int):
        return self.__items[index]
    
    def __setitem__(self, index: int, value: str):  
        self.__items[index] = value  
    
    def __str__(self):
        return (
            f"В вашей корзине к покупке следующие товары: "
            f"{', '.join(self.__items) if self.__items else 'корзина пуста'}"
        )


cart = ShoppingCart() 
cart.add_item("Кофе")
cart.add_item("Книга")

print(len(cart))  # Output: 2
print(cart[0])  # Output: Кофе

cart[1] = 'Журнал'  # Update the item at index 1
print(cart)  # Output: В вашей корзине к покупке следующие товары: Кофе, Журнал

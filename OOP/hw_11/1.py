import time

class LoggingMixin:
    def log(self, message:str):
        print(f"[LOG] {message}")


class CachMixin:
    cach: dict = {}

    def get(self, key:int):
        if key in self.cach:
            return self.cach[key]
        
    def set(self, key:int, value:dict):
        self.cach[key] = value


class ProductService(CachMixin, LoggingMixin):
    def get_product(self, product_id: int):
        product = self.get(product_id)

        if product is None:
            self.log(f'Product {product_id} not found in cache')

            product = self.get_product_from_db(product_id)
            self.set(product_id, product)
            self.log(f'Product {product_id} is added to cache')

        else:
            return product
        
    
    def get_product_from_db(self, product_id:int):
        self.log('Обращаюсь к БД. Будет задержка в 3 секунды')

        time.sleep(3)
        self.log(f'Product {product_id} loaded from DB')
        return {"id": product_id, "name": f"Product {product_id}"}
    

product_service = ProductService()
product_id_1 = 1
product_id_2 = 2

# Первый вызов: обращение к базе данных (так как данных в кэше еще нет)
product_1_first_call = product_service.get_product(product_id_1)
product_1_second_call =product_service.get_product(product_id_1) # Второй вызов из кэша
product_1_third_call = product_service.get_product(product_id_1) # Третий вызов из кэша

print(product_1_first_call)
print(product_1_second_call)
print(product_1_third_call)

# Тот же процесс для другого продукта
product_2_first_call = product_service.get_product(product_id_2)
product_2_second_call = product_service.get_product(product_id_2)
product_2_third_call =product_service.get_product(product_id_2)
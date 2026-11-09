class Product:
    def __init__(self, name, price, quantity = 0):
        self.__name = name
        self.price = price
        self.__quantity = quantity

    @property
    def name(self):
        return self.__name
    

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price):
        if price <= 0:
            raise ValueError('price must be positive')
        self.__price = price


    @property
    def quantity(self):
        return self.__quantity


    def add_stock(self, amount):
        if amount < 0:
            raise ValueError('amount must be positive')
        self.__quantity += amount


    def sell(self, amount):
        if self.__quantity < amount:
            raise ValueError(f'not enough {self.__name}')
        self.__quantity -= amount


    @property
    def total_value(self):
        return self.price * self.__quantity
    
    def __str__(self):
        return f'{self.__name}: {self.__quantity} x {self.price} = {self.total_value}'
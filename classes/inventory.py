from classes.product import Product

class Inventory:
    def __init__(self):
        self.__products = []
        
        
    def add(self, new_product: Product):
        if self.find(new_product.name):
            raise ValueError(f'{new_product.name} already exists')
        self.__products.append(new_product)
            
            
    def find(self, name):
        find_item = list(filter(lambda p: p.name == name, self.__products))
        return find_item[0] if find_item else None
        
        
    def by_value(self):
        return sorted(self.__products, key= lambda p: p.total_value, reverse=True)
    
    
    @property
    def total_value(self):
        total_price = 0
        for product in self.__products:
            total_price += product.total_value
            
        return total_price
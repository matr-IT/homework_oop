from src.Product import Product

class LawnGrass(Product):
    """
    Класс газонной травы, наследник класса продукта
    """
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
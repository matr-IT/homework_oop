class Product:
    """
    Класс продукта
    """

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        return self.__price * self.quantity + other.__price * other.quantity

    @classmethod
    def new_product(cls, product: dict):

        new_product = Product(product["name"], product["description"], product["price"], product["quantity"])
        return new_product

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price > 0:
            if price >= self.__price:
                self.__price = price
            elif price < self.__price:
                if input("Подтвердите снижение цены:\ny - да\nn - нет") == "y":
                    self.__price = price
        else:
            print("“Цена не должна быть нулевая или отрицательная”")


p1 = Product("Телефон", "Смартфон", 50000.0, 10)
print(p1)
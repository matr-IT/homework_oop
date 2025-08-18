class Product:
    """
    Класс продукта
    """

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product: dict):

        new_product = Product(product["name"], product["description"], product["price"], product["quantity"])
        return new_product

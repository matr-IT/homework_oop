from src.Product import Product


class Category:
    """
    Класс категории
    """

    category_count = 0
    product_count = 0

    name: str
    description: str
    __products: list[Product]

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product и его наследников")
        self.__products.append(product)
        Category.product_count += 1

    def __str__(self):
        quantity_counter = 0
        for i in self.__products:
            quan = i.quantity
            quantity_counter += quan
        return f"{self.name}, количество продуктов: {quantity_counter} шт."

    @property
    def products(self):
        for i in self.__products:
            print(i)

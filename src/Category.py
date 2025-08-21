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
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            "В категорию можно добавить только объект класса Product"

    @property
    def products(self):
        list_of_products = ""
        for i in self.__products:
            list_of_products += f"{i.name}, {i.price} руб. Остаток: {i.quantity} шт.\n"
        return list_of_products

from src.Product import Product


class Category:
    """
    Класс категории
    """

    category_count = 0
    product_count = 0

    name: str
    description: str
    products: list[Product]

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)

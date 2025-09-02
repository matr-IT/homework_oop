from src.Product import Product


class Category:
    """
    Класс категории
    """

    category_count = 0
    product_count = 0

    name: str
    description: str
    __products: list

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = list(products)
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
        str_list = []
        for i in self.__products:
            str_list.append(f"{i.name}, {i.price} руб. Остаток: {i.quantity} шт.")
        return "\n".join(str_list)

    def middle_price(self):
        try:
            counter = 0
            for i in self.__products:
                counter += i.price
            return round(counter / len(self.__products))
        except ZeroDivisionError:
            return 0

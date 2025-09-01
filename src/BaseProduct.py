from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """
    Абстрактный класс для класса продукта
    """

    @abstractmethod
    def new_product(cls, product: dict):
        pass

    @abstractmethod
    def price(self):
        pass

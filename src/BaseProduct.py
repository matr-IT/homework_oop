from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def new_product(cls, product: dict):
        pass

    @abstractmethod
    def price(self):
        pass

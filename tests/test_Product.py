import pytest

from src.Product import Product


@pytest.fixture
def sample_product():
    """Фикстура для создания продукта"""
    return Product("Телефон", "Смартфон", 50000.0, 10)


class TestProduct:
    def test_product_creation(self, sample_product):
        """Создание продукта через класс"""
        assert sample_product.name == "Телефон"
        assert sample_product.description == "Смартфон"
        assert sample_product.price == 50000.0
        assert sample_product.quantity == 10

    def test_product_creation_with_new_product(self):
        """Создание продукта через new_product"""
        product_data = {"name": "Ноутбук", "description": "Игровой ноутбук", "price": 100000.0, "quantity": 5}

        product = Product.new_product(product_data)

        assert product.name == "Ноутбук"
        assert product.description == "Игровой ноутбук"
        assert product.price == 100000.0
        assert product.quantity == 5

    def test_price_property_getter(self, sample_product):
        """Тест получения цены"""
        prod = sample_product

        assert prod.price == 50000.0

    def test_price_setter_increase(self, sample_product):
        """Тест увеличения цены"""
        prod = sample_product
        prod.price = 60000.0  # Увеличиваем цену

        assert prod.price == 60000.0

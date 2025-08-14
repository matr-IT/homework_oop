import pytest

from src.Product import Product


@pytest.fixture
def sample_product():
    """Фикстура для создания продукта"""
    return Product("Телефон", "Смартфон", 50000.0, 10)


class TestProduct:
    def test_product_creation(self, sample_product):
        assert sample_product.name == "Телефон"
        assert sample_product.description == "Смартфон"
        assert sample_product.price == 50000.0
        assert sample_product.quantity == 10

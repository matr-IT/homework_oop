import pytest

from src.Category import Category
from src.Product import Product


@pytest.fixture(autouse=True)
def reset_counters():
    """Автоматический сброс счетчиков перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def sample_products():
    """Фикстура для списка продуктов"""
    return [
        Product("Ноутбук", "Игровой ноутбук", 100000.0, 5),
        Product("Планшет", "Графический планшет", 30000.0, 8),
    ]


@pytest.fixture
def empty_category():
    """Фикстура для пустой категории"""
    return Category("Пустая", "Категория без товаров", [])


@pytest.fixture
def sample_category(sample_products):
    """Фикстура для категории с товарами"""
    return Category("Электроника", "Техника", sample_products)


class TestCategory:
    def test_category_creation(self, sample_category, sample_products):
        """Тест создания категории с продуктами"""
        assert sample_category.name == "Электроника"
        assert sample_category.description == "Техника"

    def test_empty_category(self, empty_category):
        assert empty_category.name == "Пустая"
        assert empty_category.description == "Категория без товаров"
        assert empty_category.products == ""

    def test_single_category_no_products(self, empty_category):
        """Создание категории без продуктов"""
        assert Category.category_count == 1
        assert Category.product_count == 0

    def test_add_product_to_category(self, empty_category):
        """Тест добавления продукта в категорию"""

        new_product = Product("Телефон", "Смартфон", 50000.0, 10)
        empty_category.add_product(new_product)

        products_str = empty_category.products
        assert "Телефон, 50000.0 руб. Остаток: 10 шт." in products_str
        assert Category.product_count == 1

    def test_single_category_with_products(self, sample_products):
        """Создание категории с несколькими продуктами"""
        category = Category("Электроника", "Техника", sample_products)
        assert Category.category_count == 1
        assert Category.product_count == 2

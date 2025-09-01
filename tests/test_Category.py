from logging import raiseExceptions

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
def not_a_product():
    """Фикстура для не-продукта"""
    return "Это не продукт"


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

        assert Category.product_count == 1

    def test_single_category_with_products(self, sample_products):
        """Создание категории с несколькими продуктами"""
        category = Category("Электроника", "Техника", sample_products)
        assert Category.category_count == 1
        assert Category.product_count == 2

    def test_str(self, sample_category, sample_products):
        """Тест пользовательского вывода категории"""
        samp = sample_category
        assert str(samp) == "Электроника, количество продуктов: 13 шт."

    def test_add_non_product_raises_type_error(self, empty_category, not_a_product):
        """Тест добавления не-продукта в категорию"""
        with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product и его наследников"):
            empty_category.add_product(not_a_product)

    def test_middle_price(self, sample_category):
        """Тест среднего ценника в категории"""
        assert sample_category.middle_price() == 65000

    def test_middle_price_empty_category(self, empty_category):
        """Тест среднего ценника в пустой категории"""
        assert empty_category.middle_price() == 0
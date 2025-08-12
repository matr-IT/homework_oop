import pytest


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
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

@pytest.fixture(autouse=True)
def reset_counters():
    """Автоматический сброс счетчиков перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0

@pytest.fixture
def sample_product():
    """Фикстура для создания продукта"""
    return Product("Телефон", "Смартфон", 50000.0, 10)


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


class TestProduct:
    def test_product_creation(self, sample_product):
        assert sample_product.name == "Телефон"
        assert sample_product.description == "Смартфон"
        assert sample_product.price == 50000.0
        assert sample_product.quantity == 10


class TestCategory:
    def test_category_creation(self, sample_category, sample_products):
        assert sample_category.name == "Электроника"
        assert sample_category.description == "Техника"
        assert sample_category.products == sample_products

    def test_empty_category(self, empty_category):
        assert empty_category.name == "Пустая"
        assert empty_category.description == "Категория без товаров"
        assert empty_category.products == []

    def test_initial_counters(self):
        """Проверка начального состояния счетчиков"""
        assert Category.category_count == 0
        assert Category.product_count == 0

    def test_single_category_no_products(self, empty_category):
        """Создание категории без продуктов"""
        assert Category.category_count == 1
        assert Category.product_count == 0

    def test_single_category_with_products(self, sample_products):
        """Создание категории с несколькими продуктами"""
        category = Category("Электроника", "Техника", sample_products)
        assert Category.category_count == 1
        assert Category.product_count == 2
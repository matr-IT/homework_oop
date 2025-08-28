import pytest

from src.Category import Category
from src.LawnGrass import LawnGrass
from src.Product import Product
from src.Smartphone import Smartphone


class TestSmartphone:
    @pytest.fixture
    def sample_smartphone(self):
        return Smartphone("Test Phone", "Test Description", 1000.0, 10, 95.0, "Test Model", 128, "Black")

    def test_smartphone_creation(self, sample_smartphone):
        assert sample_smartphone.name == "Test Phone"
        assert sample_smartphone.description == "Test Description"
        assert sample_smartphone.price == 1000.0
        assert sample_smartphone.quantity == 10
        assert sample_smartphone.efficiency == 95.0
        assert sample_smartphone.model == "Test Model"
        assert sample_smartphone.memory == 128
        assert sample_smartphone.color == "Black"

    def test_smartphone_addition(self):
        phone1 = Smartphone("Phone1", "Desc1", 1000.0, 2, 90.0, "M1", 64, "Black")
        phone2 = Smartphone("Phone2", "Desc2", 2000.0, 3, 95.0, "M2", 128, "White")

        result = phone1 + phone2
        expected = 1000.0 * 2 + 2000.0 * 3
        assert result == expected


class TestLawnGrass:
    @pytest.fixture
    def sample_lawn_grass(self):
        return LawnGrass("Test Grass", "Test Description", 500.0, 100, "Test Country", "14 дней", "Green")

    def test_lawn_grass_creation(self, sample_lawn_grass):
        assert sample_lawn_grass.name == "Test Grass"
        assert sample_lawn_grass.description == "Test Description"
        assert sample_lawn_grass.price == 500.0
        assert sample_lawn_grass.quantity == 100
        assert sample_lawn_grass.country == "Test Country"
        assert sample_lawn_grass.germination_period == "14 дней"
        assert sample_lawn_grass.color == "Green"

    def test_lawn_grass_addition(self):
        grass1 = LawnGrass("Grass1", "Desc1", 500.0, 10, "C1", "10 дней", "Green")
        grass2 = LawnGrass("Grass2", "Desc2", 300.0, 20, "C2", "7 дней", "Blue")

        result = grass1 + grass2
        expected = 500.0 * 10 + 300.0 * 20
        assert result == expected


class TestCategory:
    @pytest.fixture
    def sample_products(self):
        return [
            Smartphone("Phone1", "Desc1", 1000.0, 2, 90.0, "M1", 64, "Black"),
            LawnGrass("Grass1", "Desc2", 500.0, 10, "C1", "10 дней", "Green"),
        ]

    def test_category_creation(self, sample_products):
        category = Category("Test Category", "Test Description", sample_products)

        assert category.name == "Test Category"
        assert category.description == "Test Description"

    def test_add_invalid_product(self):
        category = Category("Test", "Test", [])

        with pytest.raises(TypeError):
            category.add_product("Not a product")

    def test_total_products_count(self):
        initial_count = Category.product_count
        products = [
            Smartphone("Phone1", "Desc1", 1000.0, 2, 90.0, "M1", 64, "Black"),
            LawnGrass("Grass1", "Desc2", 500.0, 10, "C1", "10 дней", "Green"),
        ]
        category = Category("Test", "Test", products)

        assert Category.product_count == initial_count + len(products)


class TestProductsAddition:
    def test_cross_category_addition(self):
        phone = Smartphone("Phone", "Desc", 1000.0, 2, 90.0, "M1", 64, "Black")
        grass = LawnGrass("Grass", "Desc", 500.0, 10, "C1", "10 дней", "Green")

        with pytest.raises(TypeError):
            phone + grass


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
        assert empty_category.products == None

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
        samp = sample_category
        assert str(samp) == "Электроника, количество продуктов: 13 шт."

    def test_add_non_product_raises_type_error(self, empty_category, not_a_product):
        """Тест добавления не-продукта в категорию"""
        with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product и его наследников"):
            empty_category.add_product(not_a_product)




@pytest.fixture
def sample_lawn_grass():
    """Фикстура для создания газонной травы"""
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


class TestLawnGrass:
    def test_lawn_grass_creation(self, sample_lawn_grass):
        """Создание газонной травы через класс"""
        assert sample_lawn_grass.name == "Газонная трава"
        assert sample_lawn_grass.description == "Элитная трава для газона"
        assert sample_lawn_grass.price == 500.0
        assert sample_lawn_grass.quantity == 20
        assert sample_lawn_grass.country == "Россия"
        assert sample_lawn_grass.germination_period == "7 дней"
        assert sample_lawn_grass.color == "Зеленый"

    def test_add(self, sample_lawn_grass):
        """Тест сложения Газонной травы"""
        grass1 = sample_lawn_grass
        grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
        assert LawnGrass.__add__(grass1, grass2) == 16750.0

    def test_str(self, sample_lawn_grass):
        """Тест пользовательского вывода"""
        grass = sample_lawn_grass
        assert str(grass) == "Газонная трава, 500.0 руб. Остаток: 20 шт."


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

    def test_str(self, sample_product):
        """Тест пользовательского вывода"""
        prod = sample_product
        assert str(prod) == "Телефон, 50000.0 руб. Остаток: 10 шт."

    def test_add(self, sample_product):
        """Тест сложения Продуктов"""
        prod = sample_product
        prod_2 = Product("Планшет", "Смартфон, но побольше", 80000.0, 13)
        assert Product.__add__(prod, prod_2) == 1540000


@pytest.fixture
def sample_smartphone():
    """Фикстура для создания смартфона"""
    return Smartphone(
        "iPhone 14 Pro", "256GB, Фиолетовый цвет, 48MP камера", 120000.0, 10, 90.5, "14 Pro", 256, "Фиолетовый"
    )


class TestSmartphone:
    def test_smartphone_initialization(self, sample_smartphone):
        """Тест инициализации объекта Smartphone"""
        assert sample_smartphone.name == "iPhone 14 Pro"
        assert sample_smartphone.description == "256GB, Фиолетовый цвет, 48MP камера"
        assert sample_smartphone.price == 120000.0
        assert sample_smartphone.quantity == 10
        assert sample_smartphone.efficiency == 90.5
        assert sample_smartphone.model == "14 Pro"
        assert sample_smartphone.memory == 256
        assert sample_smartphone.color == "Фиолетовый"

    def test_str_representation(self, sample_smartphone):
        """Тест строкового представления объекта Smartphone"""
        assert str(sample_smartphone) == "iPhone 14 Pro, 120000.0 руб. Остаток: 10 шт."

    def test_addition(self, sample_smartphone):
        """Тест сложения двух объектов Smartphone"""
        smartphone2 = Smartphone(
            "Samsung Galaxy S21", "128GB, Черный цвет, 64MP камера", 80000.0, 5, 85.0, "S21", 128, "Черный"
        )
        total_value = sample_smartphone + smartphone2
        assert total_value == (120000.0 * 10) + (80000.0 * 5)

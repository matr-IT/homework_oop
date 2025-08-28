import pytest
from src.Category import Category
from src.LawnGrass import LawnGrass
from src.Smartphone import Smartphone


class TestSmartphone:
    @pytest.fixture
    def sample_smartphone(self):
        return Smartphone(
            "Test Phone", "Test Description", 1000.0, 10,
            95.0, "Test Model", 128, "Black"
        )

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
        return LawnGrass(
            "Test Grass", "Test Description", 500.0, 100,
            "Test Country", "14 дней", "Green"
        )

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
            LawnGrass("Grass1", "Desc2", 500.0, 10, "C1", "10 дней", "Green")
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
            LawnGrass("Grass1", "Desc2", 500.0, 10, "C1", "10 дней", "Green")
        ]
        category = Category("Test", "Test", products)

        assert Category.product_count == initial_count + len(products)


class TestProductsAddition:
    def test_cross_category_addition(self):
        phone = Smartphone("Phone", "Desc", 1000.0, 2, 90.0, "M1", 64, "Black")
        grass = LawnGrass("Grass", "Desc", 500.0, 10, "C1", "10 дней", "Green")

        with pytest.raises(TypeError):
            phone + grass
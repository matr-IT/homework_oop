import pytest

from src.Smartphone import Smartphone


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

import pytest

from src.LawnGrass import LawnGrass


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

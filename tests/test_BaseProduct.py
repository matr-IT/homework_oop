from src.BaseProduct import BaseProduct
import pytest

class TestBaseProduct:

    def test_instantiate_abstract_class_fails(self):
        """Проверка, что нельзя создать экземпляр абстрактного класса."""
        with pytest.raises(TypeError):
            BaseProduct()  # Должно вызвать TypeError
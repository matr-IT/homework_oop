from src.MixinLog import MixinLog


# Тестовый класс для проверки работы MixinLog
class TestProduct(MixinLog):
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        super().__init__()


def test_mixin_log_output(capsys):
    """
    Тестирует вывод информации при создании объекта класса с миксином
    """
    # Создаем объект и перехватываем вывод
    product = TestProduct("Продукт1", "Описание продукта", 1200, 10)

    # Получаем перехваченный вывод
    captured = capsys.readouterr()
    output = captured.out.strip()

    # Проверяем, что вывод содержит имя класса
    assert output.startswith("TestProduct(")
    assert output.endswith(")")

    # Проверяем, что вывод содержит все атрибуты
    assert "'name': 'Продукт1'" in output
    assert "'description': 'Описание продукта'" in output
    assert "'price': 1200" in output
    assert "'quantity': 10" in output

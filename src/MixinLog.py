class MixinLog:
    """ "
    Класс-миксин для логирования создания экземпляров класса в консоль
    """

    def __init__(self, *args, **kwargs):
        print(self.__repr__())

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

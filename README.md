# Проект в рамках курса "Введение в ООП"

## Описание
Учебный проект по созданию интернет-магазина


## Требования к использованию

[Python ≥ 3.10](https://www.python.org/downloads/)

[Git](https://git-scm.com/book/ru/v2/%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%A3%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0-Git)

## Установка

1. Клонируйте репозиторий:

```commandline
git clone https://github.com/matr-IT/homework_oop
```

2. Создайте виртуальное окружение

```commandline
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Установите зависимости:

```commandline
pip install -r requirements.txt
```

## Функциональность

Реализована инициализация классов Product и Category:

Свойства Product:
1. название 
2. описание
3. цена
4. количество в наличии
 
Свойства Category:
1. название
2. описание
3. список товаров категории
4. Количество категорий
5. Количество продуктов

Реализована инициализация классов Smartphone и LawnGardenTech, наследующихся от Product:
Свойства Smartphone:
1. эффективность
2. модель
3. память
4. цвет

Свойства LawnGrass:
1. страна производитель
2. период созревания
3. цвет




### Покрытие кода

Цель: 80%+ покрытия основных модулей

```bash
pytest --cov=src --cov-report=html # Генерация отчета о покрытии
open htmlcov/index.html  # Просмотр отчета в браузере
```

## Команда проекта
Оставьте пользователям контакты и инструкции, как связаться с командой разработки.

- [Матвей Рыбин](https://github.com/matr-IT) — Back-End Engineer

## Лицензия
Проект распространяется под лицензией [MIT](https://license/).
Разрешается свободное использование при условии указания авторства.

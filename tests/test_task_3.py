import pytest
from src.Category import Category
from src.Product import Product


def test_product_initialization():
    product = Product("Test Product", "Description", 100.0, 10)
    assert product.name == "Test Product"
    assert product.description == "Description"
    assert product.price == 100.0
    assert product.quantity == 10


def test_product_str():
    product = Product("Test Product", "Description", 100.0, 10)
    expected_str = "Test Product, 100.0 руб. Остаток: 10 шт."
    assert str(product) == expected_str


def test_product_add():
    product1 = Product("Product1", "Desc1", 100.0, 2)
    product2 = Product("Product2", "Desc2", 200.0, 3)
    total_value = product1 + product2
    assert total_value == (100.0 * 2) + (200.0 * 3)


def test_category_initialization():
    products = [Product("Product1", "Desc1", 100.0, 2), Product("Product2", "Desc2", 200.0, 3)]
    category = Category("Test Category", "Description", products)
    assert category.name == "Test Category"
    assert category.description == "Description"


def test_category_str():
    products = [Product("Product1", "Desc1", 100.0, 2), Product("Product2", "Desc2", 200.0, 3)]
    category = Category("Test Category", "Description", products)
    expected_str = "Test Category, количество продуктов: 5 шт."
    assert str(category) == expected_str


def test_add_non_product():
    product = Product("Product", "Desc", 100.0, 2)
    with pytest.raises(TypeError):
        product + 100

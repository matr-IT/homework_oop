import unittest
from src.Category import Category
from src.Product import Product


class TestProduct(unittest.TestCase):
    def test_product_creation(self):
        product = Product("Test Product", "Test Description", 1000.0, 10)

        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.description, "Test Description")
        self.assertEqual(product.price, 1000.0)
        self.assertEqual(product.quantity, 10)

    def test_product_default_values(self):
        product = Product("Test Product", "Test Description", 1000.0, quantity=10)

        self.assertEqual(product.quantity, 10)


class TestCategory(unittest.TestCase):
    def setUp(self):
        # Сбрасываем счетчики перед каждым тестом
        Category.category_count = 0
        Category.product_count = 0

    def test_category_counters(self):
        product1 = Product("Product1", "Desc1", 100.0, 1)
        product2 = Product("Product2", "Desc2", 200.0, 2)

        category1 = Category("Category1", "Desc1", [product1])
        category2 = Category("Category2", "Desc2", [product2])

        self.assertEqual(Category.category_count, 2)
        self.assertEqual(Category.product_count, 2)


if __name__ == "__main__":
    unittest.main()

import unittest
from src.Category import Category
from src.Product import Product


class TestProduct(unittest.TestCase):
    def test_create_product(self):
        product = Product("Test", "Test desc", 1000.0, 10)
        self.assertEqual(product.name, "Test")
        self.assertEqual(product.description, "Test desc")
        self.assertEqual(product.price, 1000.0)
        self.assertEqual(product.quantity, 10)

    def test_new_product_alternative_constructor(self):
        data = {"name": "Test Product", "description": "Test Description", "price": 500.0, "quantity": 3}
        product = Product.new_product(data)
        self.assertIsInstance(product, Product)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.price, 500.0)


class TestCategory(unittest.TestCase):
    def setUp(self):
        self.products = [Product("Phone", "Smartphone", 50000.0, 10), Product("Tablet", "Tablet PC", 30000.0, 5)]
        self.category = Category("Electronics", "Electronic devices", self.products)

    def test_category_initialization(self):
        self.assertEqual(self.category.name, "Electronics")
        self.assertEqual(self.category.description, "Electronic devices")


if __name__ == "__main__":
    unittest.main()

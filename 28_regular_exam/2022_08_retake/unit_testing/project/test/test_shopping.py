from unittest import TestCase, main

from project.shopping_cart import ShoppingCart

if __name__ == "__main__":
    main()


class TestShoppingCart(TestCase):

    def setUp(self) -> None:
        self.cart = ShoppingCart("Test", 200)

    def test_init(self):
        self.assertEqual(self.cart.shop_name, "Test")
        self.assertEqual(self.cart.budget, 200)
        self.assertEqual(self.cart.products, {})

    def test_shop_name_not_start_with_upper_case(self):
        with self.assertRaises(ValueError) as ve:
            ShoppingCart("test1", 100)
        self.assertEqual(str(ve.exception), "Shop must contain only letters and must start with capital letter!")

    def test_add_to_cart_but_cost_too_much(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart("test", 100)
        self.assertEqual(str(ve.exception), "Product test cost too much!")

    def test_add_to_cart_valid(self):
        self.cart.add_to_cart("test", 50)
        self.assertEqual(self.cart.add_to_cart("testa", 40), "testa product was successfully added to the cart!")
        self.assertEqual(self.cart.products, {"test": 50, "testa": 40})

    def test_remove_from_cart_but_product_not_in_cart(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.remove_from_cart("test")
        self.assertEqual(str(ve.exception), "No product with name test in the cart!")

    def test_remove_from_cart_valid(self):
        self.cart.add_to_cart("test", 50)
        self.cart.add_to_cart("testa", 40)
        self.assertEqual(self.cart.products, {"test": 50, "testa": 40})
        self.assertEqual(self.cart.remove_from_cart("test"), "Product test was successfully removed from the cart!")
        self.assertEqual(self.cart.products, {"testa": 40})

    def test_add(self):
        self.cart.add_to_cart("test", 50)
        cart2 = ShoppingCart("Testa", 100)
        cart2.add_to_cart("test2", 50)
        result = self.cart.__add__(cart2)
        self.assertEqual(result.shop_name, "TestTesta")
        self.assertEqual(result.budget, 300)
        self.assertEqual(result.products, {"test": 50, "test2": 50})

    def test_buy_products_not_enough_money(self):
        self.cart.add_to_cart("test", 90)
        self.cart.add_to_cart("testa", 90)
        self.cart.add_to_cart("testb", 90)
        with self.assertRaises(ValueError) as ve:
            self.cart.buy_products()
        self.assertEqual(str(ve.exception), "Not enough money to buy the products! Over budget with 70.00lv!")

    def test_buy_products(self):
        self.cart.add_to_cart("test", 10)
        self.cart.add_to_cart("testa", 20)
        self.cart.add_to_cart("testb", 30)
        result = self.cart.buy_products()
        self.assertEqual(result, "Products were successfully bought! Total cost: 60.00lv.")

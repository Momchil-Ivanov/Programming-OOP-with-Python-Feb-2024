from unittest import TestCase, main

from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):

    def setUp(self):
        self.car = SecondHandCar('Opel', 'astra', 200, 1000)

    def test_init(self):
        self.assertEqual(self.car.model, 'Opel')
        self.assertEqual(self.car.car_type, 'astra')
        self.assertEqual(self.car.mileage, 200)
        self.assertEqual(self.car.price, 1000)
        self.assertEqual(self.car.repairs, [])

    def test_price_if_lower_or_equal_to_one(self):
        with self.assertRaises(ValueError) as ex:
            self.car.price = 1
        self.assertEqual(str(ex.exception), 'Price should be greater than 1.0!')

    def test_if_mileage_is_lower_or_equal_to_hundred(self):
        with self.assertRaises(ValueError) as ex:
            self.car.mileage = 99
        self.assertEqual(str(ex.exception), 'Please, second-hand cars only! Mileage must be greater than 100!')

    def test_promotional_price_higher_than_original_price(self):
        with self.assertRaises(ValueError) as ex:
            self.car.set_promotional_price(1100)
        self.assertEqual(str(ex.exception), 'You are supposed to decrease the price!')

    def test_valid_promotional_price(self):
        self.car.set_promotional_price(900)
        self.assertEqual(self.car.price, 900)
        self.assertEqual(self.car.set_promotional_price(800), 'The promotional price has been successfully set.')

    def test_need_repair_if_price_is_higher_than_half_and_repair_is_impossible(self):
        self.assertEqual(self.car.need_repair(10000, 'a'), 'Repair is impossible!')

    def test_need_repair_if_price_lower_than_half_and_repair_is_possible(self):
        self.assertEqual(self.car.need_repair(500, 'a'), 'Price has been increased due to repair charges.')
        self.assertEqual(self.car.price, 1500)
        self.assertEqual(self.car.repairs, ['a'])

    def test_greater_than_if_car_type_mismatch(self):
        other = SecondHandCar('Opel', 'omega', 200, 1000)
        self.assertEqual(self.car.__gt__(other), 'Cars cannot be compared. Type mismatch!')

    def test_greater_than_if_car_type_match(self):
        other = SecondHandCar('Opel', 'astra', 200, 1100)
        self.assertEqual(self.car.__gt__(other), False)

    def test_str(self):
        self.assertEqual(str(self.car), f"""Model {self.car.model} | Type {self.car.car_type} | Milage {self.car.mileage}km
Current price: {self.car.price:.2f} | Number of Repairs: {len(self.car.repairs)}""")


if __name__ == '__main__':
    main()
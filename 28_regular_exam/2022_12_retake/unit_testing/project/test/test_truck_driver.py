from unittest import TestCase, main

from project.truck_driver import TruckDriver

if __name__ == "__main__":
    main()


class TestTruckDriver(TestCase):

    def setUp(self):
        self.truck_driver = TruckDriver("Ivan", 2)

    def test_init(self):
        self.assertEqual(self.truck_driver.name, "Ivan")
        self.assertEqual(self.truck_driver.money_per_mile, 2)
        self.assertEqual(self.truck_driver.earned_money, 0)
        self.assertEqual(self.truck_driver.miles, 0)
        self.assertEqual(self.truck_driver.available_cargos, {})

    def test_earned_money_if_lower_than_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.truck_driver.earned_money = -1
        self.assertEqual(str(ve.exception), f"Ivan went bankrupt.")

    def test_bankrupt(self):
        self.truck_driver.money_per_mile = 0.01
        self.truck_driver.add_cargo_offer("California", 2000)

        with self.assertRaises(ValueError) as ve:
            self.truck_driver.drive_best_cargo_offer()

        self.assertEqual(str(ve.exception), f"{self.truck_driver.name} went bankrupt.")

    def test_add_cargo_offer_if_cargo_offer_is_already_added(self):
        self.truck_driver.add_cargo_offer("Iasi", 10)
        with self.assertRaises(Exception) as ex:
            self.truck_driver.add_cargo_offer("Iasi", 10)
        self.assertEqual(str(ex.exception), "Cargo offer is already added.")

    def test_add_cargo_offer_successfully(self):
        result = self.truck_driver.add_cargo_offer("Iasi", 10)
        self.assertEqual(self.truck_driver.available_cargos, {"Iasi": 10})
        self.assertEqual(result, "Cargo for 10 to Iasi was added as an offer.")

    def test_drive_best_cargo_offer_but_no_offers_available(self):
        result = self.truck_driver.drive_best_cargo_offer()
        self.assertEqual(result, "There are no offers available.")

    def test_drive_best_cargo_offer_successfully(self):
        self.truck_driver.add_cargo_offer("Iasi", 10000)
        self.truck_driver.add_cargo_offer("Sofia", 5000)
        result = self.truck_driver.drive_best_cargo_offer()
        self.assertEqual(result, "Ivan is driving 10000 to Iasi.")
        self.assertEqual(self.truck_driver.earned_money, 8250)
        self.assertEqual(self.truck_driver.miles, 10000)

    def test_eat(self):
        self.truck_driver.earned_money = 100

        self.truck_driver.eat(250)
        self.truck_driver.eat(500)

        self.assertEqual(self.truck_driver.earned_money, 60)

    def test_sleep(self):
        self.truck_driver.earned_money = 100

        self.truck_driver.sleep(1000)
        self.truck_driver.sleep(2000)

        self.assertEqual(self.truck_driver.earned_money, 10)

    def test_pump_gas(self):
        self.truck_driver.earned_money = 2000

        self.truck_driver.pump_gas(1500)
        self.truck_driver.pump_gas(3000)

        self.assertEqual(self.truck_driver.earned_money, 1000)

    def repair_truck(self):
        self.truck_driver.earned_money = 16000

        self.truck_driver.repair_truck(10000)
        self.truck_driver.repair_truck(20000)

        self.assertEqual(self.truck_driver.earned_money, 1000)

    def test_repr(self):
        result = str(self.truck_driver)
        self.assertEqual(result, f"Ivan has 0 miles behind his back.")










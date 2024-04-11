from unittest import TestCase, main

from project.robot import Robot

if __name__ == '__main__':
    main()


class TestRobot(TestCase):

    def setUp(self) -> None:
        self.robot = Robot("Tester", "Military", 100, 1000.0)
        self.robot_with_upgrades_and_updates = Robot("TesterUpgradedUpdated", "Military", 100, 1000.0)
        self.robot_with_upgrades_and_updates.upgrade("Test", 10)
        self.robot_with_upgrades_and_updates.update(1.0, 10)


    def test_init(self):
        self.assertEqual(self.robot.robot_id, "Tester")
        self.assertEqual(self.robot.category, "Military")
        self.assertEqual(self.robot.available_capacity, 100)
        self.assertEqual(self.robot.price, 1000.0)
        self.assertEqual(self.robot.hardware_upgrades, [])
        self.assertEqual(self.robot.software_updates, [])

    def test_when_category_invalid(self):
        with self.assertRaises(ValueError) as ex:
            self.robot.category = "Test"
        self.assertEqual(str(ex.exception), "Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'")

    def test_when_price_invalid_negative(self):
        with self.assertRaises(ValueError) as ex:
            self.robot.price = -1
        self.assertEqual(str(ex.exception), "Price cannot be negative!")

    def test_if_upgrade_is_invalid(self):
        result = self.robot_with_upgrades_and_updates.upgrade("Test", 10)
        self.assertEqual(result, "Robot TesterUpgradedUpdated was not upgraded.")
        self.assertEqual(self.robot_with_upgrades_and_updates.hardware_upgrades, ["Test"])
        self.assertEqual(self.robot_with_upgrades_and_updates.price, 1015.0)

    def test_if_upgrade_is_valid(self):
        result = self.robot_with_upgrades_and_updates.upgrade("TestSecond", 10)
        self.assertEqual(result, "Robot TesterUpgradedUpdated was upgraded with TestSecond.")
        self.assertEqual(self.robot_with_upgrades_and_updates.hardware_upgrades, ["Test", "TestSecond"])
        self.assertEqual(self.robot_with_upgrades_and_updates.price, 1030.0)

        result = self.robot.upgrade("Test", 10)
        self.assertEqual(result, "Robot Tester was upgraded with Test.")
        self.assertEqual(self.robot.hardware_upgrades, ["Test"])
        self.assertEqual(self.robot.price, 1015.0)

    def test_if_update_is_invalid_version(self):
        result = self.robot_with_upgrades_and_updates.update(1.0, 10)
        self.assertEqual(result, "Robot TesterUpgradedUpdated was not updated.")
        self.assertEqual(self.robot_with_upgrades_and_updates.software_updates, [1.0])
        self.assertEqual(self.robot_with_upgrades_and_updates.available_capacity, 90)

    def test_if_update_is_invalid_capacity(self):
        result = self.robot_with_upgrades_and_updates.update(2.0, 100)
        self.assertEqual(result, "Robot TesterUpgradedUpdated was not updated.")
        self.assertEqual(self.robot_with_upgrades_and_updates.software_updates, [1.0])
        self.assertEqual(self.robot_with_upgrades_and_updates.available_capacity, 90)

    def test_if_update_is_valid(self):
        result = self.robot_with_upgrades_and_updates.update(2.0, 10)
        self.assertEqual(result, "Robot TesterUpgradedUpdated was updated to version 2.0.")
        self.assertEqual(self.robot_with_upgrades_and_updates.software_updates, [1.0, 2.0])
        self.assertEqual(self.robot_with_upgrades_and_updates.available_capacity, 80)

        result = self.robot.update(2.0, 10)
        self.assertEqual(result, "Robot Tester was updated to version 2.0.")
        self.assertEqual(self.robot.software_updates, [2.0])
        self.assertEqual(self.robot.available_capacity, 90)

    def test_greater_than_if_price_is_more_expensive(self):
        other_robot = Robot("Other", "Military", 100, 900.0)
        result = self.robot > other_robot
        self.assertEqual(result, f'Robot with ID Tester is more expensive than Robot with ID Other.')

    def test_greater_than_if_price_is_equally_expensive(self):
        other_robot = Robot("Other", "Military", 100, 1000.0)
        result = self.robot > other_robot
        self.assertEqual(result, f'Robot with ID Tester costs equal to Robot with ID Other.')

    def test_greater_than_if_price_is_cheaper(self):
        other_robot = Robot("Other", "Military", 100, 1100.0)
        result = self.robot > other_robot
        self.assertEqual(result, f'Robot with ID Tester is cheaper than Robot with ID Other.')

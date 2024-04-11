from unittest import TestCase, main

from project.climbing_robot import ClimbingRobot

if __name__ == '__main__':
    main()


class TestClimbingRobot(TestCase):
    def setUp(self):
        self.robot = ClimbingRobot('Mountain', 'Helper', 100, 200)

        self.robot_with_software = ClimbingRobot('Mountain', 'Helper', 100, 200)
        self.robot_with_software.installed_software = [{'name': 'PyCharm', 'capacity_consumption': 50, 'memory_consumption': 49}, {'name': 'CLion', 'capacity_consumption': 49, 'memory_consumption': 51}]

    def test_init(self):
        self.assertEqual(self.robot.category, 'Mountain')
        self.assertEqual(self.robot.part_type, 'Helper')
        self.assertEqual(self.robot.capacity, 100)
        self.assertEqual(self.robot.memory, 200)
        self.assertEqual(self.robot.installed_software, [])

    def test_category(self):
        with self.assertRaises(ValueError) as ex:
            self.robot.category = 'BoulderingA'
        self.assertEqual(str(ex.exception), "Category should be one of ['Mountain', 'Alpine', 'Indoor', 'Bouldering']")

    def test_get_used_capacity_success(self):
        expected_result = sum(s['capacity_consumption'] for s in self.robot_with_software.installed_software)
        result = self.robot_with_software.get_used_capacity()
        self.assertEqual(result, expected_result)

    def test_get_available_capacity_success(self):
        expected_result = self.robot_with_software.capacity - self.robot_with_software.get_used_capacity()
        result = self.robot_with_software.get_available_capacity()
        self.assertEqual(result, expected_result)

    def test_get_used_memory_success(self):
        expected_result = sum(s['memory_consumption'] for s in self.robot_with_software.installed_software)
        result = self.robot_with_software.get_used_memory()
        self.assertEqual(result, expected_result)

    def test_get_available_memory(self):
        expected_result = self.robot_with_software.memory - self.robot_with_software.get_used_memory()
        result = self.robot_with_software.get_available_memory()
        self.assertEqual(result, expected_result)

    def test_install_software_with_max_equal_values_valid(self):
        result = self.robot.install_software({'name': 'PyCharm', 'capacity_consumption': 100, 'memory_consumption': 200})

        self.assertEqual(result, f"Software 'PyCharm' successfully installed on Mountain part.")
        self.assertEqual(self.robot.installed_software, [{'name': 'PyCharm', 'capacity_consumption': 100, 'memory_consumption': 200}])

    def test_install_software_with_less_than_max_values_valid(self):
        result = self.robot.install_software({'name': 'PyCharm', 'capacity_consumption': 10, 'memory_consumption': 20})

        self.assertEqual(result, f"Software 'PyCharm' successfully installed on Mountain part.")
        self.assertEqual(self.robot.installed_software, [{'name': 'PyCharm', 'capacity_consumption': 10, 'memory_consumption': 20}])

    def test_install_software_with_one_value_greater_than_max_values_invalid(self):
        result = self.robot.install_software({'name': 'PyCharm', 'capacity_consumption': 10, 'memory_consumption': 2000})

        self.assertEqual(result, f"Software 'PyCharm' cannot be installed on Mountain part.")
        self.assertEqual(self.robot.installed_software, [])

    def test_install_software_with_two_values_greater_than_max_values_invalid(self):
        result = self.robot_with_software.install_software({'name': 'PyCharm', 'capacity_consumption': 49, 'memory_consumption': 50})

        self.assertEqual(result, f"Software 'PyCharm' cannot be installed on Mountain part.")
        self.assertEqual(self.robot_with_software.installed_software, [{'name': 'PyCharm', 'capacity_consumption': 50, 'memory_consumption': 49}, {'name': 'CLion', 'capacity_consumption': 49, 'memory_consumption': 51}])

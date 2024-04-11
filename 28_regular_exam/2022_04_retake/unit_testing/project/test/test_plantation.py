from unittest import TestCase, main

from project.plantation import Plantation

if __name__ == '__main__':
    main()


class TestPlantation(TestCase):

    def setUp(self) -> None:
        self.plantation = Plantation(2)

    def test_init(self):
        self.assertEqual(2, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_if_size_is_negative(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -1
        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_hire_worker(self):
        self.assertEqual([], self.plantation.workers)
        self.assertEqual(0, len(self.plantation))
        self.plantation.hire_worker("Ivan")
        self.assertEqual(["Ivan"], self.plantation.workers)
        self.assertEqual(1, len(self.plantation.workers))

    def test_hire_worker_already_hired_raises(self):
        self.plantation.hire_worker("Ivan")
        self.assertEqual(["Ivan"], self.plantation.workers)
        self.assertEqual(1, len(self.plantation.workers))

        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Ivan")
        self.assertEqual("Worker already hired!", str(ve.exception))
        self.assertEqual(["Ivan"], self.plantation.workers)
        self.assertEqual(1, len(self.plantation.workers))

    def test_len(self):
        self.plantation.size = 3
        self.plantation.hire_worker("Ivan")
        self.plantation.planting("Ivan", "potato")
        self.assertEqual(1, len(self.plantation))
        self.plantation.planting("Ivan", "tomato")
        self.assertEqual(2, len(self.plantation))
        self.plantation.hire_worker("Ivanka")
        self.plantation.planting("Ivanka", "carrot")
        self.assertEqual(3, len(self.plantation))

    def test_planting_working_doesnt_exist(self):
        self.plantation.hire_worker("Ivan")
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Ivanka", "potato")
        self.assertEqual("Worker with name Ivanka is not hired!", str(ve.exception))

    def test_planting_plantation_is_full_raises(self):
        self.plantation.size = 0
        self.plantation.hire_worker("Ivan")
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Ivan", "tomato")
        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_planting(self):
        self.assertEqual({}, self.plantation.plants)
        result = self.plantation.hire_worker("Ivan")
        self.assertEqual("Ivan successfully hired.", result)
        result_for_planting = self.plantation.planting("Ivan", "potato")
        self.assertEqual({"Ivan": ["potato"]}, self.plantation.plants)
        self.assertEqual("Ivan planted it's first potato.", result_for_planting)
        result_for_planting_second = self.plantation.planting("Ivan", "tomato")
        self.assertEqual({"Ivan": ["potato", "tomato"]}, self.plantation.plants)
        self.assertEqual("Ivan planted tomato.", result_for_planting_second)

    def test_str(self):
        self.plantation.hire_worker("Ivan")
        self.plantation.planting("Ivan", "potato")
        self.plantation.hire_worker("Ivanka")
        self.plantation.planting("Ivanka", "tomato")

        result = str(self.plantation)

        expected = "Plantation size: 2\nIvan, Ivanka\nIvan planted: potato\nIvanka planted: tomato"
        self.assertEqual(expected, result)

        self.plantation.plants = {}
        self.plantation.planting("Ivan", "potato")
        self.plantation.planting("Ivan", "tomato")

        result = str(self.plantation)
        expected = "Plantation size: 2\nIvan, Ivanka\nIvan planted: potato, tomato"
        self.assertEqual(expected, result)

    def test_repr(self):
        self.plantation.hire_worker("Ivan")
        self.plantation.hire_worker("Ivanka")

        result = repr(self.plantation)
        expected = "Size: 2\nWorkers: Ivan, Ivanka"
        self.assertEqual(expected, result)

from unittest import TestCase, main

from first_worker import Worker


class TestWorker(TestCase):

    def setUp(self):  # runs before each testcase
        self.worker = Worker('TestGuy', 25_000, 100)

    def test_correct_init(self):
        self.assertEqual(self.worker.name, 'TestGuy')
        self.assertEqual(self.worker.salary, 25_000)
        self.assertEqual(self.worker.energy, 100)
        self.assertEqual(self.worker.money, 0)

    def test_work_when_worker_has_energy_expect_money_increase_and_energy_decrease(self):
        expected_money = self.worker.salary * 2
        expected_energy = self.worker.energy - 2

        self.worker.work()
        self.worker.work()

        self.assertEqual(self.worker.money, expected_money)
        self.assertEqual(self.worker.energy, expected_energy)

    def test_work_when_worker_does_not_have_energy_raise_exception(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_rest_increases_energy_with_one(self):
        expected_energy = self.worker.energy + 1
        self.worker.rest()
        self.assertEqual(self.worker.energy, expected_energy)

    def test_get_info_returns_correct_string(self):
        self.assertEqual(self.worker.get_info(), f'TestGuy has saved 0 money.')


if __name__ == '__main__':
    main()

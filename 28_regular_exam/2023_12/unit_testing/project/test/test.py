from collections import deque
from unittest import TestCase, main

from project.railway_station import RailwayStation

if __name__ == "__main__":
    main()


class TestRailwayStation(TestCase):

    def setUp(self) -> None:
        self.rs = RailwayStation("TrainStation")

        self.rs_with_trains = RailwayStation("TrainStation_with_trains")
        self.rs_with_trains.arrival_trains.append("Train")
        self.rs_with_trains.arrival_trains.append("TrainSecond")
        self.rs_with_trains.arrival_trains.append("TrainThird")
        self.rs_with_trains.departure_trains.append("TrainOld")

    def test_init(self):
        self.assertEqual(self.rs.name, "TrainStation")
        self.assertEqual(self.rs.arrival_trains, deque())
        self.assertEqual(self.rs.departure_trains, deque())

    def test_name_when_less_than_three_symbols_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            RailwayStation("a")
        self.assertEqual(str(ve.exception), "Name should be more than 3 symbols!")

    def test_new_arrival_on_board_first_arrival(self):
        self.rs.new_arrival_on_board("Train")
        self.assertEqual(self.rs.arrival_trains, deque(["Train"]))

    def test_new_arrival_on_board_another_arrival(self):
        self.rs_with_trains.new_arrival_on_board("TrainForth")
        self.assertEqual(self.rs_with_trains.arrival_trains, deque(["Train", "TrainSecond", "TrainThird", "TrainForth"]))

    def test_train_has_arrived_but_other_trains_to_arrive(self):
        result = self.rs_with_trains.train_has_arrived("TrainSecond")
        expected = f"There are other trains to arrive before TrainSecond."
        self.assertEqual(result, expected)
        self.assertEqual(self.rs_with_trains.departure_trains, deque(["TrainOld"]))

    def test_train_has_arrived_no_other_trains_to_arrive(self):
        result = self.rs_with_trains.train_has_arrived("Train")
        expected = f"Train is on the platform and will leave in 5 minutes."
        self.assertEqual(result, expected)
        self.assertEqual(self.rs_with_trains.departure_trains, deque(["TrainOld", "Train"]))

    def test_train_has_left(self):
        result = self.rs_with_trains.train_has_left("TrainOld")
        self.assertEqual(self.rs_with_trains.departure_trains, deque([]))
        self.assertEqual(result, True)

    def test_train_has_left_not(self):
        result = self.rs_with_trains.train_has_left("Train")
        self.assertEqual(self.rs_with_trains.departure_trains, deque(["TrainOld"]))
        self.assertEqual(result, False)

from unittest import TestCase, main

from project.trip import Trip


class TestTrip(TestCase):

    def setUp(self):
        self.t1f = Trip(10000, 1, False)
        self.t2f = Trip(10000, 2, False)
        self.t2t = Trip(10000, 2, True)

    def test_init_trip(self):
        self.assertEqual(self.t1f.budget, 10000)
        self.assertEqual(self.t1f.travelers, 1)
        self.assertEqual(self.t1f.is_family, False)
        self.assertEqual(self.t1f.booked_destinations_paid_amounts, {})

    def test_setter_travelers(self):
        with self.assertRaises(ValueError) as ex:
            self.t1f.travelers = 0
        self.assertEqual(str(ex.exception), 'At least one traveler is required!')

    def test_setter_is_family(self):
        self.assertTrue(self.t2t.is_family)

        self.t1f.is_family = True
        self.assertFalse(self.t1f.is_family)

    def test_book_a_trip_not_in_offers(self):
        self.assertEqual(self.t1f.book_a_trip('USA'), 'This destination is not in our offers, please choose a new one!')

    def test_book_a_trip_not_enough_budget(self):
        self.assertEqual(self.t2t.book_a_trip('New Zealand'), 'Your budget is not enough!')

    def test_book_a_trip_successfully_no_family_discounts(self):
        self.assertEqual(self.t1f.book_a_trip('New Zealand'), 'Successfully booked destination New Zealand! Your budget left is 2500.00')
        self.assertEqual(self.t1f.budget, 2500)
        self.assertEqual(self.t1f.booked_destinations_paid_amounts, {'New Zealand': 7500})

    def test_book_a_trip_successfully_with_family_discounts(self):
        self.assertEqual(self.t2t.book_a_trip('Bulgaria'), 'Successfully booked destination Bulgaria! Your budget left is 9100.00')
        self.assertEqual(self.t2t.budget, 9100)
        self.assertEqual(self.t2t.booked_destinations_paid_amounts, {'Bulgaria': 900})

    def test_booking_status_no_bookings(self):
        self.assertEqual(self.t1f.booking_status(), 'No bookings yet. Budget: 10000.00')

    def test_booking_status_with_bookings(self):
        self.t2f.budget = 100000
        self.t2f.book_a_trip('New Zealand')
        self.t2f.book_a_trip('Brazil')
        expected = """Booked Destination: Brazil
Paid Amount: 12400.00
Booked Destination: New Zealand
Paid Amount: 15000.00
Number of Travelers: 2
Budget Left: 72600.00"""
        result = self.t2f.booking_status()
        self.assertEqual(result, expected)


if __name__ == "__main__":
    main()

from unittest import TestCase, main

from project.bookstore import Bookstore

if __name__ == "__main__":
    main()


class TestBookstore(TestCase):

    def setUp(self) -> None:
        self.bookstore = Bookstore(20)

    def test_init(self):
        self.assertEqual(self.bookstore.books_limit, 20)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {})
        self.assertEqual(self.bookstore.total_sold_books, 0)

    def test_total_sold_books(self):
        self.assertEqual(self.bookstore.total_sold_books, 0)

    def test_if_books_limit_is_equal_or_below_zero(self):
        with self.assertRaises(ValueError) as ex:
            Bookstore(0)
        self.assertEqual(str(ex.exception), "Books limit of 0 is not valid")

    def test_len(self):
        self.assertEqual(len(self.bookstore), 0)
        self.bookstore.availability_in_store_by_book_titles["test"] = 5
        self.assertEqual(len(self.bookstore), 5)

    def test_receive_book_but_book_limit_is_reached(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("test", 21)
        self.assertEqual(str(ex.exception), "Books limit is reached. Cannot receive more books!")

    def test_receive_book_valid(self):
        self.bookstore.availability_in_store_by_book_titles["test"] = 5
        self.assertEqual(self.bookstore.receive_book("test", 5), "10 copies of test are available in the bookstore.")
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles["test"], 10)

    def test_sell_book_but_title_doesn_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("test", 5)
        self.assertEqual(str(ex.exception), "Book test doesn't exist!")

    def test_sell_book_but_not_enough_copies(self):
        self.bookstore.availability_in_store_by_book_titles["test"] = 5
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("test", 6)
        self.assertEqual(str(ex.exception), "test has not enough copies to sell. Left: 5")

    def test_sell_book_valid(self):
        self.bookstore.availability_in_store_by_book_titles["test"] = 5
        self.assertEqual(self.bookstore.sell_book("test", 5), "Sold 5 copies of test")
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles["test"], 0)

    def test_str(self):
        self.bookstore.receive_book("test", 5)
        self.bookstore.receive_book("test2", 10)
        self.bookstore.sell_book("test2", 5)
        result = self.bookstore.__str__()
        expected = f"Total sold books: 5\nCurrent availability: 10\n - test: 5 copies\n - test2: 5 copies"
        self.assertEqual(result, expected)


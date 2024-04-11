from unittest import TestCase, main

from project.toy_store import ToyStore

if __name__ == "__main__":
    main()


class TestToyStore(TestCase):

    def setUp(self):
        self.toy_store = ToyStore()

    def test_init(self):
        self.assertEqual(self.toy_store.toy_shelf, {"A": None, "B": None, "C": None, "D": None, "E": None, "F": None, "G": None})

    def test_add_toy_but_shelf_does_not_exist_raise_exception(self):
        self.assertEqual(self.toy_store.toy_shelf, {"A": None, "B": None, "C": None, "D": None, "E": None, "F": None, "G": None})
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("Z", "Doll")
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")
        self.assertEqual(self.toy_store.toy_shelf, {"A": None, "B": None, "C": None, "D": None, "E": None, "F": None, "G": None})

    def test_add_toy_but_toy_is_already_in_shelf_raise_exception(self):
        self.toy_store.toy_shelf = {"A": 'Doll', "B": None, "C": None, "D": None, "E": None, "F": None, "G": None}
        self.assertEqual(self.toy_store.toy_shelf, {"A": 'Doll', "B": None, "C": None, "D": None, "E": None, "F": None, "G": None})
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "Doll")
        self.assertEqual(str(ex.exception), "Toy is already in shelf!")
        self.assertEqual(self.toy_store.toy_shelf, {"A": 'Doll', "B": None, "C": None, "D": None, "E": None, "F": None, "G": None})

    def test_add_toy_but_shelf_is_already_taken_raise_exception(self):
        self.toy_store.toy_shelf = {"A": 'Doll', "B": None, "C": None, "D": None, "E": None, "F": None, "G": None}
        self.assertEqual(self.toy_store.toy_shelf, {"A": 'Doll', "B": None, "C": None, "D": None, "E": None, "F": None, "G": None})
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "Spider")
        self.assertEqual(str(ex.exception), "Shelf is already taken!")
        self.assertEqual(self.toy_store.toy_shelf, {"A": 'Doll', "B": None, "C": None, "D": None, "E": None, "F": None, "G": None})

    def test_add_toy_successfully(self):
        self.toy_store.toy_shelf = {"A": None, "B": None, "C": None, "D": None, "E": None, "F": None, "G": None}
        self.assertEqual(self.toy_store.toy_shelf, {"A": None, "B": None, "C": None, "D": None, "E": None, "F": None, "G": None})
        result = self.toy_store.add_toy("A", "Doll")
        self.assertEqual(result, "Toy:Doll placed successfully!")
        self.assertEqual(self.toy_store.toy_shelf, {"A": "Doll", "B": None, "C": None, "D": None, "E": None, "F": None, "G": None})

    def test_remove_toy_but_shelf_does_not_exist_raise_exception(self):
        self.toy_store.toy_shelf = {"A": 'Doll', "B": None, "C": None, "D": None, "E": None, "F": None, "G": None}
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("Z", "Doll")
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")
        self.assertEqual(self.toy_store.toy_shelf, {"A": 'Doll', "B": None, "C": None, "D": None, "E": None, "F": None, "G": None})

    def test_remove_toy_but_toy_is_not_in_shelf_raise_exception(self):
        self.toy_store.toy_shelf = {"A": 'Doll', "B": None, "C": None, "D": None, "E": None, "F": None, "G": None}
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("A", "Spider")
        self.assertEqual(str(ex.exception), "Toy in that shelf doesn't exists!")
        self.assertEqual(self.toy_store.toy_shelf, {"A": 'Doll', "B": None, "C": None, "D": None, "E": None, "F": None, "G": None})

    def test_remove_toy_successfully(self):
        self.toy_store.toy_shelf = {"A": 'Doll', "B": None, "C": None, "D": None, "E": None, "F": None, "G": None}
        self.assertEqual(self.toy_store.toy_shelf, {"A": 'Doll', "B": None, "C": None, "D": None, "E": None, "F": None, "G": None})
        result = self.toy_store.remove_toy("A", "Doll")
        self.assertEqual(result, "Remove toy:Doll successfully!")
        self.assertEqual(self.toy_store.toy_shelf, {"A": None, "B": None, "C": None, "D": None, "E": None, "F": None, "G": None})

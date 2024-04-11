from unittest import TestCase, main

from project.pet_shop import PetShop

if __name__ == '__main__':
    main()


class TestPetShop(TestCase):

    def setUp(self) -> None:
        self.pet_shop = PetShop('Pet Shop')

    def test_init(self):
        self.assertEqual('Pet Shop', self.pet_shop.name)
        self.assertEqual({}, self.pet_shop.food)
        self.assertEqual([], self.pet_shop.pets)

    def test_add_food_but_quantity_is_not_valid(self):
        with self.assertRaises(ValueError) as ve:
            self.pet_shop.add_food('food', 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ve.exception))

    def test_add_food_valid(self):
        result = self.pet_shop.add_food('food', 10)
        self.assertEqual('Successfully added 10.00 grams of food.', result)
        self.assertEqual({'food': 10.00}, self.pet_shop.food)

        result = self.pet_shop.add_food('food_second', 20)
        self.assertEqual('Successfully added 20.00 grams of food_second.', result)
        self.assertEqual({'food': 10.00, 'food_second': 20.00}, self.pet_shop.food)

    def test_add_pet_but_already_existing_raise_exception(self):
        self.pet_shop.add_pet('Pet')
        self.assertEqual(['Pet'], self.pet_shop.pets)
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet('Pet')
        self.assertEqual('Cannot add a pet with the same name', str(ex.exception))
        self.assertEqual(['Pet'], self.pet_shop.pets)

    def test_add_pet_valid(self):
        result = self.pet_shop.add_pet('Pet')
        self.assertEqual('Successfully added Pet.', result)
        self.assertEqual(['Pet'], self.pet_shop.pets)

        result = self.pet_shop.add_pet('Pet_second')
        self.assertEqual('Successfully added Pet_second.', result)
        self.assertEqual(['Pet', 'Pet_second'], self.pet_shop.pets)

    def test_feed_pet_not_existing_pet_raise_exception(self):
        self.pet_shop.add_pet('Pet')
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet('food', 'Pet_second')
        self.assertEqual('Please insert a valid pet name', str(ex.exception))
        self.assertEqual(['Pet'], self.pet_shop.pets)

    def test_feed_pet_not_existing_food_raise_exception(self):
        self.pet_shop.add_pet('Pet')
        self.pet_shop.add_food('food', 10)
        result = self.pet_shop.feed_pet('food_second', 'Pet')
        self.assertEqual('You do not have food_second', result)
        self.assertEqual(['Pet'], self.pet_shop.pets)
        self.assertEqual({'food': 10.00}, self.pet_shop.food)

    def test_feed_pet_not_enough_food(self):
        self.pet_shop.add_pet('Pet')
        self.pet_shop.add_food('food', 10)
        result = self.pet_shop.feed_pet('food', 'Pet')
        self.assertEqual('Adding food...', result)
        self.assertEqual(['Pet'], self.pet_shop.pets)
        self.assertEqual({'food': 1010.00}, self.pet_shop.food)

    def test_feed_pet_valid(self):
        self.pet_shop.add_pet('Pet')
        self.pet_shop.add_food('food', 110)
        result = self.pet_shop.feed_pet('food', 'Pet')
        self.assertEqual('Pet was successfully fed', result)
        self.assertEqual(['Pet'], self.pet_shop.pets)
        self.assertEqual({'food': 10.00}, self.pet_shop.food)

    def test_repr(self):
        self.pet_shop.add_pet('Pet')
        self.pet_shop.add_pet('Pet_second')
        self.pet_shop.add_food('food', 10)
        self.pet_shop.add_food('food_second', 20)
        result = self.pet_shop.__repr__()
        self.assertEqual('Shop Pet Shop:\nPets: Pet, Pet_second', result)

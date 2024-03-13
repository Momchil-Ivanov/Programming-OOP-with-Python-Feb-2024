from abc import ABC, abstractmethod


class Food(ABC):

    def __init__(self, quantity: int):
        self.quantity = quantity


class Fruit(Food):
    pass


class Meat(Food):
    pass


class Vegetable(Food):
    pass


class Seed(Food):
    pass
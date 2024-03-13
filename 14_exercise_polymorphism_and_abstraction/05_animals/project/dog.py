from abc import ABC
from project.animal import Animal


class Dog(Animal, ABC):

    @staticmethod
    def make_sound() -> str:
        return "Woof!"
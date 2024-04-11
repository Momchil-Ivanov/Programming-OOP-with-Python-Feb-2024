from typing import List

from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    VALID_CAR_TYPES = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}

    def __init__(self):
        self.cars: List[Car] = []
        self.drivers: List[Driver] = []
        self.races: List[Race] = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        car = next(filter(lambda c: c.model == model, self.cars), None)
        if car:
            raise Exception(f"Car {model} is already created!")

        if car_type in self.VALID_CAR_TYPES:
            self.cars.append(self.VALID_CAR_TYPES[car_type](model, speed_limit))
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        driver = next(filter(lambda d: d.name == driver_name, self.drivers), None)
        if driver:
            raise Exception(f"Driver {driver_name} is already created!")

        self.drivers.append(Driver(driver_name))
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        race = next(filter(lambda r: r.name == race_name, self.races), None)
        if race:
            raise Exception(f"Race {race_name} is already created!")

        self.races.append(Race(race_name))
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = next(filter(lambda d: d.name == driver_name, self.drivers), None)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        cars = [c for c in self.cars if c.__class__.__name__ == car_type]
        cars_reversed = cars[::-1]
        current_car = None
        for car in cars_reversed:
            if not car.is_taken:
                current_car = car
                break
        if not current_car:
            raise Exception(f'Car {car_type} could not be found!')

        if driver.car:
            old_model = driver.car.model
            driver.car.is_taken = False
            driver.car = current_car
            new_model = driver.car.model
            driver.car.is_taken = True
            return f"Driver {driver.name} changed his car from {old_model} to {new_model}."

        driver.car = current_car
        car_model = driver.car.model
        driver.car.is_taken = True
        return f"Driver {driver.name} chose the car {car_model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = next(filter(lambda r: r.name == race_name, self.races), None)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        driver = next(filter(lambda d: d.name == driver_name, self.drivers), None)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = next(filter(lambda r: r.name == race_name, self.races), None)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        fastest_driver = sorted(race.drivers, key=lambda d: d.car.speed_limit, reverse=True)
        counter = 0
        result = ''
        for driver in fastest_driver:
            if counter == 3:
                break
            counter += 1
            driver.number_of_wins += 1
            result += f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.\n"

        return result.strip()

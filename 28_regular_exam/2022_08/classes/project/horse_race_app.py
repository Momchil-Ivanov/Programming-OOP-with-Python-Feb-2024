from typing import List

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_HORSE_TYPES = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in self.VALID_HORSE_TYPES:
            return
        horse_names = [horse.name for horse in self.horses]
        if horse_name in horse_names:
            raise Exception(f"Horse {horse_name} has been already added!")
        self.horses.append(self.VALID_HORSE_TYPES[horse_type](horse_name, horse_speed))
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        jockey_names = [jockey.name for jockey in self.jockeys]
        if jockey_name in jockey_names:
            raise Exception(f"Jockey {jockey_name} has been already added!")
        self.jockeys.append(Jockey(jockey_name, age))

        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        race_types = [race.race_type for race in self.horse_races]
        if race_type in race_types:
            raise Exception(f"Race {race_type} has been already created!")
        self.horse_races.append(HorseRace(race_type))
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys), None)
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        horses_reversed = self.horses[::-1]
        horse = next(filter(lambda h: h.__class__.__name__ == horse_type and not h.is_taken, horses_reversed), None)
        if horse is None:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."
        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = next(filter(lambda r: r.race_type == race_type, self.horse_races), None)
        jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys), None)
        if race is None:
            raise Exception(f"Race {race_type} could not be found!")
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."
        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = next(filter(lambda r: r.race_type == race_type, self.horse_races), None)
        if race is None:
            raise Exception(f"Race {race_type} could not be found!")
        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")
        winner = sorted(race.jockeys, key=lambda j: -j.horse.speed)[0]
        return f"The winner of the {race_type} race, with a speed of {winner.horse.speed}km/h is" \
               f" {winner.name}! Winner's horse: {winner.horse.name}."

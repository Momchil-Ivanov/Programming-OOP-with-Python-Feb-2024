from typing import Dict


class Player:

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: Dict[int] = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost) -> str:
        if skill_name not in self.skills.keys():
            self.skills[skill_name] = mana_cost
            return f'Skill {skill_name} added to the collection of the player {self.name}'

        return f'Skill already added'

    def player_info(self) -> str:
        skills_details = ""
        for key, value in self.skills.items():
            skills_details += f'==={key} - {value}\n'

        return f'Name: {self.name}\n' \
               f'Guild: {self.guild}\n' \
               f'HP: {self.hp}\n' \
               f'MP: {self.mp}\n' \
               f'{skills_details}\n'

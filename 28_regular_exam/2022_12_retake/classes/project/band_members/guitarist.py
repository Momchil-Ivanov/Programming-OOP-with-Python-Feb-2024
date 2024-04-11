from project.band_members.musician import Musician


class Guitarist(Musician):

    GUITARIST_AVAILABLE_SKILLS = (
        "play metal",
        "play rock",
        "play jazz",)

    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.available_skills_to_learn = self.GUITARIST_AVAILABLE_SKILLS

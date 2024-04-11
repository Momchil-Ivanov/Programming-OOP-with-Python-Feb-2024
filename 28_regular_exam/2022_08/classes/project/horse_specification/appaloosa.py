from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    Horse.MAX_SPEED = 120
    TRAINING_SPEED_INCREASE: int = 2

    def train(self):
        if self.speed + self.TRAINING_SPEED_INCREASE > self.MAX_SPEED:
            self.speed = self.MAX_SPEED
        else:
            self.speed += self.TRAINING_SPEED_INCREASE

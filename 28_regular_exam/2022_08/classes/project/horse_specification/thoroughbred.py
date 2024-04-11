from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    Horse.MAX_SPEED = 140
    TRAINING_SPEED_INCREASE = 3

    def train(self):
        if self.speed + self.TRAINING_SPEED_INCREASE > self.MAX_SPEED:
            self.speed = self.MAX_SPEED
        else:
            self.speed += self.TRAINING_SPEED_INCREASE

from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):

    def __init__(self, name: str):
        super().__init__(name, 200)

    def can_climb(self):
        if self.strength >= 100:
            return True
        return False

    def climb(self, peak: BasePeak):
        difficulty = peak.difficulty_level
        if difficulty == "Extreme":
            self.strength -= 20 * 2
        elif difficulty == "Advanced":
            self.strength -= 20 * 1.5

        self.conquered_peaks.append(peak.name)

    def __str__(self):
        return f"{ArcticClimber.__name__}: /// Climber name: {self.name} * Left strength: {self.strength:.1f} * Conquered peaks: {', '.join(self.conquered_peaks)} ///"

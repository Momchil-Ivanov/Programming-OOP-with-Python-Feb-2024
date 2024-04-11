from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):

    def __init__(self, name: str):
        super().__init__(name, 150)

    def can_climb(self):
        if self.strength >= 75:
            return True
        return False

    def climb(self, peak: BasePeak):
        difficulty = peak.difficulty_level
        if difficulty == "Advanced":
            self.strength -= 30 * 1.3
        elif difficulty == "Extreme":
            self.strength -= 30 * 2.5

        self.conquered_peaks.append(peak.name)

    def __str__(self):
        return f"{SummitClimber.__name__}: /// Climber name: {self.name} * Left strength: {self.strength:.1f} * Conquered peaks: {', '.join(self.conquered_peaks)} ///"
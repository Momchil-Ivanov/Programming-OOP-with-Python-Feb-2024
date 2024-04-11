from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    def __init__(self, name: str):
        super().__init__(name, 540)

    def miss(self, time_to_catch: int):
        reduced_amount = round(time_to_catch * 0.3)
        if self.oxygen_level < reduced_amount:
            self.oxygen_level = 0
            self.has_health_issue = True
        else:
            if self.oxygen_level == reduced_amount:
                self.has_health_issue = True
            self.oxygen_level -= reduced_amount

    def renew_oxy(self):
        self.oxygen_level = 540

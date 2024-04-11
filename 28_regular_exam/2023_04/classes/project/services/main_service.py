from project.services.base_service import BaseService


class MainService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, 30)

    def details(self):
        result = f"{self.name} Main Service:\n"
        if len(self.robots) > 0:
            robot_names = [r.name for r in self.robots]
            result += f"Robots: {' '.join(robot_names)}"
        else:
            result += "Robots: none"
        return result

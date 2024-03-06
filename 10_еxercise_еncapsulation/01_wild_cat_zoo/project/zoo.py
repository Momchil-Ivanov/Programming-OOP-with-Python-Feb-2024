from project.animal import Animal
from project.worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: list[Animal] = []
        self.workers: list[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f'{animal.name} the {animal.__class__.__name__} added to the zoo'
        elif self.__animal_capacity > len(self.animals) and self.__budget < price:
            return f'Not enough budget'
        return f'Not enough space for animal'

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f'{worker.name} the {worker.__class__.__name__} hired successfully'
        return f'Not enough space for worker'

    def fire_worker(self, worker_name: str) -> str:
            try:
                worker = [w for w in self.workers if w.name == worker_name][0]
                self.workers.remove(worker)
                return f'{worker_name} fired successfully'
            except IndexError:
                return f'There is no {worker_name} in the zoo'

    def pay_workers(self) -> str:
        money_to_pay = sum([w.salary for w in self.workers])

        if money_to_pay <= self.__budget:
            self.__budget -= money_to_pay
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        return f'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self) -> str:
        money_to_feed_animals = sum([a.money_for_care for a in self.animals])
        if money_to_feed_animals <= self.__budget:
            self.__budget -= money_to_feed_animals
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'
        return f'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        result = f'You have {len(self.animals)} animals\n'
        lions = [l for l in self.animals if l.__class__.__name__ == "Lion"]
        amount_of_lions = len(lions)
        result += f'----- {amount_of_lions} Lions:\n'
        for lion in lions:
            result += f'{lion}\n'

        tigers = [t for t in self.animals if t.__class__.__name__ == "Tiger"]
        amount_of_tigers = len(tigers)
        result += f'----- {amount_of_tigers} Tigers:\n'
        for tiger in tigers:
            result += f'{tiger}\n'

        cheetahs = [c for c in self.animals if c.__class__.__name__ == "Cheetah"]
        amount_of_cheetahs = len(cheetahs)
        result += f'----- {amount_of_cheetahs} Cheetahs:\n'
        for cheetah in cheetahs:
            result += f'{cheetah}\n'

        return result[:-1]

    def workers_status(self) -> str:
        result = f'You have {len(self.workers)} workers\n'

        keepers = [k for k in self.workers if k.__class__.__name__ == "Keeper"]
        amount_of_keepers = len(keepers)
        result += f'----- {amount_of_keepers} Keepers:\n'
        for keeper in keepers:
            result += f'{keeper}\n'

        caretakers = [c for c in self.workers if c.__class__.__name__ == "Caretaker"]
        amount_of_caretakers = len(caretakers)
        result += f'----- {amount_of_caretakers} Caretakers:\n'
        for caretaker in caretakers:
            result += f'{caretaker}\n'

        vets = [v for v in self.workers if v.__class__.__name__ == "Vet"]
        amount_of_vets = len(vets)
        result += f'----- {amount_of_vets} Vets:\n'
        for vet in vets:
            result += f'{vet}\n'

        return result[:-1]






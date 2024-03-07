from typing import Dict


class Shop:

    def __init__(self, name: str, type_shop: str, capacity: int):
        self.name = name
        self.type = type_shop
        self.capacity = capacity
        self.items: Dict[str: int] = {}

    @classmethod
    def small_shop(cls, name: str, type_shop: str):
        return cls(name, type_shop, capacity=10)

    def add_item(self, item_name: str) -> str:
        if sum(self.items.values()) >= self.capacity:
            return 'Not enough capacity in the shop'

        self.items[item_name] = self.items.get(item_name, 0) + 1

        return f'{item_name} added to the shop'

    def remove_item(self, item_name: str, amount: int) -> str:
        product_quantity = self.items.get(item_name)

        if not product_quantity or amount > product_quantity:
            return f'Cannot remove {amount} {item_name}'

        self.items[item_name] -= amount

        if self.items[item_name] == 0:
            del self.items[item_name]

        return f'{amount} {item_name} removed from the shop'

    def __repr__(self):
        return f'{self.name} of type {self.type} with capacity {self.capacity}'

from project.bakery import Bakery

bakery = Bakery("My Bakery")
print(bakery.add_food("Bread", "baguette", 1.5))
print(bakery.add_drink("Tea", "Green", 2, "Coca Cola"))
print(bakery.add_drink("Water", "Coca Cola", 2, "Coca Cola"))
print(bakery.add_drink("Tea", "Bunga", 2, "Coca Cola"))
print(bakery.add_table("InsideTable", 1, 4))
print(bakery.order_drink(1, "Green", "Rush"))
print(bakery.add_table("OutsideTable", 52, 4))
print(bakery.add_table("InsideTable", 3, 4))
print(bakery.get_free_tables_info())
print(bakery.get_total_income())
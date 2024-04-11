from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VALID_VEHICLE_TYPES = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}
    route_id_counter: int = 1

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        driver = next(filter(lambda u: u.driving_license_number == driving_license_number, self.users), None)
        if driver:
            return f"{driving_license_number} has already been registered to our platform."

        self.users.append(User(first_name, last_name, driving_license_number))
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VALID_VEHICLE_TYPES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        vehicle = next(filter(lambda v: v.license_plate_number == license_plate_number, self.vehicles), None)
        if vehicle:
            return f"{license_plate_number} belongs to another vehicle."

        self.vehicles.append(self.VALID_VEHICLE_TYPES[vehicle_type](brand, model, license_plate_number))
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        route = next(filter(lambda r: r.start_point == start_point and r.end_point == end_point and r.length == length, self.routes), None)
        if route:
            return f"{start_point}/{end_point} - {length} km had already been added to our platform."

        route = next(filter(lambda r: r.start_point == start_point and r.end_point == end_point, self.routes), None)
        if route and route.length < length:
            return f"{start_point}/{end_point} shorter route had already been added to our platform."

        self.routes.append(Route(start_point, end_point, length, self.route_id_counter))
        self.route_id_counter += 1

        route = next(filter(lambda r: r.start_point == start_point and r.end_point == end_point and r.length > length, self.routes), None)
        if route:
            route.is_locked = True

        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user = next(filter(lambda u: u.driving_license_number == driving_license_number, self.users), None)
        vehicle = next(filter(lambda v: v.license_plate_number == license_plate_number, self.vehicles), None)
        route = next(filter(lambda r: r.route_id == route_id, self.routes), None)

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()

        result = str(vehicle)
        return result

    def repair_vehicles(self, count: int):
        count_of_repaired_vehicles = 0

        damaged_vehicles = [v for v in self.vehicles if v.is_damaged]
        sorted_damaged_vehicles = sorted(damaged_vehicles, key=lambda v: (v.brand, v.model))

        if count > len(sorted_damaged_vehicles):
            count = len(damaged_vehicles)

        for i in range(0, count):
            sorted_damaged_vehicles[i].recharge()
            sorted_damaged_vehicles[i].change_status()
            count_of_repaired_vehicles += 1

        return f"{count_of_repaired_vehicles} vehicles were successfully repaired!"

    def users_report(self):
        sorted_users = sorted(self.users, key=lambda u: -u.rating)
        result = f"*** E-Drive-Rent ***\n"
        for user in sorted_users:
            result += str(user) + "\n"

        return result.strip()

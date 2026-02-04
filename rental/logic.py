class Person:
    def __init__(self, name):
        self.name = name

class Car:
    def __init__(self, car_id, brand, model, year):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.year = year
        self.available = True

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"

class Customer(Person):
    def __init__(self, name):
        super().__init__(name)
        self.rented_cars = []

class CarRentalSystem:
    def __init__(self):
        self.cars = []
        self.customers = []

    def add_car(self, car):
        self.cars.append(car)

    def add_customer(self, customer):
        self.customers.append(customer)

    def rent_car(self, customer_name, car_id):
        customer = next((c for c in self.customers if c.name == customer_name), None)
        car = next((c for c in self.cars if str(c.car_id) == str(car_id)), None)
        
        if customer and car and car.available:
            car.available = False
            customer.rented_cars.append(car)
            return True
        return False

    def return_car(self, customer_name, car_id):
        customer = next((c for c in self.customers if c.name == customer_name), None)
        if customer:
            car = next((c for c in customer.rented_cars if str(c.car_id) == str(car_id)), None)
            if car:
                car.available = True
                customer.rented_cars.remove(car)
                return True
        return False

# Global instance for in-memory storage
rental_system = CarRentalSystem()

# Pre-populate with some data for testing
rental_system.add_car(Car(1, "Tesla", "Model S", 2023))
rental_system.add_car(Car(2, "BMW", "M4", 2022))
rental_system.add_customer(Customer("Omkar Patole"))

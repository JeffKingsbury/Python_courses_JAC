# 2) Create two new classes Motorcycle and Auto that inherit from vehicle
# Add a new attribute to this classes “color” and “brand”
# Create the appropriate Initializer for this classes. (remember o invoke the parent initializer)
# Create an object of type Motorcycle and an object of type Car
# Get the current speed for both objects
# Set the speed of the Motorcycle to 95
# Set the speed of the car to 100
# Get the current speed for both the Motorcycle and the Car
# Print the color and brands of the car and the color of the motorcycle objects


class Vehicle:
    vehicle_count = 0

    def __init__(self, wheels, passengers, max_speed):
        self.wheels = wheels
        self.passengers = passengers
        self.max_speed = max_speed
        self.speed = 0
        Vehicle.vehicle_count += 1

    def current_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed


class Auto(Vehicle):
    def __init__(self, wheels, passengers, max_speed, color, brand):
        super().__init__(wheels, passengers, max_speed)
        self.color = color
        self.brand = brand

    def get_color(self):
        return self.color

    def get_brand(self):
        return self.brand


class Moto(Vehicle):
    def __init__(self, wheels, passengers, max_speed, color, brand):
        super().__init__(wheels, passengers, max_speed)
        self.color = color
        self.brand = brand

    def get_color(self):
        return self.color

    def get_brand(self):
        return self.brand


Motorcycle = Moto(2, 2, 100, "black", "Harley")
Car = Auto(4, 5, 90, "green", "Hyundai")

print(Motorcycle.current_speed())
print(Car.current_speed())

Motorcycle.set_speed(95)
Car.set_speed(100)

print(Motorcycle.current_speed())
print(Car.current_speed())

print(Motorcycle.get_color(), Motorcycle.get_brand())
print(Car.get_color(), Car.get_brand())

# 1) Create a class “Vehicle” (Exploring simple classes)
# . The class contains one instance attribute vehicle_count (accessible by all instances of the
# class vehicle)
# . Add an initializer to the class. The initializer receives several parameters:
# . number of wheels, number of passengers max_speed (km/hour)
# . The initializer also defines the attribute speed. To start the speed is initialized to zero.
#  . In the initializer, add 1 to vehicle_count.
# . Create a method called current_speed() that returns the current speed of the vehicle
# . Create a method called set_speed(speed) that sets the speed of the vehicle.
# Once your Class is done, use it to create the following objects:
# V01 = vehicle(4,2,100)
# V02 = vehicle(6,4,75)
# Print the current_speed of both vehicles
#  Set the speed of vehicle V01 to 90
#  Set the speed of vehicle V02 to 60
# Print the current_speed of both vehicles
# Print the value vehicle_count

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


V01 = Vehicle(4, 2, 100)
V02 = Vehicle(6, 4, 75)

print(V01.current_speed())
print(V02.current_speed())

V01.set_speed(90)
V02.set_speed(60)

print(V01.current_speed())
print(V02.current_speed())

print(Vehicle.vehicle_count)

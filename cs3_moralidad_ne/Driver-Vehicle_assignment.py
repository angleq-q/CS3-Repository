class Vehicle:
    def  __init__(self, plate_number, model):
        self.plate_number = plate_number
        self.model = model

class Driver:
    def __init__(self, name):
        self.name = name

    def assign_vehicle(self, vehicle):
        self.vehicle = vehicle

Vehicle1 = Vehicle("ABC 1234", "Toyota Vios")
Driver1 = Driver("Mr. Santos")

Driver1.assign_vehicle(Vehicle1)

print(Driver1.name)
print(Driver1.assign_vehicle.plate_number)
print(Driver1.assign_vehicle.model)
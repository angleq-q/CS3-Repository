class Starship:
    def __init__(self, base_weight, cargo_weight, total_fuel):
        self.base_weight = base_weight
        self.cargo = cargo_weight
        self.total_fuel = total_fuel

    def cargo_weight(self, weight=0):
        self.cargo += weight
        return self.cargo

    def load_cargo(self):
        cargo_weight += 1000

    def calculate_fuel(self):
        total_weight = self.cargo + self.base_weight
        self.total_fuel = total_weight * 3
        return self.total_fuel


starship = Starship(base_weight=50000, cargo_weight=0, total_fuel=0)
Starship.load_cargo()
Starship.load_cargo()
Starship.load_cargo()

required_fuel = starship.calculate_fuel()
print("Total Cargo Loaded:", starship.cargo_weight(), "kg")
print("Total Fuel Required:", required_fuel, "gallons")


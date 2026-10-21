def calculate_fuel(cargo_weight):
    total_weight = cargo_weight + 50000
    fuel_needed = total_weight * 3
    return fuel_needed

total_cargo_weight = 0
while True:
    item = input("Enter cargo (satellite, rover, supplies) or type 'launch': ")
    if item == "launch":
        break
    if item == "satellite":
        print("Confirmation: Satellite added.")
        total_cargo_weight = total_cargo_weight + 1000  
    elif item == "rover":
        print("Confirmation: Rover added.")
        total_cargo_weight = total_cargo_weight + 2500
    elif item == "supplies":
        print("Confirmation: Supplies added.")
        total_cargo_weight = total_cargo_weight + 500
    else:
        print("That item is not approved for the mission.")

    if total_cargo_weight > 10000:
        print("MAX WEIGHT REACHED")
        break

required_fuel = calculate_fuel(total_cargo_weight)

print("Total Cargo Loaded:", total_cargo_weight, "kg")
print("Total Fuel Required:", required_fuel, "gallons")
class Plant:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
    def attack(self, zombie):
        if self.health > 0:
            zombie.health = zombie.health - self.damage
            print(f"{self.name} Health: {self.health}")
        else:
            zombie.health = zombie.health
            print(f"{self.name} Health: {self.health}")
        
class Zombie:
    def __init__(self, name, health, damage, distance):
        self.name = name
        self.health = health
        self.damage = damage
        self.distance = distance
    def move(self, steps):
        if self.health > 0:
            self.distance = self.distance - steps
            print(f"{self.name} Health: {self.health}")
            print(f'{self.name} distance: {self.distance}')
        else:
             self.distance = self.distance
    def attack(self, plant):
        if self.distance <=1 and self.health > 0:
            plant.health = plant.health- self.damage
        else:
             plant.health = plant.health

plant1 = Plant("Peashooter1", 10, 3)
plant2 = Plant("Peashooter2", 10, 5)
zombeh = Zombie("Yana", 3000, 3, 30)

plants = [plant1, plant2]
turn = 1
current_target_index = 0

print("BATTLE START")

while zombeh.health > 0 and any(p.health > 0 for p in plants):
    print(f"\n Turn {turn}")

    for plant in plants:
        if plant.health > 0:
            plant.attack(zombeh)
    
    if zombeh.health <= 0:
        print(f"\n {zombeh.name} has been defeated! The plants win!")
        break
        
    zombeh.move(steps=2)
    
    for plant in plants:
        if plant.health > 0:
            zombeh.attack(plant)
            break  
     
    if all(p.health <= 0 for p in plants):
        print(f"\n All plants have been destroyed! {zombeh.name} wins!")
        break

    turn += 1

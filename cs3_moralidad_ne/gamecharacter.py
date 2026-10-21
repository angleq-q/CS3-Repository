class GameCharacter:

    def __init__(self, health, strength, defense, speed):
        self._health = health  
        self.strength = strength
        self.defense = defense
        self.speed = speed
        self.level = 1

    def take_damage(self, hit_points):
        actual_damage =  hit_points -  self.defense
        self._health = actual_damage
        print(f"Player taking {hit_points} damage")
        print(f"Player has {self.defense}")
        print(f"Actual damage:{actual_damage}")

    def train(self, train_points):
        self.strength += train_points
        print(f"Player trained. Strength: {self.strength}")

    def health_regen(self, regen_points):
        self._health += regen_points
        print(f"Player is healing: Health {self._health}")

    def show_stats(self):
        print(f"Player Health: {self._health }")
        print(f"Player Strength: {self.strength}")
        print(f"Player Defense: {self.defense}")

character_patrice= GameCharacter(100, 80, 80, 10000000000000000000000)

character_patrice.train(50)
character_patrice.take_damage(50)
character_patrice.health_regen(1)
character_patrice.take_damage(10)
character_patrice.show_stats()

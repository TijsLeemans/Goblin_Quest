import attack as at

class Enemy:
    def __init__(self, name, icon, healthpoints, attack, defence, pattern, attack_types, state = 1):
        self.name = name
        self.icon = icon
        self.healthpoints = healthpoints
        self.attack = attack
        self.defence = defence
        self.pattern = pattern
        self.attack_types = attack_types
        self.state = state

    def calculate_healthpoints(self, damage_taken):
        self.healthpoints = self.healthpoints - (damage_taken - self.defence)
        if self.healthpoints =< 0:
            print(self.name, "has been defeated!")
            self.state = 0

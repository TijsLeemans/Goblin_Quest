class Player:
    def __init__(self, name, healthpoints, attack, defence, prayer = 0, state = True):
        self.name = name
        self.healthpoints = healthpoints
        self.attack = attack
        self.defence = defence
        self.prayer = prayer
        self.state = state

    def calculate_healthpoints(self, damage_taken, attack_type):
        if attack_type == self.prayer:
            self.healthpoints = self.healthpoints - ((damage_taken * 0.5) - self.defence)
        else:
            self.healthpoints = self.healthpoints - (damage_taken - self.defence)

Player = Player("Alendos", 9900, 0, 0)
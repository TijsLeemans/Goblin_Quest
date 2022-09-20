import sys, pygame
import attack as at

class Player:
    def __init__(self, name, healthpoints, attack, defence, prayer = 0, prayer_color = (0,0,0), state = True):
        self.name = name
        self.healthpoints = healthpoints
        self.attack = attack
        self.defence = defence
        self.prayer = prayer
        self.prayer_color = prayer_color
        self.state = state


    def calculate_healthpoints(self, damage_taken, attack_type):
        if attack_type == self.prayer:
            self.healthpoints = self.healthpoints - ((damage_taken * 0.5) - self.defence)
        else:
            self.healthpoints = self.healthpoints - (damage_taken - self.defence)
        if self.healthpoints <= 0:
            self.state = False
            print(self.name, "has died for the last time.")          

    soulsplit_color = (240,240,240)
    melee_color = (110,110,110)
    ranged_color = (0,200,0)
    magic_color = (0,0,200)

    idle = at.Attack(
        "Idle",
        (0,0,0),
        "none",
        0,
        1,
        0,
        0,
        0
    )

    magic_blast = at.Attack(
        "Magic Blast",
        at.Attack.magic_color,
        "Magic",
        2,
        1800,
        0,
        200,
        200
    )


Player = Player("Alendos", 9900, 100, 0)
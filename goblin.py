from enemy import Enemy
import attack as at

class Goblin(Enemy):

    def __init__(self, name, icon, healthpoints, attack, defence, pattern, attack_types, state=1):
        super().__init__(name, icon, healthpoints, attack, defence, pattern, attack_types, state)

    swipe = at.Attack(
        "Swipe",
        at.Attack.melee_color,
        "Melee",
        2,
        1800,
        200,
        1000,
        2000
    )

    ranged_attack = at.Attack(
        "Ranged Attack",
        at.Attack.ranged_color,
        "Ranged",
        1,
        1800,
        0,
        200,
        400
    )

Goblin_King = Goblin(
    "Goblin King",
    "goblin_King.png",
    1000,
    0,
    0,
    [[Goblin.ranged_attack, Goblin.ranged_attack, Goblin.ranged_attack, Goblin.swipe]],
    0,
    1
)

from enemy import Enemy
import attack as at

class Goblin(Enemy):

    swipe = at.Attack(
        "Swipe",
        melee_color,
        "Melee",
        2,
        1800,
        1000,
        2000
    )

    auto_attack = at.Attack(
        "Auto_Attack"
        ranged_color,
        1,
        1800,
        200,
        400
    )

Goblin_King = Goblin(
    "Goblin King",
    0,
    1000,
    0,
    0,
    [[auto_attack, auto_attack, auto_attack, swipe]],
    0,
    1
)

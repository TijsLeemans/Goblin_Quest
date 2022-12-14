from random import randrange

class Attack:
    def __init__(self, name, color, type, hit_amount, timer, multihit_timer, minimal_damage, damage_variance):
        self.name = name
        self.color = color
        self.type = type
        self.hit_amount = hit_amount
        self.timer = timer
        self.multihit_timer = multihit_timer
        self.minimal_damage = minimal_damage
        self.damage_variance = damage_variance

    def attack_damage_calculation(self):
        damage_output = 0
        local_hit_amount = self.hit_amount
        while local_hit_amount > 0:
            damage_output = damage_output + (randrange(self.damage_variance) + self.minimal_damage)
            self.timer -= self.multihit_timer
            local_hit_amount -= local_hit_amount
        return damage_output

    melee_color = (110,110,110)
    ranged_color = (0,200,0)
    magic_color = (0,0,200)

# melee_aa = Auto_Attack(
#     "Melee auto attack",
#     (110,110,110),
#     "Melee",
#     1200,
#     200,
#     400)
#
# ranged_aa = Auto_Attack(
#     "Ranged auto attack",
#     (0,200,0),
#     "Ranged",
#     1800,
#     200,
#     500
# )
#
# magic_aa = Auto_Attack(
#     "Magic auto attack",
#     (0,0,200),
#     "Magic",
#     1800,
#     200,
#     500)
#
# def attack_generator():
#     int = randrange(3)
#     if int == 0:
#         print("melee")
#         return melee_aa
#     if int == 1:
#         print("range")
#         return ranged_aa
#     if int == 2:
#         print("magic")
#         return magic_aa

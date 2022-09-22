import sys, pygame
from player import Player
from goblin import Goblin_King

pygame.init()

windowsize = width, hight = 800, 600
enemy_action_timer = 0
player_action_timer = 0
clock = pygame.time.Clock()

target_attack_index = 0

black = (0,0,0)

screen = pygame.display.set_mode(windowsize)
enemy_icon = pygame.image.load(Goblin_King.icon)
enemy_current_attack = Goblin_King.pattern[Goblin_King.state - 1][target_attack_index]
# print(len(Goblin_King.pattern[0]))
player_current_attack = Player.idle


def handle_inputs(events):
    global player_action_timer, player_current_attack
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_u:
                Player.prayer = "Soulsplit"
                Player.prayer_color = Player.soulsplit_color
            if event.key == pygame.K_i:
                Player.prayer = "Melee"
                Player.prayer_color = Player.melee_color
            if event.key == pygame.K_o:
                Player.prayer = "Ranged"
                Player.prayer_color = Player.ranged_color
            if event.key == pygame.K_p:
                Player.prayer = "Magic"
                Player.prayer_color = Player.magic_color
            if event.key == pygame.K_q:
                player_action_timer = 0
                # print("Magic go brrrrrrr")
                player_current_attack = Player.magic_blast

while Player.state & Goblin_King.state != 0:
    screen.fill(black)
    tick = clock.tick()

    pygame.Surface.blit(enemy_icon (400,400))
    handle_inputs(pygame.event.get())

    if player_current_attack.name != "Idle":
        if player_action_timer > player_current_attack.timer:
            player_action_timer = 0
            damage_taken = player_current_attack.attack_damage_calculation()
            print("Your attack deals: ", damage_taken)
            Goblin_King.calculate_healthpoints(damage_taken)
            player_current_attack = Player.idle
            # print(damage_taken)

    if enemy_action_timer > enemy_current_attack.timer:
        enemy_action_timer = 0
        target_attack_index = (target_attack_index + 1) % len(Goblin_King.pattern[0])
        # print(enemy_current_attack.hit_amount)
        damage_taken = enemy_current_attack.attack_damage_calculation()
        Player.calculate_healthpoints(damage_taken, enemy_current_attack.type)
        # print(damage_taken)
        enemy_current_attack = Goblin_King.pattern[Goblin_King.state - 1][target_attack_index]

    enemy_health_bar = 10 + (200 *(Goblin_King.healthpoints / 1000))
    enemy_attack_animation = 10 + (200 * (enemy_action_timer / enemy_current_attack.timer))
    player_health_bar = 10 + (200 * (Player.healthpoints / 9900))
    player_attack_animation = 10 + (200 * (player_action_timer / player_current_attack.timer))

    pygame.draw.line(screen, enemy_current_attack.color, (10,20), (enemy_attack_animation, 20), 5)
    pygame.draw.line(screen, (255,0,0), (10,40), (player_health_bar, 40), 5)
    pygame.draw.line(screen, (255,0,0), (10,80), (enemy_health_bar, 80), 5)
    pygame.draw.line(screen, player_current_attack.color, (10,60), (player_attack_animation, 60), 5)
    pygame.draw.rect(screen, Player.prayer_color,(100,100,200,200))

    player_action_timer += tick
    enemy_action_timer += tick
    pygame.display.flip()
      
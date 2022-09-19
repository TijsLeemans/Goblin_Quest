import sys, pygame
from player import Player
import goblin

pygame.init()

windowsize = width, hight = 320, 240
action_timer = 0
clock = pygame.time.Clock()

black = (0,0,0)
soulsplit_color = (240,240,240)
melee_color = (110,110,110)
ranged_color = (0,200,0)
magic_color = (0,0,200)
prayer_color = black

screen = pygame.display.set_mode(windowsize)
current_attack = at.attack_generator()
print(Goblin_King.pattern)

while Player.state:
    screen.fill(black)
    tick = clock.tick()
    target_attack_animation = 10 + (200 * (action_timer / current_attack.timer))
    player_health_bar = 10 + (200 * (Player.healthpoints / 9900))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_u:
                Player.prayer = "Soulsplit"
                prayer_color = soulsplit_color
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                Player.prayer = "Melee"
                prayer_color = melee_color
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o:
                Player.prayer = "Ranged"
                prayer_color = ranged_color
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                Player.prayer = "Magic"
                prayer_color = magic_color

    pygame.draw.line(screen, current_attack.color, (10,20), (target_attack_animation, 20), 5)
    pygame.draw.line(screen, (255,0,0), (10,40), (player_health_bar, 40), 5)
    pygame.draw.rect(screen, prayer_color,(100,100,200,200))

    if action_timer > current_attack.timer:
        action_timer = 0
        damage_taken = current_attack.attack_damage_calculation()
        Player.calculate_healthpoints(damage_taken, current_attack.type)
        current_attack = at.attack_generator()
        print(damage_taken)
        if Player.healthpoints <= 0:
            Player.state = False
            print(Player.name, "has died for the last time.")

    action_timer += tick
    pygame.display.flip()

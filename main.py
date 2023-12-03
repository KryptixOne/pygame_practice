import pygame
import sys
from random import randint


def display_score(start_time):
    current_time = pygame.time.get_ticks() - start_time  # gives time in ms
    score_surf = test_font.render('Score: ' + str(int(current_time / 1000)), False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obs_rect in obstacle_list:
            obs_rect.x -= 5

            if obs_rect.bottom == 300:
                screen.blit(snail_surface, obs_rect)
            else:
                screen.blit(fly_surf, obs_rect)

        # delete rect that have left the screen
        obstacle_list = [obs for obs in obstacle_list if obs.x > -100]
    return obstacle_list


def collisions(player, obstacles):
    if obstacles:
        for rect in obstacles:
            if player.colliderect(rect):
                print('collide')
                return False
    return True


# starts pygame and init all sub-parts
pygame.init()
width = 800
height = 400

game_active = True
start_time = 0
# create screen of size 400x800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Happy_Runner')  # set title on window
clock = pygame.time.Clock()
test_font = pygame.font.Font('./assets/font/Pixeltype.ttf', 50)

"""
# to create a colored surface
test_surface = pygame.Surface((100, 200))  # tuple (w,h)
test_surface.fill('Red')
"""

sky_surface = pygame.image.load('./assets/graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('./assets/graphics/ground.png').convert_alpha()

score_surface = test_font.render('My Game :O', False, (64, 64, 64))
score_rect = score_surface.get_rect(center=(400, 50))

# For Gameover Screen
player_stand = pygame.image.load('./assets/graphics/Player/player_stand.png')
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))
player_surface = pygame.image.load('./assets/graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80, 300))  # draws rect in shape of player surface

# obstacles
snail_surface = pygame.image.load('./assets/graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=((600, 300)))

fly_surf = pygame.image.load('./assets/graphics/Fly/Fly2.png').convert_alpha()
fly_rect = fly_surf.get_rect(midbottom=((600, 800)))
obst_rect_list = []

# Gravity
player_gravity = 0

# Obstable Timer
obs_timer = pygame.USEREVENT + 1  # always add +1 to each custom event to prevent issues
pygame.time.set_timer(obs_timer, 1500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # quits pygame
            sys.exit()  # exits code
        # gives mouse position every interation of loop
        # if event.type == pygame.MOUSEMOTION:
        #    player_rect.collidepoint(event_pos)  # check if collision with player

        # pygame.MOUSEBUTTONDOWN and BUTTONUP check if mouse is being held or has been released
        if game_active:
            # checking if any button is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks()
        if event.type == obs_timer and game_active:
            if randint(0, 2):
                obst_rect_list.append(snail_surface.get_rect(midbottom=((randint(900, 1100), 300))))
            else:
                obst_rect_list.append(fly_surf.get_rect(midbottom=((randint(900, 1100), 150))))

    if game_active:
        screen.blit(sky_surface, (0, 0))  # place surface at position (0,0)
        screen.blit(ground_surface, (0, 300))
        pygame.draw.rect(screen, '#c0e8ec', score_rect)

        # screen.blit(score_surface, score_rect)
        display_score(start_time)

        """snail_rect.left -= 5
        screen.blit(snail_surface, snail_rect)"""

        player_gravity += 1
        player_rect.y += player_gravity

        # set floor
        if player_rect.bottom >= 300:
            player_rect.bottom = 300

        screen.blit(player_surface, player_rect)

        # Obstacle Movement
        obst_rect_list = obstacle_movement(obst_rect_list)

        # Collision detector on rectangle
        game_active = collisions(player_rect, obst_rect_list)

    else:
        obst_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_gravity = 0
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)

    pygame.display.update()  # updates display surface
    clock.tick(60)  # tells pygame should be maxed at 60 fps

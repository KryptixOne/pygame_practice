import pygame
import sys

# starts pygame and init all sub-parts
pygame.init()
width = 800
height = 400

game_active = True
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

player_surface = pygame.image.load('./assets/graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80, 300))  # draws rect in shape of player surface
snail_surface = pygame.image.load('./assets/graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=((600, 300)))

# Gravity
player_gravity = 0

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
                if event.key == pygame.K_SPACE and player_rect.bottom ==300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True

    if game_active:
        screen.blit(sky_surface, (0, 0))  # place surface at position (0,0)
        screen.blit(ground_surface, (0, 300))
        pygame.draw.rect(screen, '#c0e8ec', score_rect)

        screen.blit(score_surface, score_rect)

        snail_rect.left -= 5
        screen.blit(snail_surface, snail_rect)

        player_gravity += 1
        player_rect.y += player_gravity

        # set floor
        if player_rect.bottom >= 300:
            player_rect.bottom =300


        screen.blit(player_surface, player_rect)

        # Collision detector on rectangle
        if player_rect.colliderect(snail_rect):  # returns 0 or 1
            snail_rect.left = 600
            game_active = False

        # Collision with mouse
        mouse_pos = pygame.mouse.get_pos()  # returns x,y pos of mouse
        # pygame.mouse.get_pressed() returns what mouse button is being pressed, Tuple of booleans
        if player_rect.collidepoint((mouse_pos)):  # checks x,y pos
            player_rect.left = 80

        # keys = pygame.key.get_pressed()  # returns states of all buttons

        if snail_rect.left <= 0:
            snail_rect.left = 600

    else:
        screen.fill ('Yellow')


    pygame.display.update()  # updates display surface
    clock.tick(60)  # tells pygame should be maxed at 60 fps

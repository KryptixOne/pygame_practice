import pygame
import sys

# starts pygame and init all sub-parts
pygame.init()
width = 800
height = 400
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
text_surface = test_font.render('My Game :O', False, 'Black')

player_surface = pygame.image.load('./assets/graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom =(80,300))  # draws rect in shape of player surface
snail_surface = pygame.image.load('./assets/graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=((600, 300)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # quits pygame
            sys.exit()  # exits code

    screen.blit(sky_surface, (0, 0))  # place surface at position (0,0)
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    snail_rect.left -=5
    screen.blit(snail_surface, snail_rect)
    player_rect.left += 1
    screen.blit(player_surface, player_rect)

    if snail_rect.left <= 0:
        snail_rect.left = 600
    pygame.display.update()  # updates display surface
    clock.tick(60)  # tells pygame should be maxed at 60 fps

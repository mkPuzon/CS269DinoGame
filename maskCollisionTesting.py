'''Pygame sprite collisions using masks. From this tutorial: 
https://www.youtube.com/watch?v=uW3Fhe-Vkx4&t=723s from 3:05-14:53'''

import pygame, sys

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Assets/Dino/DinoJumpC.png').convert_alpha()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect(center=(300,300))
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if pygame.mouse.get_pos():
            self.rect.center = pygame.mouse.get_pos()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Assets/Cactus/LargeCactus2C.png').convert_alpha()
        self.image.set_colorkey((255,255,255))
        pygame.transform.scale(self.image,(150,150))
        self.rect = self.image.get_rect(center = (400,400))
        self.mask = pygame.mask.from_surface(self.image)

pygame.init()
SCREEN = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()

player = pygame.sprite.GroupSingle(Player())
obstacle = pygame.sprite.GroupSingle(Obstacle())


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    SCREEN.fill('dark green')

    player.update()
    player.draw(SCREEN)
    obstacle.draw(SCREEN)

    # collision. sprite.collide uses rectangle by defult, need self.mask under __init__ method
    if pygame.sprite.spritecollide(player.sprite, obstacle, False):
        if pygame.sprite.spritecollide(player.sprite, obstacle, False,pygame.sprite.collide_mask):
            print('collision')
    
    pygame.display.update()
    clock.tick(60)

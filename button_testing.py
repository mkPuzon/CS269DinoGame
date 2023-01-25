import pygame
from sys import exit
from v3Constants import *
from v3Classes import *
from random import randint

pygame.init()

SCREEN = pygame.display.set_mode((SCREEN_W,SCREEN_H), pygame.FULLSCREEN)   # add 'full' for fullscreen mode
pygame.display.set_caption('Dino Game v3')
clock = pygame.time.Clock()
level_1_button = Button(SCREEN_W //2 + SCREEN_W//4, SCREEN_H // 2,100,100,"1")


while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
    
    SCREEN.fill('white')
    font = pygame.font.Font('Assets/ARCADECLASSIC.TTF', 30)
    text = font.render("Press ESC to Quit   Press Tab To Pause", True, (0,0,0))
    text_rect = text.get_rect()
    text_rect.center = (SCREEN_W //2, SCREEN_H // 8)
    SCREEN.blit(text, text_rect)
    
    if(level_1_button.draw_button(SCREEN)):
        SCREEN.fill('black')
    clock.tick(30)
    pygame.display.update()

    
        
'''Classes for v3 of dino game'''
import pygame
from v3Constants import *

class Player(pygame.sprite.Sprite):
    # player constants
    X_POS = 100
    Y_POS = GROUND_LOCATION
    JUMP_VEL = 8.5

    def __init__(self,groups):
        super().__init__(groups)
        self.image = pygame.image.load("Assets/Dino/defaultJump.png").convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

        self.jump_cooldown = 0
        self.step_index = 0
        self.jump_vel = self.JUMP_VEL

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.duck_imgs = DUCKING
        self.run_imgs = RUNNING
        self.jump_img = JUMPING


    def update(self,user_input):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.jump_cooldown != 0:
            self.jump_cooldown -= 1

        if self.step_index >= 10:
            self.step_index = 0

        if user_input[pygame.K_UP] and not self.dino_jump and self.jump_cooldown == 0:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or user_input[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def duck(self):
        self.image = self.duck_imgs[self.step_index // 5]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.step_index += 1

    def run(self):
        self.image = self.run_imgs[self.step_index // 5]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        self.mask = pygame.mask.from_surface(self.image)
        self.jump_cooldown = 2
        if self.dino_jump:
            self.rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self,SCREEN):
        SCREEN.blit(self.image, self.rect)

class GroundObstacle(pygame.sprite.Sprite):
    X_POS = SCREEN_W + 100
    Y_POS = GROUND_LOCATION
    def __init__(self,image, groups):
        super().__init__(groups)
        self.image = image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = self.Y_POS
        self.rect.x = self.X_POS
        self.mask = pygame.mask.from_surface(self.image)

    def update(self,game_speed):
        self.rect.x -= game_speed
        if self.rect.x < -100:
            self.kill()

    def draw(self,SCREEN):
        SCREEN.blit(self.image,self.rect)

class FlyingObstacle(pygame.sprite.Sprite):
    X_POS = SCREEN_W + 100
    Y_POS = GROUND_LOCATION - 8

    def __init__(self,image, groups):
        super().__init__(groups)
        self.image = image
        self.rect = self.image[0].get_rect()
        self.rect.y = self.Y_POS
        self.rect.x = self.X_POS
        self.mask = pygame.mask.from_surface(self.image[0])
        self.index = 0

    def update(self,game_speed):
        self.rect.x -= game_speed
        if self.rect.x < 0:
            self.kill()

    def draw(self, SCREEN):
        if self.index >= 20:
            self.index = 0
        SCREEN.blit(self.image[self.index//10], self.rect)
        self.index += 1

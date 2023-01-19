'''Classes for v3 of dino game'''
import pygame
from v3Constants import *
from random import randint

class Player_0(pygame.sprite.Sprite):
    # player constants
    X_POS = 100
    Y_POS = GROUND_LOCATION
    JUMP_VEL = 8.5

    def __init__(self, SCREEN, groups):
        super().__init__(groups)
        self.image = JUMPING.convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.SCREEN = SCREEN

        self.jump_cooldown = 0
        self.step_index = 0
        self.jump_vel = self.JUMP_VEL

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.duck_imgs = DUCKING
        self.run_imgs = RUNNING
        self.jump_img = JUMPING
        self.dead_img = DEAD


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

class Player_1(pygame.sprite.Sprite):
    # player constants
    X_POS = 100
    Y_POS = GROUND_LOCATION
    JUMP_VEL = 8.5

    def __init__(self, SCREEN, groups):
        super().__init__(groups)
        self.image = JUMPING1.convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.SCREEN = SCREEN

        self.jump_cooldown = 0
        self.step_index = 0
        self.jump_vel = self.JUMP_VEL

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.duck_imgs = DUCKING1
        self.run_imgs = RUNNING1
        self.jump_img = JUMPING1
        self.dead_img = DEAD1


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

class Player_2(pygame.sprite.Sprite):
    # player constants
    X_POS = 100
    Y_POS = GROUND_LOCATION
    JUMP_VEL = 8.5

    def __init__(self, SCREEN, groups):
        super().__init__(groups)
        self.image = JUMPING2.convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.SCREEN = SCREEN

        self.jump_cooldown = 0
        self.step_index = 0
        self.jump_vel = self.JUMP_VEL

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.duck_imgs = DUCKING2
        self.run_imgs = RUNNING2
        self.jump_img = JUMPING2
        self.dead_img = DEAD2


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

class Player_3(pygame.sprite.Sprite):
    # player constants
    X_POS = 100
    Y_POS = GROUND_LOCATION
    JUMP_VEL = 8.5

    def __init__(self, SCREEN, groups):
        super().__init__(groups)
        self.image = JUMPING3.convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.SCREEN = SCREEN

        self.jump_cooldown = 0
        self.step_index = 0
        self.jump_vel = self.JUMP_VEL

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.duck_imgs = DUCKING3
        self.run_imgs = RUNNING3
        self.jump_img = JUMPING3
        self.dead_img = DEAD3


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

class GroundObstacle1(pygame.sprite.Sprite):
    X_POS = SCREEN_W + 100
    Y_POS = GROUND_LOCATION + 75
    def __init__(self,images,groups):
        super().__init__(groups)
        self.image = images
        self.rect = self.image[0].get_rect()
        self.rect.y = self.Y_POS
        self.rect.x = self.X_POS
        self.mask = pygame.mask.from_surface(self.image[0])
        self.index = 0

    def update(self,game_speed):
        self.rect.x -= game_speed
        if self.rect.x < -100:
            self.kill()

    def draw(self,SCREEN):
        if self.index >= 20:
            self.index = 0
        SCREEN.blit(pygame.transform.scale(self.image[self.index//10], (50,50)), self.rect)
        self.index += 1

class FlyingObstacle(pygame.sprite.Sprite):
    X_POS = SCREEN_W + randint(0,500)
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

class FlyingObstacle1(pygame.sprite.Sprite):
    X_POS = SCREEN_W + randint(0,500)
    Y_POS = GROUND_LOCATION - 10

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
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1

class FlyingObstacle2(pygame.sprite.Sprite):
    X_POS = SCREEN_W + randint(0,500)
    Y_POS = GROUND_LOCATION - 50

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
        if self.rect.x < -100:
            self.kill()

    def draw(self, SCREEN):
        if self.index >= 20:
            self.index = 0
        SCREEN.blit(self.image[self.index//10], self.rect)
        self.index += 1

class FlyingObstacle3(pygame.sprite.Sprite):
    X_POS = SCREEN_W + randint(0,500)
    Y_POS = GROUND_LOCATION - 15

    def __init__(self,image, groups):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.y = self.Y_POS
        self.rect.x = self.X_POS
        self.mask = pygame.mask.from_surface(self.image)
        self.index = 0

    def update(self,game_speed):
        self.rect.x -= game_speed
        if self.rect.x < 0:
            self.kill()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, self.rect)

class Item1(pygame.sprite.Sprite):
    def __init__(self,groups,pos,IMAGES):
        super().__init__(groups)
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.image = pygame.transform.scale(IMAGES[0],(40,40))
        self.active_image = pygame.transform.scale(IMAGES[1],(40,40))
        self.rect = self.image.get_rect()
        self.rect.x = self.x_pos
        self.rect.y = self.y_pos
        self.cooldown = 0
        self.ammo = 3

    def update(self, player):
        self.rect.x = player.rect.x + 75
        self.rect.y = player.rect.y + 75
        if player.dino_duck == True:
            self.rect.y = player.rect.y + 90
        if self.ammo == 0:
            self.kill()

    def draw(self,SCREEN):
        SCREEN.blit(self.image,self.rect)


import pygame, random
from v2Constants import *

class Dinosaur(pygame.sprite.Sprite):
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self, groups):
        super().__init__(groups)
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

        self.mask = pygame.mask.from_surface(self.image)

    def update(self, userInput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0
        
        if userInput[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, image, groups, type):
        super().__init__(groups)
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = self.image[self.type].get_height()

        self.mask = pygame.mask.from_surface(self.image[self.type])
        
    def update(self,game_speed,obstacles):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)

class SmallCactus(Obstacle):
    def __init__(self, image, groups):
        self.type = random.randint(0,2)
        super().__init__(image, groups, self.type)
        self.rect.y = 325

class LargeCactus(Obstacle):
    def __init__(self, image, groups):
        self.type = random.randint(0,2)
        super().__init__(image, groups, self.type)
        self.rect.y = 300

class Bird(Obstacle):
    def __init__(self, image, groups):
        self.type = 0
        super().__init__(image, groups, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 20:
            self.index = 0
        SCREEN.blit(self.image[self.index//10], self.rect)
        self.index += 1

class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800,1000)
        self.y = random.randint(50,100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self,game_speed):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500,3000)
            self.y = random.randint(50,100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x,self.y))
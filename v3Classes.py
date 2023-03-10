'''Classes for v3 of dino game'''
import pygame
from v3Constants import *
from random import randint


class Player_1(pygame.sprite.Sprite):
    # player constants
    X_POS = 100
    Y_POS = GROUND_LOCATION
    JUMP_VEL = 8.5

    def __init__(self, groups):
        super().__init__(groups)
        self.image = JUMPING.convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

        self.jump_cooldown = 0
        self.down_cooldown = 0
        self.step_index = 0
        self.jump_vel = self.JUMP_VEL

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False
        self.dino_down = False
        
        

        self.duck_imgs = DUCKING
        self.run_imgs = RUNNING
        self.jump_img = JUMPING
        self.dead_img = DEAD.convert_alpha()

    def render_player(self,display):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        display.blit(self.image, self.rect)
    


    def update(self,actions):
        if self.jump_cooldown != 0:
            self.jump_cooldown -= 1
        
        if self.down_cooldown != 0:
            self.down_cooldown -= 1

        if self.step_index >= 10:
            self.step_index = 0
        
        if actions['up'] and not self.dino_jump and self.jump_cooldown == 0:
            JUMP_SOUND.play()
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        if actions['down'] and self.dino_jump and self.jump_vel > -self.JUMP_VEL:
            self.dino_down = True
    
        elif actions['down'] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
            self.dino_down = False
        elif not (self.dino_jump or actions['down']):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False
            self.dino_down = False
    

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
            
            if self.dino_down:
                self.rect.y -= self.jump_vel * 4
                self.jump_vel -= 1.4
            else:
                self.rect.y -= self.jump_vel * 4
                self.jump_vel -= 0.8
            
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL  

    def draw(self,display):
    
        display.blit(self.image, self.rect)
        
        

class Player_2(pygame.sprite.Sprite):
    # player constants
    X_POS = 100
    Y_POS = GROUND_LOCATION
    JUMP_VEL = 8.5

    def __init__(self, groups):
        super().__init__(groups)
        self.image = JUMPING1.convert_alpha()
        self.rect = self.image.get_rect()
        self.weapon_images = ITEM1
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.mask = pygame.mask.from_surface(self.image)
        
        self.jump_cooldown = 0
        self.step_index = 0
        self.jump_vel = self.JUMP_VEL

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False
        self.dino_down = False
        self.shoot = False

        self.duck_imgs = DUCKING1
        self.run_imgs = RUNNING1
        self.jump_img = JUMPING1
        self.dead_img = DEAD1

    def render_player(self,display):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        
        display.blit(self.image, self.rect)

        if self.dino_duck:
            display.blit(pygame.transform.scale(self.weapon_images[0], (40,40)), (self.rect.x + 75,self.rect.y + 90))
        else:
            display.blit(pygame.transform.scale(self.weapon_images[0], (40,40)), (self.rect.x + 75,self.rect.y + 70))
    

    def update(self,actions):

        if self.jump_cooldown != 0:
            self.jump_cooldown -= 1

        if self.step_index >= 10:
            self.step_index = 0

        if actions['up'] and not self.dino_jump and self.jump_cooldown == 0:
            JUMP_SOUND.play()
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        if actions['down'] and self.dino_jump and self.jump_vel > -self.JUMP_VEL:
            self.dino_down = True
        elif actions['down'] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
            self.dino_down = False
        elif not (self.dino_jump or actions['down']):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False
            self.dino_down = False
    

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
            if self.dino_down:
                self.rect.y -= self.jump_vel * 4
                self.jump_vel -= 1.4
            else:
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

    def __init__(self, groups):
        super().__init__(groups)
        self.image = JUMPING2.convert_alpha()
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
        self.dino_down = False

        self.duck_imgs = DUCKING2
        self.run_imgs = RUNNING2
        self.jump_img = JUMPING2
        self.dead_img = DEAD2


    def render_player(self,display):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        
        display.blit(self.image, self.rect)
    
    

    def update(self,actions):

        if self.jump_cooldown != 0:
            self.jump_cooldown -= 1

        if self.step_index >= 10:
            self.step_index = 0

        if actions['up'] and not self.dino_jump and self.jump_cooldown == 0:
            JUMP_SOUND.play()
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        
        if actions['down'] and self.dino_jump and self.jump_vel > -self.JUMP_VEL:
            self.dino_down = True
        
        elif actions['down'] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
            self.dino_down = False
        elif not (self.dino_jump or actions['down']):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False
            self.dino_down = False
    

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
            if self.dino_down:
                self.rect.y -= self.jump_vel * 4
                self.jump_vel -= 1.4
            else:
                self.rect.y -= self.jump_vel * 4
                self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self,SCREEN):
        SCREEN.blit(self.image, self.rect)

class Player_4(pygame.sprite.Sprite):
    # player constants
    X_POS = 100
    Y_POS = GROUND_LOCATION
    JUMP_VEL = 8.5

    def __init__(self, groups):
        super().__init__(groups)
        self.image = JUMPING3.convert_alpha()
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
        self.dino_down = False

        self.duck_imgs = DUCKING3
        self.run_imgs = RUNNING3
        self.jump_img = JUMPING3
        self.dead_img = DEAD3


    def render_player(self,display):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        
        display.blit(self.image, self.rect)
    
    

    def update(self,actions):

        if self.jump_cooldown != 0:
            self.jump_cooldown -= 1

        if self.step_index >= 10:
            self.step_index = 0

        if actions['up'] and not self.dino_jump and self.jump_cooldown == 0:
            JUMP_SOUND.play()
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        
        if actions['down'] and self.dino_jump and self.jump_vel > -self.JUMP_VEL:
            self.dino_down = True
        
        elif actions['down'] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
            self.dino_down = False
        elif not (self.dino_jump or actions['down']):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False
            self.dino_down = False
    

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
            if self.dino_down:
                self.rect.y -= self.jump_vel * 4
                self.jump_vel -= 1.4
            else:
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
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.y = self.Y_POS
        self.rect.x = self.X_POS
        

    def update(self,game_speed):
        self.rect.x -= game_speed
        if self.rect.x < -200:
            self.kill()

    def draw(self,display):
        display.blit(self.image,self.rect)

class GroundObstacle1(pygame.sprite.Sprite):
    X_POS = SCREEN_W + 100
    Y_POS = GROUND_LOCATION + 15
    def __init__(self,image,groups):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.y = self.Y_POS
        self.rect.x = self.X_POS
        self.mask = pygame.mask.from_surface(self.image)
        self.index = 0

    def update(self,game_speed):
        self.rect.x -= game_speed
        if self.rect.x < -200:
            self.kill()

    def draw(self,SCREEN):
        if self.index >= 20:
            self.index = 0
        SCREEN.blit(pygame.transform.scale(self.image, (100,100)), self.rect)
        self.index += 1

class Mine2(pygame.sprite.Sprite):
    X_POS = SCREEN_W + 100
    Y_POS = GROUND_LOCATION + 100
    def __init__(self,images, groups):
        super().__init__(groups)
        for image in images:
            image.convert_alpha()
        self.image = images
        self.rect = self.image[0].get_rect()
        self.rect.y = self.Y_POS
        self.rect.x = self.X_POS
        self.mask = pygame.mask.from_surface(self.image[0])
        self.index = 0

    def update(self,game_speed):
        self.rect.x -= game_speed
        if self.rect.x < -200:
            self.kill()

    def draw(self, SCREEN):
        if self.index >= 20:
            self.index = 0
        SCREEN.blit(pygame.transform.scale(self.image[self.index//10], (70,70)), self.rect)
        self.index += 1

class GroundObstacle1_T(pygame.sprite.Sprite):
    X_POS = SCREEN_W + 100
    Y_POS = GROUND_LOCATION + 65
    def __init__(self,images,groups):
        super().__init__(groups)
        self.image = images
        self.rect = images[0].get_rect()
        self.rect.y = self.Y_POS
        self.rect.x = self.X_POS
        self.mask = pygame.mask.from_surface(pygame.transform.scale(self.image[0], (60,60)))
        self.index = 0

    def update(self,game_speed):
        self.rect.x -= game_speed
        if self.rect.x < -200:
            self.kill()

    def draw(self,SCREEN):
        if self.index >= 20:
            self.index = 0
        SCREEN.blit(pygame.transform.scale(self.image[self.index//10], (60,60)), self.rect)
        self.index += 1

class Mine2(pygame.sprite.Sprite):
    X_POS = SCREEN_W + 100
    Y_POS = GROUND_LOCATION + 93
    def __init__(self,images, groups):
        super().__init__(groups)
        for image in images:
            image.convert_alpha()
        self.image = images
        self.rect = self.image[0].get_rect()
        self.rect.y = self.Y_POS
        self.rect.x = self.X_POS
        self.mask = pygame.mask.from_surface(self.image[0])
        self.index = 0

    def update(self,game_speed):
        self.rect.x -= game_speed
        if self.rect.x < -200:
            self.kill()

    def draw(self, SCREEN):
        if self.index >= 20:
            self.index = 0
        SCREEN.blit(pygame.transform.scale(self.image[self.index//10], (80,80)), self.rect)
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
        self.rect.x -= game_speed*1.2
        if self.rect.x < -200:
            self.kill()

    def draw(self, SCREEN):
        if self.index >= 20:
            self.index = 0
        SCREEN.blit(self.image[self.index//10], self.rect)
        self.index += 1

class FlyingObstacle1(pygame.sprite.Sprite):
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
        self.rect.x -= game_speed * 1.2
        if self.rect.x < -200:
            self.kill()

    def draw(self, SCREEN):
        if self.index >= 20:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1

class FlyingObstacle2(pygame.sprite.Sprite):
    X_POS = SCREEN_W + randint(0,500)
    Y_POS = GROUND_LOCATION - 75

    def __init__(self,image, groups):
        super().__init__(groups)
        self.image = image
        self.rect = self.image[0].get_rect()
        self.rect.y = self.Y_POS
        self.rect.x = self.X_POS
        self.mask = pygame.mask.from_surface(self.image[0])
        self.index = 0

    def update(self,game_speed):
        self.rect.x -= game_speed * 1.2
        if self.rect.x < -200:
            self.kill()

    def draw(self, SCREEN):
        if self.index >= 20:
            self.index = 0
        SCREEN.blit(self.image[self.index//10], self.rect)
        self.index += 1

class FlyingObstacle3(pygame.sprite.Sprite):
    X_POS = SCREEN_W + randint(0,500)
    Y_POS = GROUND_LOCATION - 22

    def __init__(self,image, groups):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.y = self.Y_POS
        self.rect.x = self.X_POS
        self.mask = pygame.mask.from_surface(self.image)
        self.index = 0

    def update(self,game_speed):
        self.rect.x -= game_speed * 1.2
        if self.rect.x < -200:
            self.kill()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, self.rect)

class Button():
    

    def __init__(self,x,y,width,height,text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.clicked = False

        self.basic_color = (30,80,200)
        self.hover_color = (70,70,170)
        
    def draw_button(self,SCREEN,unlocked = True):
        # action = False
        button_rect = pygame.Rect(self.x,self.y,self.width,self.height)

        # if button_rect.collidepoint(pos):
        #     pygame.draw.rect(SCREEN,self.hover_color,button_rect)
            
        #     if (pygame.mouse.get_pressed()[0]):
        #         self.clicked = True
            
        #     if(self.clicked == True and pygame.mouse.get_pressed()[0] == False):
        #             action = True
        #             print("trigger")
        #             self.clicked = False
        #             return action       
        # else:
        
        if(unlocked == True):
            pygame.draw.rect(SCREEN,self.basic_color,button_rect)
        if(unlocked == False):
            pygame.draw.rect(SCREEN,self.hover_color,button_rect)
        
        font = pygame.font.Font('Assets/ARCADECLASSIC.TTF', 30)
        text = font.render(self.text, True, (255,255,255))
        text_len = text.get_width()
        SCREEN.blit(text,((self.x + int(self.width/2) - int(text_len / 2)), self.y + 25))
        # return action

class Bullet(pygame.sprite.Sprite):

    def __init__(self,x_pos,y_pos,group):
        super().__init__(group)
        self.velocity = 50

        self.image = BULLET.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos,y_pos)
        self.mask = pygame.mask.from_surface(self.image)
    
    def update(self):
        self.rect.x += self.velocity
        #kills the sprite when it is offscreen
        if(self.rect.x > SCREEN_W + 100):
            self.kill()
    
    def draw(self,display):
        display.blit(self.image,self.rect)








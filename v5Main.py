'''Uses menu and levels. After reaching 1000 points, next level is unlocked. Each level scrolls infinitely. References v3Constants'''

import pygame
from sys import exit
from v3Constants import *
from v3Classes import *
from random import randint

pygame.init()
pygame.mixer.init()

SCREEN = pygame.display.set_mode((1200, 600))

buttons = pygame.sprite.Group()
player_group = pygame.sprite.Group()
obstacle_group = pygame.sprite.Group()

pygame.display.set_caption('Dino Game v5')
clock = pygame.time.Clock()
global high_score
high_score = 0
levels = {
    0:True,
    1:True,
    2:True,
    3:False,
    4:False
}

class Button(pygame.sprite.Sprite):

    def __init__(self, images, pos, groups, level, avalibility):
        super().__init__(groups)
        self.avalible = avalibility
        if self.avalible == True:
            self.image = images[0]
        else:
            self.image = images[1]
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.level = level

    def draw(self,SCREEN):
        SCREEN.blit(self.image,self.rect)

    def play_level(self):
        self.level()

def level0_loop(): # defult
    global x_pos_bg, y_pos_bg, x_pos_backdrop, y_pos_backdrop, points, game_speed
    player = Player_0(SCREEN, player_group)
    game_speed = 14
    points = 0
    death_count = 0
    x_pos_bg = 0
    y_pos_bg = GROUND_LOCATION + 100
    x_pos_backdrop = 0
    y_pos_backdrop = 115
    font = pygame.font.Font('Assets/ARCADECLASSIC.TTF', 30)

    def move_ground():
        global x_pos_bg, y_pos_bg
        ground_img = GROUND.convert_alpha()
        image_width = ground_img.get_width()
        SCREEN.blit(ground_img, (x_pos_bg, y_pos_bg))
        SCREEN.blit(ground_img, (x_pos_bg + image_width, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(ground_img, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    def move_backdrop():
        global x_pos_backdrop, y_pos_backdrop
        backdrop_img = BACKDROP.convert_alpha()
        image_width = backdrop_img.get_width()
        SCREEN.blit(backdrop_img, (x_pos_backdrop, y_pos_backdrop))
        SCREEN.blit(backdrop_img, (image_width + x_pos_backdrop, y_pos_backdrop))
        if x_pos_backdrop <= -image_width:
            SCREEN.blit(backdrop_img, (image_width + x_pos_backdrop, y_pos_backdrop))
            x_pos_backdrop = 0
        x_pos_backdrop -= (game_speed * 0.3)

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        text = font.render(f'Score  ' + str(points), True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (SCREEN_W - text_rect.width - 20, 40)
        h_text = font.render('HI  '+ str(high_score), True, (100,100,100))
        h_text_rect = h_text.get_rect()
        h_text_rect.center = (880, 40)
        if points < 1000:
            c1_text = font.render('Reach 1000 points',True, (0,0,0))
            c2_text = font.render('to unlock the next level',True, (0,0,0))
        else:
            c1_text = font.render('Reach 1000 points',True, (0,255,0))
            c2_text = font.render('to unlock the next level',True, (0,255,0))
        c1_text_rect = c1_text.get_rect()
        c1_text_rect.left = 50
        c2_text_rect = c2_text.get_rect()
        c2_text_rect.top = c1_text_rect.bottom
        c2_text_rect.left = c1_text_rect.left
        SCREEN.blit(c1_text,c1_text_rect)
        SCREEN.blit(c2_text,c2_text_rect)
        SCREEN.blit(h_text, h_text_rect)
        SCREEN.blit(text, text_rect)

    while True:

        if len(obstacle_group) == 0:
            obstacle = GroundObstacle(SMALL_OBST[0],obstacle_group)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # if event.type == pygame.KEYDOWN:   # for testing collisions
            #     if event.key == pygame.K_m:
            #         SHOW_MASKS = not(SHOW_MASKS)

        SCREEN.fill("white")
        user_input = pygame.key.get_pressed()

        move_backdrop()
        move_ground()

        player.update(user_input)
        for obstacle in obstacle_group:
            obstacle.update(game_speed)

        player.draw(SCREEN)
        for obstacle in obstacle_group:
            obstacle.draw(SCREEN)
            overlap_area = player.mask.overlap_area(obstacle.mask, (obstacle.rect.x - player.rect.x, obstacle.rect.y - player.rect.y))
            if 30 < overlap_area:
                if points < 1000:
                    death_count += 1
                    pygame.time.delay(2000)
                    player_group.empty()
                    for obstacle in obstacle_group:
                        obstacle.kill()
                    menu(death_count,points,0)
                else:
                    pygame.time.delay(2000)
                    player_group.empty()
                    for obstacle in obstacle_group:
                        obstacle.kill()
                    obstacle_group.empty()
                    menu(death_count, points, 2)


        if len(obstacle_group) == 0:
            if randint(0,2) == 0:
                new_obst = GroundObstacle(SMALL_OBST[0],obstacle_group)
            elif randint(0,2) == 1:
                new_obst = GroundObstacle(LARGE_OBST[0],obstacle_group)
                new_obst2 = GroundObstacle(SMALL_OBST[0],obstacle_group)
                new_obst2.rect.x = new_obst.X_POS + randint(400,1000)
            elif randint(0,2) == 2:
                new_obst = FlyingObstacle(FLYING_OBST,obstacle_group)
                new_obst2 = GroundObstacle(SMALL_OBST[0],obstacle_group)
                new_obst2.rect.x = new_obst.X_POS + randint(400,1000)
            elif randint(0,1) == 1:
                new_obst = FlyingObstacle(FLYING_OBST,obstacle_group)
                new_obst2 = GroundObstacle(LARGE_OBST[0],obstacle_group)
                new_obst2.rect.x = new_obst.X_POS + randint(300,2000)

        score()

        clock.tick(30)
        pygame.display.update()

def level1_loop(): # western
    global x_pos_bg, y_pos_bg, x_pos_backdrop, y_pos_backdrop, points, gs
    player = Player_1(SCREEN, player_group)
    revolver = Item1(player_group,(player.X_POS,player.Y_POS), ITEM1)
    gs = 14
    points = 0
    death_count = 0
    x_pos_bg = 0
    y_pos_bg = GROUND_LOCATION + 100
    x_pos_backdrop = 0
    y_pos_backdrop = 115
    font = pygame.font.Font('Assets/ARCADECLASSIC.TTF', 30)

    def move_ground():
        global x_pos_bg, y_pos_bg
        ground_img = GROUND1.convert_alpha()
        image_width = ground_img.get_width()
        SCREEN.blit(ground_img, (x_pos_bg, y_pos_bg))
        SCREEN.blit(ground_img, (x_pos_bg + image_width, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(ground_img, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= gs

    def move_backdrop():
        global x_pos_backdrop, y_pos_backdrop
        backdrop_img = BACKDROP1.convert_alpha()
        image_width = backdrop_img.get_width()
        SCREEN.blit(backdrop_img, (x_pos_backdrop, y_pos_backdrop))
        SCREEN.blit(backdrop_img, (image_width + x_pos_backdrop, y_pos_backdrop))
        if x_pos_backdrop <= -image_width:
            SCREEN.blit(backdrop_img, (image_width + x_pos_backdrop, y_pos_backdrop))
            x_pos_backdrop = 0
        x_pos_backdrop -= (gs * 0.3)

    def score():
        global points, gs
        points += 1
        if points % 100 == 0:
            gs += 1

        text = font.render(f'Score  ' + str(points), True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (SCREEN_W - text_rect.width - 20, 40)

        h_text = font.render('HI  '+ str(high_score), True, (100,100,100))
        h_text_rect = h_text.get_rect()
        h_text_rect.center = (880, 40)
        if points < 1000:
            c1_text = font.render('Reach 1000 points',True, (0,0,0))
            c2_text = font.render('to unlock the next level',True, (0,0,0))
        else:
            c1_text = font.render('Reach 1000 points',True, (0,255,0))
            c2_text = font.render('to unlock the next level',True, (0,255,0))
        c1_text_rect = c1_text.get_rect()
        c1_text_rect.left = 50
        c2_text_rect = c2_text.get_rect()
        c2_text_rect.top = c1_text_rect.bottom
        c2_text_rect.left = c1_text_rect.left
        SCREEN.blit(c1_text,c1_text_rect)
        SCREEN.blit(c2_text,c2_text_rect)
        SCREEN.blit(h_text, h_text_rect)
        SCREEN.blit(text, text_rect)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        SCREEN.fill("white")
        user_input = pygame.key.get_pressed()

        move_backdrop()
        move_ground()

        player.update(user_input)
        revolver.update(player, user_input, SCREEN)
        for obstacle in obstacle_group:
            obstacle.update(gs)

        player.draw(SCREEN)
        revolver.draw(SCREEN)
        for obstacle in obstacle_group:
            obstacle.draw(SCREEN)
            overlap_area = player.mask.overlap_area(obstacle.mask, (obstacle.rect.x - player.rect.x, obstacle.rect.y - player.rect.y))
            if 100 < overlap_area:
                if points < 1000:
                    death_count += 1
                    pygame.time.delay(2000)
                    player_group.empty()
                    for obstacle in obstacle_group:
                        obstacle.kill()
                    menu(death_count,points,0)
                else:
                    pygame.time.delay(2000)
                    player_group.empty()
                    for obstacle in obstacle_group:
                        obstacle.kill()
                    obstacle_group.empty()
                    menu(death_count, points, 3)

        if len(obstacle_group) == 0:
            if randint(0,2) == 0:
                new_obst = GroundObstacle1(SMALL_OBST1,obstacle_group)
            # elif randint(0,2) == 1:
            #     new_obst = GroundObstacle1(LARGE_OBST[0],obstacle_group)
            #     new_obst2 = GroundObstacle1(SMALL_OBST[0],obstacle_group)
            #     new_obst2.rect.x = new_obst.X_POS + randint(400,1000)
            elif randint(0,2) == 2:
                new_obst = FlyingObstacle1(FLYING_OBST1,obstacle_group)
                new_obst2 = GroundObstacle1(SMALL_OBST1,obstacle_group)
                new_obst2.rect.x = new_obst.X_POS + randint(400,1000)
            elif randint(0,1) == 1:
                new_obst = FlyingObstacle1(FLYING_OBST1,obstacle_group)
                # new_obst2 = GroundObstacle1(LARGE_OBST1,obstacle_group)
                # new_obst2.rect.x = new_obst.X_POS + randint(300,2000)

        score()

        clock.tick(30)
        pygame.display.update()

def level2_loop(): # WWI
    global x_pos_bg, y_pos_bg, x_pos_backdrop, y_pos_backdrop, points, gs
    player = Player_2(SCREEN, player_group)
    # revolver = Item(player_group,(player.X_POS,player.Y_POS), ITEM1)
    gs = 14
    points = 0
    death_count = 0
    x_pos_bg = 0
    y_pos_bg = GROUND_LOCATION + 100
    x_pos_backdrop = 0
    y_pos_backdrop = 115
    font = pygame.font.Font('Assets/ARCADECLASSIC.TTF', 30)
    # background_music = WWIMUSIC
    # background_music.play(loop=-1)

    def move_ground():
        global x_pos_bg, y_pos_bg
        ground_img = GROUND2.convert_alpha()
        image_width = ground_img.get_width()
        SCREEN.blit(ground_img, (x_pos_bg, y_pos_bg))
        SCREEN.blit(ground_img, (x_pos_bg + image_width, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(ground_img, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= gs

    def move_backdrop():
        global x_pos_backdrop, y_pos_backdrop
        backdrop_img = BACKDROP2.convert_alpha()
        image_width = backdrop_img.get_width()
        SCREEN.blit(backdrop_img, (x_pos_backdrop, y_pos_backdrop))
        SCREEN.blit(backdrop_img, (image_width + x_pos_backdrop, y_pos_backdrop))
        if x_pos_backdrop <= -image_width:
            SCREEN.blit(backdrop_img, (image_width + x_pos_backdrop, y_pos_backdrop))
            x_pos_backdrop = 0
        x_pos_backdrop -= (gs * 0.3)

    def score():
        global points, gs
        points += 1
        if points % 100 == 0:
            gs += 1

        text = font.render(f'Score  ' + str(points), True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (SCREEN_W - text_rect.width - 20, 40)

        h_text = font.render('HI  '+ str(high_score), True, (100,100,100))
        h_text_rect = h_text.get_rect()
        h_text_rect.center = (880, 40)
        if points < 1000:
            c1_text = font.render('Reach 1000 points',True, (0,0,0))
            c2_text = font.render('to unlock the next level',True, (0,0,0))
        else:
            c1_text = font.render('Reach 1000 points',True, (0,255,0))
            c2_text = font.render('to unlock the next level',True, (0,255,0))
        c1_text_rect = c1_text.get_rect()
        c1_text_rect.left = 50
        c2_text_rect = c2_text.get_rect()
        c2_text_rect.top = c1_text_rect.bottom
        c2_text_rect.left = c1_text_rect.left
        SCREEN.blit(c1_text,c1_text_rect)
        SCREEN.blit(c2_text,c2_text_rect)
        SCREEN.blit(h_text, h_text_rect)
        SCREEN.blit(text, text_rect)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        SCREEN.fill("white")
        user_input = pygame.key.get_pressed()

        move_backdrop()
        move_ground()

        player.update(user_input)
        # revolver.update(player)
        for obstacle in obstacle_group:
            obstacle.update(gs)

        player.draw(SCREEN)
        # revolver.draw(SCREEN)
        for obstacle in obstacle_group:
            obstacle.draw(SCREEN)
            overlap_area = player.mask.overlap_area(obstacle.mask, (obstacle.rect.x - player.rect.x, obstacle.rect.y - player.rect.y))
            if 30 < overlap_area:
                if points < 1000:
                    death_count += 1
                    pygame.time.delay(2000)
                    player_group.empty()
                    for obstacle in obstacle_group:
                        obstacle.kill()
                    menu(death_count,points,0)
                else:
                    pygame.time.delay(2000)
                    player_group.empty()
                    for obstacle in obstacle_group:
                        obstacle.kill()
                    obstacle_group.empty()
                    menu(death_count, points, 4)

        if len(obstacle_group) == 0:
            if randint(0,2) == 0:
                new_obst = Mine2(SMALL_OBST2,obstacle_group)
            elif randint(0,2) == 1:
                new_obst = GroundObstacle(LARGE_OBST2[randint(0,2)],obstacle_group)
                new_obst2 = GroundObstacle(SMALL_OBST2[0],obstacle_group)
                new_obst2.rect.x = new_obst.X_POS + randint(400,1000)
            elif randint(0,2) == 2:
                new_obst = FlyingObstacle2(FLYING_OBST2,obstacle_group)
                new_obst2 = GroundObstacle(LARGE_OBST2[randint(0,2)],obstacle_group)
                new_obst2.rect.x = new_obst.X_POS + randint(400,1000)
            elif randint(0,1) == 1:
                new_obst = FlyingObstacle2(FLYING_OBST2,obstacle_group)
                new_obst2 = GroundObstacle(SMALL_OBST2[0],obstacle_group)
                new_obst2.rect.x = new_obst.X_POS + randint(300,2000)

        score()

        clock.tick(30)
        pygame.display.update()

def level3_loop(): # star wars
    global x_pos_bg, y_pos_bg, x_pos_backdrop, y_pos_backdrop, points, gs
    player = Player_3(SCREEN, player_group)
    # lightsaber = Item(player_group,(player.X_POS,player.Y_POS), ITEM3)
    gs = 14
    points = 0
    death_count = 0
    x_pos_bg = 0
    y_pos_bg = GROUND_LOCATION + 100
    x_pos_backdrop = 0
    y_pos_backdrop = 115
    font = pygame.font.Font('Assets/ARCADECLASSIC.TTF', 30)

    def move_ground():
        global x_pos_bg, y_pos_bg
        ground_img = GROUND3.convert_alpha()
        image_width = ground_img.get_width()
        SCREEN.blit(ground_img, (x_pos_bg, y_pos_bg))
        SCREEN.blit(ground_img, (x_pos_bg + image_width, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(ground_img, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= gs

    def move_backdrop():
        global x_pos_backdrop, y_pos_backdrop
        backdrop_img = BACKDROP3.convert_alpha()
        image_width = backdrop_img.get_width()
        SCREEN.blit(backdrop_img, (x_pos_backdrop, y_pos_backdrop))
        SCREEN.blit(backdrop_img, (image_width + x_pos_backdrop, y_pos_backdrop))
        if x_pos_backdrop <= -image_width:
            SCREEN.blit(backdrop_img, (image_width + x_pos_backdrop, y_pos_backdrop))
            x_pos_backdrop = 0
        x_pos_backdrop -= (gs * 0.3)


    def score():
        global points, gs
        points += 1
        if points % 100 == 0:
            gs += 1

        text = font.render(f'Score  ' + str(points), True, (255,255,255))
        text_rect = text.get_rect()
        text_rect.center = (SCREEN_W - text_rect.width - 20, 40)

        h_text = font.render('HI  '+ str(high_score), True, (100,100,100))
        h_text_rect = h_text.get_rect()
        h_text_rect.center = (880, 40)
        if points < 1000:
            c1_text = font.render('Reach 1000 points',True, (0,0,0))
            c2_text = font.render('to unlock the next level',True, (0,0,0))
        else:
            c1_text = font.render('Reach 1000 points',True, (0,255,0))
            c2_text = font.render('to unlock the next level',True, (0,255,0))
        c1_text_rect = c1_text.get_rect()
        c1_text_rect.left = 50
        c2_text_rect = c2_text.get_rect()
        c2_text_rect.top = c1_text_rect.bottom
        c2_text_rect.left = c1_text_rect.left
        SCREEN.blit(c1_text,c1_text_rect)
        SCREEN.blit(c2_text,c2_text_rect)
        SCREEN.blit(h_text, h_text_rect)
        SCREEN.blit(text, text_rect)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        SCREEN.fill("black")
        user_input = pygame.key.get_pressed()

        move_backdrop()
        move_ground()

        player.update(user_input)
        # lightsaber.update(player)
        for obstacle in obstacle_group:
            obstacle.update(gs)

        player.draw(SCREEN)
        # lightsaber.draw(SCREEN)
        for obstacle in obstacle_group:
            obstacle.draw(SCREEN)
            overlap_area = player.mask.overlap_area(obstacle.mask, (obstacle.rect.x - player.rect.x, obstacle.rect.y - player.rect.y))
            if 30 < overlap_area:
                death_count += 1
                pygame.time.delay(2000)
                player_group.empty()
                for obstacle in obstacle_group:
                    obstacle.kill()
                menu(death_count, points, 0)

        if len(obstacle_group) == 0:
            if randint(0,2) == 0:
                new_obst = GroundObstacle(SMALL_OBST3[0],obstacle_group)
            elif randint(0,2) == 1: 
                new_obst = GroundObstacle(LARGE_OBST3[randint(0,2)],obstacle_group)
                new_obst2 = GroundObstacle(SMALL_OBST3[0],obstacle_group)
                new_obst2.rect.x = new_obst.X_POS + randint(400,700)
            elif randint(0,2) == 2:
                new_obst = FlyingObstacle3(FLYING_OBST3,obstacle_group)
            elif randint(0,1) == 1: 
                new_obst = GroundObstacle(LARGE_OBST3[randint(0,2)],obstacle_group)
                new_obst2 = GroundObstacle(LARGE_OBST3[randint(0,2)],obstacle_group)
                new_obst2.rect.x = new_obst.X_POS + randint(400,1700)

        score()

        clock.tick(30)
        pygame.display.update()

def menu(death_count,points,lvlUnlocked):
    global high_score, levels
    if points > high_score:
        high_score = points

    levels[lvlUnlocked] = True
    button1 = Button(L1BUTTONS,(200,450),buttons,level0_loop, levels[1])
    button2 = Button(L2BUTTONS,(450,450),buttons,level1_loop, levels[2])
    button3 = Button(L3BUTTONS,(700,450),buttons,level2_loop, levels[3])
    button4 = Button(L4BUTTONS,(950,450),buttons,level3_loop, levels[4])
    font = pygame.font.Font('Assets/ARCADECLASSIC.TTF', 50)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                for button in buttons:
                    if button.avalible == True:
                        if button.rect.collidepoint(x, y):
                            button.play_level()

        SCREEN.fill('white')
        text = font.render("Select a  Level", True, (0,0,0))
        score = font.render("Score  " + str(points), True, (0,0,0))
        score_rect = score.get_rect()
        score_rect.right = (SCREEN_W)
        SCREEN.blit(score,score_rect)
        

        hi_score = font.render("High Score  " + str(high_score), True, (0,0,0))
        hi_score_rect = hi_score.get_rect()
        hi_score_rect.right = (SCREEN_W)
        hi_score_rect.top = score_rect.bottom
        SCREEN.blit(hi_score,hi_score_rect)

        text_rect = text.get_rect()
        text_rect.center = (SCREEN_W //2, SCREEN_H // 2)
        SCREEN.blit(text, text_rect)

        for button in buttons:
            button.draw(SCREEN)

        pygame.display.update()

if __name__ == "__main__":
    menu(0,0,0)

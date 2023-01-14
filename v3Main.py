'''Building main.py from the ground up starting with collision function'''

import pygame
from sys import exit
from v3Constants import *
from v3Classes import *
from random import randint

pygame.init()


def get_screen(fullscreen=None):
    if fullscreen == None:
        SCREEN = pygame.display.set_mode((SCREEN_W,SCREEN_H))
    else: 
        SCREEN = pygame.display.set_mode((SCREEN_W,SCREEN_H), pygame.FULLSCREEN)
    return SCREEN
    
SCREEN = get_screen()   # add 'full' for fullscreen mode
pygame.display.set_caption('Dino Game v3')
clock = pygame.time.Clock()

player_group = pygame.sprite.Group()
obstacle_group = pygame.sprite.Group()

def level_loop(high_score):
    global x_pos_bg, y_pos_bg, x_pos_backdrop, y_pos_backdrop, points, game_speed
    player = Player(player_group)
    game_speed = 14
    points = 0
    death_count = 0
    x_pos_bg = 0
    y_pos_bg = GROUND_LOCATION + 100
    x_pos_backdrop = 0
    y_pos_backdrop = -135  # may have to mess with this one depending on image
    font = pygame.font.Font('Assets/ARCADECLASSIC.TTF', 30)
    
    # SHOW_MASKS = True   # for testing collisions

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
        x_pos_backdrop -= (game_speed * 0.8)

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
        h_text_rect.center = (900, 40)
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
            # check collisions
            overlap_area = player.mask.overlap_area(obstacle.mask, (obstacle.rect.x - player.rect.x, obstacle.rect.y - player.rect.y))
            if overlap_area > 30:
                death_count += 1
                pygame.time.delay(2000)
                menu(death_count,high_score)

        if len(obstacle_group) == 0:
            if randint(0,2) == 0:
                new_obst = GroundObstacle(SMALL_OBST[0],obstacle_group)
            elif randint(0,2) == 1:
                new_obst = GroundObstacle(LARGE_OBST[0],obstacle_group)
            elif randint(0,2) == 2:
                new_obst = FlyingObstacle(FLYING_OBST,obstacle_group)

        # if SHOW_MASKS:    # for testing collisions
        #     SCREEN.blit(player.mask.to_surface(unsetcolor=(0, 0, 0, 0), setcolor=(255, 0, 255, 255)), (player.rect.x,player.rect.y))
        #     SCREEN.blit(obstacle.mask.to_surface(unsetcolor=(0, 0, 0, 0), setcolor=(255, 0, 255, 255)), (obstacle.rect.x, obstacle.rect.y))

        score()

        clock.tick(30)
        pygame.display.update()

def menu(death_count,high_score):
    global points

    while True:
        SCREEN.fill('white')
        font = pygame.font.Font('Assets/ARCADECLASSIC.TTF', 30)
        
        if death_count == 0:
            text = font.render("Press the Spacebar to Start", True, (0,0,0))
        elif death_count > 0:
            text = font.render("Press the Spacebar to Restart", True, (0,0,0))
            score = font.render("Score  " + str(points), True, (0,0,0))
            score_rect = score.get_rect()
            score_rect.center = (SCREEN_W // 2, SCREEN_H // 2 - 50)
            SCREEN.blit(score,score_rect)
            
            if points > high_score:
                high_score = points

            hi_score = font.render("High Score  " + str(high_score), True, (0,0,0))
            hi_score_rect = hi_score.get_rect()
            hi_score_rect.center = score_rect.center = (SCREEN_W // 2, SCREEN_H // 2 + 50)
            SCREEN.blit(hi_score,hi_score_rect)

        text_rect = text.get_rect()
        text_rect.center = (SCREEN_W //2, SCREEN_H // 2)
        SCREEN.blit(text, text_rect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    level_loop(high_score)

menu(death_count=0,high_score=0)
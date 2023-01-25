'''Defult dino game '''

import pygame, random
from v2Classes import *
from v2Constants import *

pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
# SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), pygame.FULLSCREEN) # Fullscreen mode for mac users

all_sprites = pygame.sprite.Group()

def main(high_score):
    global x_pos_bg, y_pos_bg, y_pos_backdrop, x_pos_backdrop, points, game_speed, obstacles
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur(all_sprites)
    cloud = Cloud()
    game_speed = 14
    x_pos_bg = 0
    y_pos_bg = 380          # vertical position of background (ground)
    x_pos_backdrop = 0
    y_pos_backdrop = -155   # vertical offset for backdrop image
    points = 0
    font = pygame.font.Font('Assets/ARCADECLASSIC.TTF', 30)
    obstacles = []
    death_count = 0

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        text = font.render(str(points), True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (1050, 40)

        h_text = font.render('HI  '+ str(high_score), True, (100,100,100))
        h_text_rect = h_text.get_rect()
        h_text_rect.center = (900, 40)
        SCREEN.blit(text, text_rect)
        SCREEN.blit(h_text, h_text_rect)

    def background():
        '''moves ground image'''
        global x_pos_bg, y_pos_bg
        BG.convert_alpha()
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    def backdrop():
        '''moves image behind all sprites'''
        global x_pos_backdrop, y_pos_backdrop
        BACKDROP.convert()
        image_width = BACKDROP.get_width()
        SCREEN.blit(BACKDROP, (x_pos_backdrop, y_pos_backdrop))
        SCREEN.blit(BACKDROP, (image_width + x_pos_backdrop, y_pos_backdrop))
        if x_pos_backdrop <= -image_width:
            SCREEN.blit(BACKDROP, (image_width + x_pos_backdrop, y_pos_backdrop))
            x_pos_backdrop = 0
        x_pos_backdrop -= (game_speed * 0.1)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill('white')
        userInput = pygame.key.get_pressed()

        backdrop()
        background()

        player.draw(SCREEN)
        player.update(userInput)

        if len(obstacles) == 0:
            if random.randint(0,2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS,all_sprites))
            elif random.randint(0,2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS,all_sprites))
            elif random.randint(0,2) == 2:
                obstacles.append(Bird(BIRD,all_sprites))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update(game_speed, obstacles)
            if pygame.sprite.collide_mask(obstacle,player) != None:
                pygame.time.delay(2000)
                death_count += 1
                menu(death_count,high_score)

        
        cloud.draw(SCREEN)
        cloud.update(game_speed)

        score()

        clock.tick(30)
        pygame.display.update()


def menu(death_count,high_score):
    global points
    run = True

    while run:
        SCREEN.fill('white')
        font = pygame.font.Font('Assets/ARCADECLASSIC.TTF', 30)

        if death_count == 0:
            text = font.render("Press the Spacebar to Start", True, (0,0,0))
        elif death_count > 0:
            text = font.render("Press the Spacebar to Restart", True, (0,0,0))
            score = font.render("Score  " + str(points), True, (0,0,0))
            score_rect = score.get_rect()
            score_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
            SCREEN.blit(score,score_rect)
            
            if points > high_score:
                high_score = points

            hi_score = font.render("High Score  " + str(high_score), True, (0,0,0))
            hi_score_rect = hi_score.get_rect()
            hi_score_rect.center = score_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(hi_score,hi_score_rect)

        text_rect = text.get_rect()
        text_rect.center = (SCREEN_WIDTH //2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, text_rect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
                    pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main(high_score)



menu(death_count=0, high_score=0)
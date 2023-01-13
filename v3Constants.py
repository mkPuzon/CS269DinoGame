'''File to hold constants and assets'''
import pygame

# Screen dimentions
SCREEN_W = 1200
SCREEN_H = 600

GROUND_LOCATION = 300

# Import assets for level 1 (defult)
RUNNING = [pygame.image.load("Assets/Dino/defaultRun1.png"),
           pygame.image.load(("Assets/Dino/defaultRun2.png"))]
JUMPING = pygame.image.load("Assets/Dino/defaultJump.png")
DUCKING = [pygame.image.load("Assets/Dino/defaultDuck1.png"),
           pygame.image.load("Assets/Dino/defaultDuck2.png")]
DEAD = pygame.image.load("Assets/Dino/defaultDead.png")
SMALL_OBST = [pygame.image.load("Assets/Cactus/smallCactus.png"),
                pygame.image.load("Assets/Cactus/smallCactus.png"),
                pygame.image.load("Assets/Cactus/smallCactus.png")]
LARGE_OBST = [pygame.image.load("Assets/Cactus/tallCactus.png"),
                pygame.image.load("Assets/Cactus/tallCactus.png"),
                pygame.image.load("Assets/Cactus/tallCactus.png")]
FLYING_OBST = [pygame.image.load("Assets/Bird/bird1.png"),
        pygame.image.load("Assets/Bird/bird2.png")]
CLOUD = pygame.image.load("Assets/Other/Cloud.png")
GROUND = pygame.image.load("Assets/Other/Track.png")
BACKDROP = pygame.image.load("Assets/Other/Backdrop.png")


# # Import assets for level 2 (WWI)


# # Import assets for level 3 (Western)


# # Import assets for level 4 (Star Wars)


# # Import assets for final boss/ boss fights
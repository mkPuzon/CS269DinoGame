'''File to hold constants and assets'''
import pygame, os

# Screen dimentions
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

# Import assets for level 1 (defult)
RUNNING = [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoRun2.png"))]
JUMPING = pygame.image.load(os.path.join("Assets/Dino", "DinoJump.png"))
DUCKING = [pygame.image.load(os.path.join("Assets/Dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2.png"))]
SMALL_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]
LARGE_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]
BIRD = [pygame.image.load(os.path.join("Assets/Bird", "Bird1.png")),
        pygame.image.load(os.path.join("Assets/Bird", "Bird2.png"))]
CLOUD = pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))
BG = pygame.image.load(os.path.join("Assets/Other", "Track.png"))
BACKDROP = pygame.image.load(os.path.join("Assets/Other", "Backdrop.png"))



# # Import assets for level 2 (WWI)
# RUNNING2 = [pygame.image.load(os.path.join("Assets/", "")),
#            pygame.image.load(os.path.join("Assets/", """))]
# JUMPING2 = pygame.image.load(os.path.join("Assets/", ""))
# DUCKING2 = [pygame.image.load(os.path.join("Assets/", ")),
#            pygame.image.load(os.path.join("Assets/", ""))]
# SMALL_OBSTACLE2 = [pygame.image.load(os.path.join("Assets/", "")),
#                 pygame.image.load(os.path.join("Assets/", "")),
#                 pygame.image.load(os.path.join("Assets/", ""))]
# LARGE_OBSTACLE2 = [pygame.image.load(os.path.join("Assets/", "")),
#                 pygame.image.load(os.path.join("Assets/", "")),
#                 pygame.image.load(os.path.join("Assets/", ""))]
# FLYING_OBSTACLE2 = [pygame.image.load(os.path.join("Assets/", "")),
#         pygame.image.load(os.path.join("Assets/", ""))]
# CLOUD2 = pygame.image.load(os.path.join("Assets/", ""))
# BG2 = pygame.image.load(os.path.join("Assets/", ""))
# BACKDROP2 = pygame.image.load(os.path.join("Assets/", ""))

# # Import assets for level 3 (Western)
# RUNNING3 = [pygame.image.load(os.path.join("Assets/", "")),
#            pygame.image.load(os.path.join("Assets/", """))]
# JUMPING3 = pygame.image.load(os.path.join("Assets/", ""))
# DUCKING3 = [pygame.image.load(os.path.join("Assets/", ")),
#            pygame.image.load(os.path.join("Assets/", ""))]
# SMALL_OBSTACLE3 = [pygame.image.load(os.path.join("Assets/", "")),
#                 pygame.image.load(os.path.join("Assets/", "")),
#                 pygame.image.load(os.path.join("Assets/", ""))]
# LARGE_OBSTACLE3 = [pygame.image.load(os.path.join("Assets/", "")),
#                 pygame.image.load(os.path.join("Assets/", "")),
#                 pygame.image.load(os.path.join("Assets/", ""))]
# FLYING_OBSTACLE3 = [pygame.image.load(os.path.join("Assets/", "")),
#         pygame.image.load(os.path.join("Assets/", ""))]
# CLOUD3 = pygame.image.load(os.path.join("Assets/", ""))
# BG3 = pygame.image.load(os.path.join("Assets/", ""))
# BACKDROP3 = pygame.image.load(os.path.join("Assets/", ""))

# # Import assets for level 4 (Star Wars)
# RUNNING4 = [pygame.image.load(os.path.join("Assets/", "")),
#            pygame.image.load(os.path.join("Assets/", """))]
# JUMPING4 = pygame.image.load(os.path.join("Assets/", ""))
# DUCKING4 = [pygame.image.load(os.path.join("Assets/", ")),
#            pygame.image.load(os.path.join("Assets/", ""))]
# SMALL_OBSTACLE4 = [pygame.image.load(os.path.join("Assets/", "")),
#                 pygame.image.load(os.path.join("Assets/", "")),
#                 pygame.image.load(os.path.join("Assets/", ""))]
# LARGE_OBSTACLE4 = [pygame.image.load(os.path.join("Assets/", "")),
#                 pygame.image.load(os.path.join("Assets/", "")),
#                 pygame.image.load(os.path.join("Assets/", ""))]
# FLYING_OBSTACLE4 = [pygame.image.load(os.path.join("Assets/", "")),
#         pygame.image.load(os.path.join("Assets/", ""))]
# CLOUD4 = pygame.image.load(os.path.join("Assets/", ""))
# BG4 = pygame.image.load(os.path.join("Assets/", ""))
# BACKDROP4 = pygame.image.load(os.path.join("Assets/", ""))

# # Import assets for final boss/ boss fights
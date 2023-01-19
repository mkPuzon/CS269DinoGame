'''File to hold constants and assets'''
import pygame

# Screen dimentions
SCREEN_W = 1200
SCREEN_H = 600

GROUND_LOCATION = 300

# Import assets for level 0 (defult)
RUNNING = [pygame.image.load("Assets/Dino/defaultRun1.png"),
           pygame.image.load(("Assets/Dino/defaultRun2.png"))]
JUMPING = pygame.image.load("Assets/Dino/defaultJump.png")
DUCKING = [pygame.image.load("Assets/Dino/defaultDuck1.png"),
           pygame.image.load("Assets/Dino/defaultDuck2.png")]
DEAD = pygame.image.load("Assets/Dino/defaultDead.png")
SMALL_OBST = [pygame.image.load("Assets/GroundObst/smallCactus.png"),
                pygame.image.load("Assets/GroundObst/smallCactus.png"),
                pygame.image.load("Assets/GroundObst/smallCactus.png")]
LARGE_OBST = [pygame.image.load("Assets/GroundObst/tallCactus.png"),
                pygame.image.load("Assets/GroundObst/tallCactus.png"),
                pygame.image.load("Assets/GroundObst/tallCactus.png")]
FLYING_OBST = [pygame.image.load("Assets/FlyingObst/bird1.png"),
        pygame.image.load("Assets/FlyingObst/bird2.png")]
GRAPHICS = pygame.image.load("Assets/Other/Cloud.png")
GROUND = pygame.image.load("Assets/Other/TrackFilled.png")
BACKDROP = pygame.image.load("Assets/Other/defultBackdrop.png")

# Import assets for level 1 (Western)
RUNNING1 = [pygame.image.load("Assets/Dino/westernRun1.png"),
           pygame.image.load(("Assets/Dino/westernRun2.png"))]
JUMPING1 = pygame.image.load("Assets/Dino/westernJump.png")
DUCKING1 = [pygame.image.load("Assets/Dino/westernDuck1.png"),
           pygame.image.load("Assets/Dino/westernDuck2.png")]
DEAD1 = pygame.image.load("Assets/Dino/westernDead.png")
ITEM1 = [pygame.image.load("Assets/Other/revolver.png"),pygame.image.load("Assets/Other/revolverShooting.png")]

SMALL_OBST1 = [pygame.image.load("Assets/GroundObst/Tumbleweed.png"),
                pygame.image.load("Assets/GroundObst/Tumbleweed2.png"),
                pygame.image.load("Assets/GroundObst/Tumbleweed.png")]
# LARGE_OBST1 = [pygame.image.load("Assets/GroundObst/.png"),
#                 pygame.image.load("Assets/GroundObst/.png"),
#                 pygame.image.load("Assets/GroundObst/.png")]
FLYING_OBST1 = [pygame.image.load("Assets/FlyingObst/boomerang.png"),
        pygame.image.load("Assets/FlyingObst/boomerang2.png"), pygame.image.load("Assets/FlyingObst/boomerang3.png"),
        pygame.image.load("Assets/FlyingObst/boomerang4.png")]
# GRAPHICS1 = pygame.image.load("Assets/Other/.png")
GROUND1 = pygame.image.load("Assets/Other/TrackFilled.png")
BACKDROP1 = pygame.image.load("Assets/Other/westernBackdrop.png")

# Import assets for level 2 (WWI)
RUNNING2 = [pygame.image.load("Assets/Dino/defaultRun1.png"),
           pygame.image.load(("Assets/Dino/defaultRun2.png"))]
JUMPING2 = pygame.image.load("Assets/Dino/defaultJump.png")
DUCKING2 = [pygame.image.load("Assets/Dino/defaultDuck1.png"),
           pygame.image.load("Assets/Dino/defaultDuck2.png")]
DEAD2 = pygame.image.load("Assets/Dino/defaultDead.png")
SMALL_OBST2 = [pygame.image.load("Assets/GroundObst/smallCactus.png"),
                pygame.image.load("Assets/GroundObst/smallCactus.png"),
                pygame.image.load("Assets/GroundObst/smallCactus.png")]
LARGE_OBST2 = [pygame.image.load("Assets/GroundObst/sandbags.png"),
                pygame.image.load("Assets/GroundObst/sandbagsWithWire.png"),
                pygame.image.load("Assets/GroundObst/sandbagsWithWire.png")]
FLYING_OBST2 = [pygame.image.load("Assets/FlyingObst/ww1Plane1.png"),
        pygame.image.load("Assets/FlyingObst/ww1Plane2.png")]
GRAPHICS2 = pygame.image.load("Assets/Other/Cloud.png")
GROUND2 = pygame.image.load("Assets/Other/TrackFilled.png")
BACKDROP2 = pygame.image.load("Assets/Other/ww1Backdrop.png")

# # Import assets for level 3 (Star Wars)
# RUNNING3 = [pygame.image.load("Assets/Dino/.png"),
#            pygame.image.load(("Assets/Dino/.png"))]
# JUMPING3 = pygame.image.load("Assets/Dino/.png")
# DUCKING3 = [pygame.image.load("Assets/Dino/.png"),
#            pygame.image.load("Assets/Dino/.png")]
# DEAD3 = pygame.image.load("Assets/Dino/.png")
# SMALL_OBST3 = [pygame.image.load("Assets/GroundObst/.png"),
#                 pygame.image.load("Assets/GroundObst/.png"),
#                 pygame.image.load("Assets/GroundObst/.png")]

RUNNING3 = [pygame.image.load("Assets/Dino/defaultRun1.png"),
           pygame.image.load(("Assets/Dino/defaultRun2.png"))]
JUMPING3 = pygame.image.load("Assets/Dino/defaultJump.png")
DUCKING3 = [pygame.image.load("Assets/Dino/defaultDuck1.png"),
           pygame.image.load("Assets/Dino/defaultDuck2.png")]
DEAD3 = pygame.image.load("Assets/Dino/defaultDead.png")

LARGE_OBST3 = [pygame.image.load("Assets/GroundObst/Stormtrooper.png"),
                pygame.image.load("Assets/GroundObst/Stormtrooper.png"),
                pygame.image.load("Assets/GroundObst/StormtrooperWithGun.png")]
FLYING_OBST3 = pygame.image.load("Assets/FlyingObst/MilleniumFalcon.png")
# GRAPHICS3 = pygame.image.load("Assets/Other/.png")
GROUND3 = pygame.image.load("Assets/Other/starWarsTrack.png")
BACKDROP3 = pygame.image.load("Assets/Other/starWarsBackdrop.png")

# # Import assets for final boss/ boss fights
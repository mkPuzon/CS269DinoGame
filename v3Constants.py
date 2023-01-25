'''File to hold constants and assets'''
import pygame
pygame.mixer.init()

pygame.init()
# Screen dimentions
SCREEN_W = 1500
SCREEN_H = 600

GROUND_LOCATION = 300

#mMenu Assets
BUTTON1 = pygame.image.load("Assets/Buttons/button_one.png")
CURSOR = pygame.image.load("Assets/cursor.png")
MENU_MOVE = pygame.mixer.Sound('Assets/Sound/menu_move.wav')
MENU_SELECT = pygame.mixer.Sound('Assets/Sound/select.wav')

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
AMMO1 = pygame.image.load("Assets/Other/test_bullet.png")
SMALL_OBST1 = [pygame.image.load("Assets/GroundObst/Tumbleweed.png"),
                pygame.image.load("Assets/GroundObst/Tumbleweed2.png")]
LARGE_OBST1 = pygame.image.load("Assets/GroundObst/horse.png")
FLYING_OBST1 = [pygame.image.load("Assets/FlyingObst/horseshoe1.png"),
        pygame.image.load("Assets/FlyingObst/horseshoe2.png"), pygame.image.load("Assets/FlyingObst/horseshoe3.png"),
        pygame.image.load("Assets/FlyingObst/horseshoe4.png")]
BULLET1 = pygame.image.load("Assets/Other/test_bullet.png")
# GRAPHICS1 = pygame.image.load("Assets/Other/.png")
GROUND1 = pygame.image.load("Assets/Other/TrackFilled.png")
BACKDROP1 = pygame.image.load("Assets/Other/westernBackdrop.png")

# Import assets for level 2 (WWI)
RUNNING2 = [pygame.image.load("Assets/Dino/wwiRun1.png"),
           pygame.image.load(("Assets/Dino/wwiRun2.png"))]
JUMPING2 = pygame.image.load("Assets/Dino/wwiRun1.png")
DUCKING2 = [pygame.image.load("Assets/Dino/wwiDuck1.png"),
           pygame.image.load("Assets/Dino/ww1Duck2.png")]
DEAD2 = pygame.image.load("Assets/Dino/wwiDead.png")
SMALL_OBST2 = [pygame.image.load("Assets/GroundObst/landmine1.png"),
                pygame.image.load("Assets/GroundObst/landmine2.png")]
LARGE_OBST2 = [pygame.image.load("Assets/GroundObst/sandbags.png"),
                pygame.image.load("Assets/GroundObst/sandbagsWithWire.png"),
                pygame.image.load("Assets/GroundObst/sandbagsWithWire.png")]
FLYING_OBST2 = [pygame.image.load("Assets/FlyingObst/ww1Plane1.png"),
        pygame.image.load("Assets/FlyingObst/ww1Plane2.png")]
GRAPHICS2 = pygame.image.load("Assets/Other/Cloud.png")
GROUND2 = pygame.image.load("Assets/Other/TrackFilled.png")
BACKDROP2 = pygame.image.load("Assets/Other/ww1Backdrop.png")

# Import assets for level 3 (Star Wars)
RUNNING3 = [pygame.image.load("Assets/Dino/spaceRun1.png"),
           pygame.image.load(("Assets/Dino/spaceRun2.png"))]
JUMPING3 = pygame.image.load("Assets/Dino/spaceRun1.png")
DUCKING3 = [pygame.image.load("Assets/Dino/spaceDuck1.png"),
           pygame.image.load("Assets/Dino/spaceDuck2.png")]
DEAD3 = pygame.image.load("Assets/Dino/spaceDead.png")
SMALL_OBST3 = [pygame.image.load("Assets/GroundObst/droid.png"),
                pygame.image.load("Assets/GroundObst/droid.png"),
                pygame.image.load("Assets/GroundObst/droid.png")]
LARGE_OBST3 = [pygame.image.load("Assets/GroundObst/Stormtrooper.png"),
                pygame.image.load("Assets/GroundObst/Stormtrooper.png"),
                pygame.image.load("Assets/GroundObst/StormtrooperWithGun.png")]
FLYING_OBST3 = pygame.image.load("Assets/FlyingObst/MilleniumFalcon.png")
# GRAPHICS3 = pygame.image.load("Assets/Other/.png")
GROUND3 = pygame.image.load("Assets/Other/starWarsTrack.png")
BACKDROP3 = pygame.image.load("Assets/Other/starWarsBackdrop.png")

# Import sound assets
DEFULT_MUSIC = pygame.mixer.Sound("Assets/Sound/FirstLevelSoundtrack.wav")
WWI_MUSIC = pygame.mixer.Sound("Assets/Sound/ww1.wav")
WESTERN_MUSIC = pygame.mixer.Sound("Assets/Sound/Western.wav")
SPACE_MUSIC = pygame.mixer.Sound("Assets/Sound/StarWars8bit.wav")
MENU_MUSIC = pygame.mixer.Sound("Assets/Sound/menu.wav")

JUMP_SOUND = pygame.mixer.Sound("Assets/Sound/jump0.wav")
DEATH_SOUND = pygame.mixer.Sound("Assets/Sound/death.wav")
GUNSHOT_SOUND = pygame.mixer.Sound("Assets/Sound/gunshot.wav")
# TANK_SHOT_SOUND = pygame.mixer.Sound("Assets/Sound/.wav")
PLANE_SOUND = pygame.mixer.Sound("Assets/Sound/plane.wav")

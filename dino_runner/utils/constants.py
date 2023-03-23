import pygame
import os

# Global Constants
TITLE = "Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
pygame.init()
FONT_STYLE = "freesansbold.ttf"
FONT = pygame.font.Font(FONT_STYLE, 22)
FONT_COLOR = {'BLACK': (0, 0, 0), 'RED': (255, 0, 0), 'BLUE': (0, 0, 255), 'GREEN': (0, 255, 0),
              'WHITE': (255, 255, 255), 'YELLOW': (255, 255, 0), 'AQUA': (0, 255, 255)}
HALF_SCREEN_HEIGHT = SCREEN_HEIGHT //2
HALF_SCREEN_WIDTH = SCREEN_WIDTH //2

pygame.mixer.init()

IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")


SMALL_CACTUS_Y_POS = 520
LARGE_CACTUS_Y_POS = 495
BIRD_Y_POS = 465
THUNDER_CLOUD_Y_POS = 130

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"
SWORD_TYPE = "sword"

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Kirby/KirbyWalk.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Kirby/KirbyWalk2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Kirby/KirbyWalk3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Kirby/KirbyWalk4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Kirby/KirbyWalk5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Kirby/KirbyWalk6.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Kirby/KirbyWalk7.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Kirby/KirbyWalk8.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Kirby/KirbyWalk9.png"))
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

JUMPING = [
    pygame.image.load(os.path.join(IMG_DIR, "Kirby/KirbyJump1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Kirby/KirbyJump2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Kirby/KirbyJump3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Kirby/KirbyJump4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Kirby/KirbyJump5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Kirby/KirbyJump6.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Kirby/KirbyJump7.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Kirby/KirbyJump8.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Kirby/KirbyJump9.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Kirby/KirbyJump10.png"))
           ]
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Kirby/KirbySlide.png"))
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

THUNDER_CLOUD = [pygame.image.load(os.path.join(IMG_DIR, "ThunderCloud/ThunderCloud.png"))]
JUMPING_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, "Dino/Dino_Jump.mp3"))
DEATH_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, "Dino/Dino_Death.mp3"))
POINT_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, "Dino/Dino_Point.mp3"))

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

METEOR = pygame.image.load(os.path.join(IMG_DIR, "Meteor/Meteor.png")),

MUSIC_MENU = [
    os.path.join(IMG_DIR, "Music/Start_menu/Outset.mp3"),
    os.path.join(IMG_DIR, "Music/Start_menu/Begin_Your_Journey.mp3"),
    os.path.join(IMG_DIR, "Music/Start_menu/No_Destination.mp3"),
    os.path.join(IMG_DIR, "Music/Start_menu/The_Most_Powerful_Chicken.mp3")
]

MUSIC_PLAYING = [
    os.path.join(IMG_DIR, "Music/Background/Cronch.mp3"),
    os.path.join(IMG_DIR, "Music/Background/Bounty_Battle.mp3"),
    os.path.join(IMG_DIR, "Music/Background/Purple_Shade.mp3"),
    os.path.join(IMG_DIR, "Music/Background/8Bit_Adventure.mp3")
]

MUSIC_DEATH_MENU = [
    os.path.join(IMG_DIR, "Music/Death/TOSOS.mp3"),
    os.path.join(IMG_DIR, "Music/Death/The_Fastest_Snail.mp3"),
    os.path.join(IMG_DIR, "Music/Death/City_Over_Clouds.mp3")
]



""" RUNNING_SWORD = [
    pygame.image.load(os.path.join(IMG_DIR, 'Dino/DinoSword1.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Dino/DinoSword2.png')),
] """

#JUMPING_SWORD = pygame.image.load(os.path.join(IMG_DIR, 'Dino/DinoSword1.png'))

#DUCKING_SWORD = pygame.image.load(os.path.join(IMG_DIR, 'Dino/DinoSword2.png'))


CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))
#SWORD = pygame.image.load(os.path.join(IMG_DIR, 'Other/sword.png'))

BG = [
    pygame.image.load(os.path.join(IMG_DIR, 'Background/Track.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Background/background_01.jpg')),
    pygame.image.load(os.path.join(IMG_DIR, 'Background/background_03.jpg'))
      ]

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"

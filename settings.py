import pygame

WINDOW_NAME = "Venture Forth"
GAME_TITLE = WINDOW_NAME

SCREEN_WIDTH, SCREEN_HEIGHT = 1600, 800

FPS = 90
DRAW_FPS = True

# sizes
BUTTONS_SIZES = (400, 90)
HAND_SIZE = 200
HAND_HITBOX_SIZE = (60, 80)
CRYSTALFLYS_SIZES = (50, 38)
CRYSTALFLYS_SIZE_RANDOMIZE = (1,2)                               # for each new CRYSTALFLY, it will multiply the size with an random value beteewn X and Y
OCTOBABY_SIZES = (50, 50)
OCTOBABY_SIZE_RANDOMIZE = (1.2, 1.5)

# drawing
DRAW_HITBOX = False # will draw all the hitbox

# animation
ANIMATION_SPEED = 0.08 # the frame of the insects will change every X sec

# difficulty
GAME_DURATION = 60
CRYSTALFLYS_SPAWN_TIME = 1
CRYSTALFLYS_MOVE_SPEED = {"min": 1, "max": 5}
OCTOBABY_PENALITY = 1 

# colors
COLORS = {"title": (38, 61, 39), "score": (38, 61, 39), "timer": (204, 255, 51), "quote": (255, 51, 102),
            "buttons": {"default": (255, 165, 0), "second":  (179, 95, 5),
                        "text": (255, 255, 255), "shadow": (46, 54, 163)},
            "white": (255, 255, 255), "black": (0, 0, 0), "red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 255, 255),
            "yellow": (255, 255, 0), "orange": (255, 165, 0), "purple": (128, 0, 128), "gray": (128, 128, 128),
            "navy": (0, 0, 100), "pink": (255, 192, 203), "light_red": (255, 99, 71), "mocha": (164,120,100)} 
# sounds / music
MUSIC_VOLUME = 0.16 # value between 0 and 1
SOUNDS_VOLUME = 1

# fonts
pygame.font.init()
FONTS = {}
FONTS["small"] = pygame.font.Font("\Documents\Font\zh-cn.ttf", 40)
FONTS["medium"] = pygame.font.Font("\Documents\Font\zh-cn.ttf", 50)
FONTS["big"] = pygame.font.Font("\Documents\Font\zh-cn.ttf", 100)

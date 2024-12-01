import pygame

WINDOW_NAME = "Venture Forth"
GAME_TITLE = WINDOW_NAME

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 700

FPS = 90
DRAW_FPS = True

# sizes
BUTTONS_SIZES = (340, 90)
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
GAME_DURATION = 20 
CRYSTALFLYS_SPAWN_TIME = 1
CRYSTALFLYS_MOVE_SPEED = {"min": 1, "max": 5}
OCTOBABY_PENALITY = 1 

# colors
COLORS = {"title": (38, 61, 39), "score": (38, 61, 39), "timer": (204, 255, 51), "quote": (255, 51, 102),
            "buttons": {"default": (0, 255, 255), "second":  (255, 51, 153),
                        "text": (0, 0, 0), "shadow": (46, 54, 163)}} 
# sounds / music
MUSIC_VOLUME = 0.16 # value between 0 and 1
SOUNDS_VOLUME = 1

# fonts
pygame.font.init()
FONTS = {}
FONTS["small"] = pygame.font.Font(None, 40)
FONTS["medium"] = pygame.font.Font(None, 72)
FONTS["big"] = pygame.font.Font(None, 120)

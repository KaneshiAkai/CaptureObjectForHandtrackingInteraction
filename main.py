import pygame
import sys
import os
import ui
import time
from settings import *
from game import Game
from menu import Menu
from leaderboard import Leaderboard
from name import Name
from contributor import Contributor



# Setup pygame
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (70,50) # windows position
pygame.init()
pygame.display.set_caption(WINDOW_NAME)
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),0,32)

mainClock = pygame.time.Clock()

# Fonts 
fps_font = pygame.font.SysFont("coopbl", 22)

# Music 
pygame.mixer.music.load("Assets/Sounds/Passing Memories (feat. Faouzia) (Genshin Impact's 4Th Anniversary English Theme Song).mp3")
pygame.mixer.music.set_volume(MUSIC_VOLUME)
pygame.mixer.music.play(-1)
# Variables
state = "menu"
player = ''
# leaderboard_data = Leaderboard.ReadLeaderboard("leaderboard.csv")
# Creation 
game = Game(SCREEN, player)
menu = Menu(SCREEN)
leaderboard = Leaderboard(SCREEN)
contributor = Contributor(SCREEN)
count = 0
# HandPause = False


# Function
def user_events():
    global state, player
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif (event.key == pygame.K_q):
                if state == "game":
                    game.pause_start_time = time.time()
                    state = "pause"
                elif state == "pause":
                    game.game_start_time += time.time() - game.pause_start_time 
                    game.pause_start_time = None
                    state = "game"
# HandTracking.display_hand(SCREEN)

def update():
    global state, player, count, leaderboard_data, HandPause
    if state == "menu":
        menu_result = menu.update()
        if menu_result == "naming":
            state = "naming"
        elif menu_result == "leaderboard":
            print("leader2")
            state = "leaderboard"
        elif menu_result == "contributor":
            state = "contributor"
    elif state == "naming":
        player = Name(SCREEN).Login()
        if player == "menu":
            state = "menu"
        else:
            game.player = player 
            state = "game"
            game.reset() 
    elif state == "game":
        if game.update() == "leaderboard":
            state = "leaderboard"
        if game.update() == "pause":
            game.pause_start_time = time.time()
            state = "pause"
    elif state == "leaderboard":
        if count == 0:
            leaderboard_data = Leaderboard.ReadLeaderboard("leaderboard.csv")
            count += 1
        if leaderboard.DisplayLeaderboard(leaderboard_data) == "menu":
            del leaderboard_data
            count = 0
            state="menu"
    elif state == "pause":
        ui.draw_text(SCREEN, "Paused", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50), COLORS["quote"], font=FONTS["big"], pos_mode="center")
        ui.draw_text(SCREEN, "No Hand detected !!!", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5), COLORS["quote"], font=FONTS["medium"], pos_mode="center")
        game.load_camera()
        game.set_hand_position()
        if game.hand_tracking.hand_detected:
            # HandPause = False
            game.game_start_time += time.time() - game.pause_start_time 
            game.pause_start_time = None
            state = "game"
        if ui.button(SCREEN, SCREEN_HEIGHT // 2, "Quit", click_sound=pygame.mixer.Sound("Assets/Sounds/getout.wav")):
            state = "menu"
    elif state == "contributor":
        if contributor.update() == "menu":
            state = "menu"
        if contributor.update() == "thanks":
            state = "thanks"
    elif state == "thanks":
        if contributor.draw_thanks(SCREEN) == "menu":
            state = "menu"
    pygame.display.update()
    mainClock.tick(FPS)
    

while True:
    user_events()
    update()

    # FPS
    if DRAW_FPS:
        fps_label = fps_font.render(f"FPS: {int(mainClock.get_fps())}", 1, (255,200,20))
        SCREEN.blit(fps_label, (5,5))

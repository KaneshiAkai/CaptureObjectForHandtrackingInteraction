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



# Setup pygame
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (300,100) # windows position
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
count = 0



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
            elif event.key == pygame.K_q:
                if state == "game":
                    state = "pause"
                elif state == "pause":
                    state = "game"



def update():
    global state, player, count, leaderboard_data
    if state == "menu":
        if menu.update() == "naming":
            game.reset() 
            state = "naming"
    elif state == "naming":
        player = Name(SCREEN).Login()
        game.player = player 
        state = "game"
    elif state == "game":
        if game.update() == "leaderboard":
            state = "leaderboard"
    elif state == "leaderboard":
        if count == 0:
            leaderboard_data = Leaderboard.ReadLeaderboard("leaderboard.csv")
            count += 1
        if leaderboard.DisplayLeaderboard(leaderboard_data) == "menu":
            count = 0
            state="menu"
    elif state == "pause":
        ui.draw_text(SCREEN, "Paused", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50), COLORS["title"], font=FONTS["big"], pos_mode="center")
        if ui.button(SCREEN, SCREEN_HEIGHT // 2, "Quit", click_sound=pygame.mixer.Sound("Assets/Sounds/getout.wav")):
            state = "leaderboard"
    pygame.display.update()
    mainClock.tick(FPS)
    

while True:
    user_events()
    update()

    # FPS
    if DRAW_FPS:
        fps_label = fps_font.render(f"FPS: {int(mainClock.get_fps())}", 1, (255,200,20))
        SCREEN.blit(fps_label, (5,5))

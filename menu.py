import pygame
import sys
from settings import *
from background import Background
import ui


class Menu:
    def __init__(self, surface):
        self.surface = surface
        self.background = Background()
        self.click_sound = pygame.mixer.Sound(f"Assets/Sounds/slap.wav")
        self.getout = pygame.mixer.Sound(f"Assets/Sounds/getout.wav")

    def draw(self):
        self.background.draw(self.surface)
        # draw title
        ui.draw_text(self.surface, GAME_TITLE, (SCREEN_WIDTH//2, 120), COLORS["title"], font=FONTS["big"],
                    shadow=True, shadow_color=(255,255,255), pos_mode="center")
        # ui.draw_text(self.surface, "I will, VENTURE FORTH to the HUNT ", (SCREEN_WIDTH//3.2, 190), COLORS["quote"], font=FONTS["small"], shadow=False, shadow_color=None)

    def update(self):
        self.draw()
        if ui.button(self.surface, 340-BUTTONS_SIZES[1]*1.5, "Go Buddy", click_sound=self.getout):
            return "naming"
        
        if ui.button(self.surface, 340, "Leaderboard", click_sound=self.getout):
            return "leaderboard"

        if ui.button(self.surface, 340+BUTTONS_SIZES[1]*1.5, "Get out", click_sound=self.getout):
            pygame.quit()
            sys.exit()

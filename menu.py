import pygame
import sys
import time
from settings import *
from background import Background
import ui
import image


class Menu:
    def __init__(self, surface):
        self.surface = surface
        self.background = Background()
        self.click_sound = pygame.mixer.Sound(f"Assets/Sounds/slap.wav")
        self.getout = pygame.mixer.Sound(f"Assets/Sounds/button.wav")
        self.start = pygame.mixer.Sound(f"Assets/Sounds/start.wav")
        self.logo = image.load("Assets/logo.png", size=(700, 230))
        self.design = image.load("Assets/design.jpg", size=(300, 300))
        self.wordpress = image.load("Assets/wordpress.png", size=(200, 200))
        self.settin = image.load("Assets/settin.png", size=(100, 100))
        self.show_music_buttons = False
        self.last_settings_click_time = 0

    def draw(self):
        self.background.draw(self.surface)
        image.draw(self.surface, self.logo, (SCREEN_WIDTH // 2, 120), pos_mode="center")
        image.draw(self.surface, self.design, (SCREEN_WIDTH // 3.8, 300), pos_mode="center")
        # draw title
        # ui.draw_text(self.surface, GAME_TITLE, (SCREEN_WIDTH//2, 120), COLORS["title"], font=FONTS["big"],
        #             shadow=True, shadow_color=(255,255,255), pos_mode="center")
        # ui.draw_text(self.surface, "I will, VENTURE FORTH to the HUNT ", (SCREEN_WIDTH//3.2, 190), COLORS["quote"], font=FONTS["small"], shadow=False, shadow_color=None)

    def update(self):
        self.draw()
        if ui.button(self.surface, 400-BUTTONS_SIZES[1]*1.5, "Go Buddy", click_sound=self.start):
            return "naming"
        
        if ui.button(self.surface, 400, "Leaderboard", click_sound=None):
            print("leader")
            return "leaderboard"
        
        if ui.vertical_button(self.surface, 50, 80, "Contributors", click_sound=None):                  
            return "contributor"
        
        ui.linkWordpress(self.surface, self.wordpress, 1400, 150)

        if ui.button(self.surface, 400+BUTTONS_SIZES[1]*1.5, "Get out", click_sound=self.getout):
            pygame.quit()
            sys.exit()
        
        current_time = time.time()
        if ui.Settin(self.surface, self.settin, 1500, 700):
            if current_time - self.last_settings_click_time > CLICK_COOLDOWN:
                self.show_music_buttons = not self.show_music_buttons
                self.last_settings_click_time = current_time

        if self.show_music_buttons:
            self.MusicChanging()

    def MusicChanging(self):
        ui.music_button(self.surface, 260, "Zoltraak", Zoltraak, click_sound=None)
        ui.music_button(self.surface, 340, "Toward The Light", TowardTheLight, click_sound=None)
        ui.music_button(self.surface, 420, "Die For You", DieForYou, click_sound=None)
        ui.music_button(self.surface, 500, "Electro Swing", ElectroSwing, click_sound=None)
        ui.music_button(self.surface, 580, "Tender Strength", TenderStrength, click_sound=None)
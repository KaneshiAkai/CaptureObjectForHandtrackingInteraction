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
        self.design = image.load("Assets/design.jpg", size=(300, 300))
        self.logo = image.load("Assets/logo.png", size=(700, 230))
        self.wordpress = image.load("Assets/wordpress.png", size=(200, 200))
        self.settin = image.load("Assets/settin.png", size=(100, 100))
        self.show_music_buttons = False
        self.last_settings_click_time = 0
        self.show_skin_buttons = False
        
        #skin
        self.skins = [
            image.load("Assets/skin/huy.png", size=(100, 100)),
            image.load("Assets/skin/chill.jpg", size=(100, 100)),
            image.load("Assets/skin/thanos.jpg", size=(100, 100)),
            
        ]
        self.selected_skin = None



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
            
        if self.show_skin_buttons:
            self.SkinChanging()

    def MusicChanging(self):
        ui.music_button(self.surface, 260, "Zoltraak", Zoltraak, click_sound=None)
        ui.music_button(self.surface, 340, "Toward The Light", TowardTheLight, click_sound=None)
        ui.music_button(self.surface, 420, "Die For You", DieForYou, click_sound=None)
        ui.music_button(self.surface, 500, "Electro Swing", ElectroSwing, click_sound=None)
        ui.music_button(self.surface, 580, "Yêu 5", Yeu5, click_sound=None)
  
        
    def SkinChanging(self):
        pos_x, pos_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        width, height = 1000, 500
        rect = pygame.Rect(pos_x - width // 2, pos_y - height // 2, width, height)
        color = COLORS["blue"]
        pygame.draw.rect(self.surface, color, rect)
        # Display skin images and handle clicks
        for i, skin in enumerate(self.skins):
            skin_x = pos_x - width // 2 + (i * 150) + 50
            skin_y = pos_y - height // 2 + 50
            if skin == self.selected_skin:
                frame_color = COLORS["gray"]
            else:
                frame_color = COLORS["black"]
            pygame.draw.rect(self.surface, frame_color, (skin_x - 50, skin_y - 50, 100, 100), 5)
            image.draw(self.surface, skin, (skin_x, skin_y), pos_mode="center")
            if pygame.Rect(skin_x - 50, skin_y - 50, 100, 100).collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:
                    self.selected_skin = skin
                    ui.change_hand_skin(self.hand, skin)
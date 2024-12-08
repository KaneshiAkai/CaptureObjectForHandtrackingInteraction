import pygame
import image
from background import Background
import ui
from settings import *
import sys


class Contributor:
    def __init__(self, surface, image_path="Assets/background.png"):
        self.surface = surface
        self.background = Background()
        self.image = image.load(image_path, size=(SCREEN_WIDTH, SCREEN_HEIGHT), convert="default")
        self.design = image.load("Assets/design.jpg", size=(300, 300))
        self.contributor = [
            {"name": "Lương Xuân Thanh", "image": image.load("Assets/xuanthanh.png", size=(700,400))},
            {"name": "Bùi Quang Huy", "image": image.load("Assets/qunaghuy.png", size=(700,400))},
        ]
        self.thanks = [
            {"name": "Hoàng Quang Huy", "image": image.load("Assets/teacherHuy.png", size=(300,400))},
            {"name": "Sergio Canu", "image": image.load("Assets/pysource.jpg", size=(350,400))},
            {"name": "Nicholas Renotte", "image": image.load("Assets/mediapipe.jpg", size=(350,400))},
        ]
        

    def draw(self, surface):
        image.draw(surface, self.image, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), pos_mode="center")
        image.draw(surface, self.design, (SCREEN_WIDTH // 1.3, 650), pos_mode="center")
        for contributor in self.contributor:
            x_offset = 400
            y_offset = 250
            for contributor in self.contributor:
                image.draw(self.surface, contributor["image"], (x_offset,  y_offset), pos_mode="center")
                ui.draw_text(self.surface, contributor["name"], (x_offset, y_offset + 260), COLORS["yellow"], font=FONTS["medium"], pos_mode="center")
                x_offset += 800
            if ui.rect_button(self.surface, 600, "Special Thanks", click_sound=pygame.mixer.Sound("Assets/Sounds/button.wav")):
                return "thanks"

    def update(self):
        if self.draw(self.surface) == "thanks":
            return "thanks"
        if ui.button(self.surface, SCREEN_HEIGHT - 100, "Back to Menu", click_sound=None):
            return "menu"
        return "contributor"
        
    def draw_thanks(self, surface):
        image.draw(surface, self.image, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), pos_mode="center")
        image.draw(surface, self.design, (SCREEN_WIDTH // 7, 100), pos_mode="center")
        ui.draw_text(self.surface, "Special Thanks", (SCREEN_WIDTH // 2, 80), COLORS["quote"], font=FONTS["big"], pos_mode="center")
        x_offset = 300
        y_offset = 370
        frame_color_start = COLORS["black"]
        frame_color_end = COLORS["yellow"]
        frame_thickness = 10  # Increased thickness
        for thanks in self.thanks:
            # Draw gradient frame
            ui.draw_gradient_frame(surface, x_offset, y_offset, thanks["image"].get_width(), thanks["image"].get_height(), frame_thickness, frame_color_start, frame_color_end)
            # Draw image
            image.draw(self.surface, thanks["image"], (x_offset, y_offset), pos_mode="center")
            # Draw text
            ui.draw_text(self.surface, thanks["name"], (x_offset, y_offset + 260), COLORS["yellow"], font=FONTS["medium"], pos_mode="center")
            x_offset += 500
        if ui.button(self.surface, SCREEN_HEIGHT - 100, "Back to Menu", click_sound=pygame.mixer.Sound("Assets/Sounds/button.wav")):
            return "menu"
        pygame.display.flip()

    

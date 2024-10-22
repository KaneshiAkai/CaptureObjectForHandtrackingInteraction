import csv
import image
import pygame
import ui
from settings import *
from background import Background

class Leaderboard:   
    list_leaderboard = []
    def __init__(self, surface, image_path="Assets/background.jpg"):
        self.surface = surface
        self.background = Background()
        self.image = image.load(image_path, size=(SCREEN_WIDTH, SCREEN_HEIGHT), convert="default")
    
    def ReadLeaderboard(file_path):
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                Leaderboard.list_leaderboard.append({'player': row[0], 'score': int(row[1])})
        return Leaderboard.list_leaderboard
    
            
    def WriteLeaderboard(self, file_path, player, score):
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([player, score])

    def draw(self, surface):
        image.draw(surface, self.image, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), pos_mode="center")
    
    def DisplayLeaderboard(self, leaderboard):
        self.draw(self.surface)
        ui.draw_text(self.surface, "Leaderboard", (SCREEN_WIDTH // 2, 80), COLORS["title"], font=FONTS["big"], pos_mode="center")
        
        y_offset = 150
        for i in leaderboard:
            ui.draw_text(self.surface, f"{i['player']}: {i['score']}", (SCREEN_WIDTH // 2, y_offset), COLORS['quote'], font=FONTS["medium"], pos_mode="center")
            y_offset += 50
            if ui.button(self.surface, 540, "Back to Menu", click_sound = pygame.mixer.Sound("Assets/Sounds/getout.wav")):
                return "menu"
            
        pygame.display.update()
            

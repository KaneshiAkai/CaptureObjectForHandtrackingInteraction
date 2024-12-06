import csv
import image
import pygame
import ui
from settings import *
from background import Background

class Leaderboard:   
    list_leaderboard = []
    def __init__(self, surface, image_path="Assets/background.png"):
        self.surface = surface
        self.background = Background()
        self.image = image.load(image_path, size=(SCREEN_WIDTH, SCREEN_HEIGHT), convert="default")
        self.design = image.load("Assets/design.jpg", size=(300, 300))
        
    def ReadLeaderboard(file_path):
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                # if len(row) >= 2:
                Leaderboard.list_leaderboard.append({'player': row[0], 'score': int(row[1])})
        Leaderboard.list_leaderboard.sort(key=lambda arrange: arrange['score'], reverse=True)
        return Leaderboard.list_leaderboard
    
            
    def  WriteLeaderboard(file_path, player, score):
        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([player, score])

    def draw(self, surface):
        image.draw(surface, self.image, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), pos_mode="center")
    
    def DisplayLeaderboard(self, leaderboard):
        self.draw(self.surface)
        image.draw(self.surface, self.design, (SCREEN_WIDTH // 1.3, 300), pos_mode="center")
        ui.draw_text(self.surface, "Leaderboard", (SCREEN_WIDTH // 2, 80), COLORS["title"], font=FONTS["big"], pos_mode="center")
        
        y_offset = 200
        print("deptrai")
        n=0
        for i in leaderboard:
            if n<8:
                print("Thisishiddenone")
                ui.draw_text(self.surface, f"{i['player']}: {i['score']}", (SCREEN_WIDTH // 2, y_offset), COLORS['quote'], font=FONTS["medium"], pos_mode="center")
                y_offset += 50
                if ui.button(self.surface, 700, "Back to Menu", click_sound = pygame.mixer.Sound("Assets/Sounds/getout.wav")):
                    Leaderboard.list_leaderboard.clear()
                    return "menu"
            n+=1
        
        pygame.display.update()
            

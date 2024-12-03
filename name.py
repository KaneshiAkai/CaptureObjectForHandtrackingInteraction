from background import Background
import ui
import pygame
from settings import *

class Name:
    def __init__(self, surface):
        self.surface = surface
        self.background = Background()
        self.input_box = pygame.Rect(SCREEN_WIDTH // 2 - 100, 300, 200, 32)
        self.input_text=''
        self.font = pygame.font.Font(None,32)

    
    def Login(self):
        self.background.draw(self.surface)
        ui.draw_text(self.surface, "Login", (SCREEN_WIDTH // 2, 90), COLORS["title"], font=FONTS["big"], pos_mode="center")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.input_text, enter_pressed = ui.text_input(event, self.input_text)
                if enter_pressed:
                    return self.input_text
            ui.draw_input_box(self.surface, self.input_box, self.input_text, self.font)
            if ui.button(self.surface, 600, "Quit", click_sound=None):
                return "menu"
            pygame.display.flip()
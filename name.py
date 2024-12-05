from background import Background
import ui
import pygame
from settings import *
import image

class Name:
    def __init__(self, surface):
        self.surface = surface
        self.background = Background()
        self.input_box = pygame.Rect(SCREEN_WIDTH // 2 - 100, 400, 200, 32)
        self.input_text=''
        self.font = pygame.font.Font(None,32)
        self.border_color = COLORS["buttons"]["shadow"]
        self.border_thickness = 2
        self.padding = 5
        self.logo = image.load("Assets/logo.png", size=(700, 230))
        self.design = image.load("Assets/design.jpg", size=(300, 300))

    def draw_decorations(self):
        pygame.draw.rect(self.surface, self.border_color, self.input_box.inflate(self.padding * 2, self.padding * 2), self.border_thickness)
        pygame.draw.rect(self.surface, COLORS["buttons"]["default"], self.input_box.inflate(self.padding, self.padding), self.border_thickness)

    def Login(self):
        self.background.draw(self.surface)
        image.draw(self.surface, self.logo, (SCREEN_WIDTH // 2, 100), pos_mode="center")
        image.draw(self.surface, self.design, (SCREEN_WIDTH // 3.8, 200), pos_mode="center")
        ui.draw__white_border_text(self.surface, "Login", (SCREEN_WIDTH // 2, 300), COLORS["black"], font=FONTS["big"], pos_mode="center")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.input_text, enter_pressed = ui.text_input(event, self.input_text)
                if enter_pressed:
                    return self.input_text
                
            pygame.draw.rect(self.surface, COLORS["white"], self.input_box)
            pygame.draw.rect(self.surface, COLORS["buttons"]["shadow"], self.input_box, 2)  # Draw border
            self.draw_decorations()
            ui.draw_input_box(self.surface, self.input_box, self.input_text, self.font)
            if ui.button(self.surface, 600, "Quit", click_sound=None):
                return "menu"
            pygame.display.flip()
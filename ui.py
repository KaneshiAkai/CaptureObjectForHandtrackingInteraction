import pygame
from settings import *

def draw_text(surface, text, pos, color, font=FONTS["medium"], pos_mode="top_left",
                shadow=True, shadow_color=(255, 255, 255), shadow_offset=2):
    label = font.render(text, 1, color)
    label_rect = label.get_rect()
    if pos_mode == "top_left":
        label_rect.x, label_rect.y = pos
    elif pos_mode == "center":
        label_rect.center = pos

    if shadow: # make the shadow
        label_shadow = font.render(text, 1, shadow_color)
        surface.blit(label_shadow, (label_rect.x - shadow_offset, label_rect.y + shadow_offset))

    surface.blit(label, label_rect) # draw the text


def button(surface, pos_y, text=None, click_sound=None, font=FONTS["medium"]):
    width, height = BUTTONS_SIZES
    center_x = SCREEN_WIDTH // 2
    offset = 20  # Độ lệch để tạo hình bình hành

    # Tạo các điểm cho hình bình hành
    points = [
        (center_x - width // 2 + offset, pos_y),
        (center_x + width // 2 + offset, pos_y),
        (center_x + width // 2 - offset, pos_y + height),
        (center_x - width // 2 - offset, pos_y + height)
    ]

    on_button = False
    if pygame.mouse.get_pos()[0] > points[0][0] and pygame.mouse.get_pos()[0] < points[1][0] and \
       pygame.mouse.get_pos()[1] > points[0][1] and pygame.mouse.get_pos()[1] < points[2][1]:
        color = COLORS["buttons"]["second"]
        on_button = True
    else:
        color = COLORS["buttons"]["default"]

    pygame.draw.polygon(surface, color, points)  # Vẽ hình bình hành

    # Vẽ text
    if text is not None:
        draw_text(surface, text, (center_x, pos_y + height // 2), COLORS["buttons"]["text"], font=font, pos_mode="center",
                  shadow=True, shadow_color=COLORS["buttons"]["shadow"])

    if on_button and pygame.mouse.get_pressed()[0]:  # Nếu người dùng nhấn vào button
        if click_sound is not None:  # Phát âm thanh nếu cần
            click_sound.play()
        return True
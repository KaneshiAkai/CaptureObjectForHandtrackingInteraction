import pygame
from settings import *
import image
import webbrowser
import time 

last_click_time = 0
CLICK_COOLDOWN = 0.5

def draw_text(surface, text, pos, color, font=FONTS["medium"], pos_mode="top_left",
                shadow=True, shadow_color=(0,0,0), shadow_offset=3):  # Increased shadow_offset
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

def draw__white_border_text(surface, text, pos, color, font=FONTS["medium"], pos_mode="top_left",
                shadow=True, shadow_color=(255,255,255), shadow_offset=3):  # Increased shadow_offset
    label = font.render(text, 1, color)
    label_rect = label.get_rect()
    if pos_mode == "top_left":
        label_rect.x, label_rect.y = pos
    elif pos_mode == "center":
        label_rect.center = pos

    if shadow: # make the shadow
        label_shadow = font.render(text, 1, shadow_color)
        surface.blit(label_shadow, (label_rect.x - shadow_offset, label_rect.y + shadow_offset))

    surface.blit(label, label_rect)

def score_button(surface,pos_x, pos_y, color):
    width, height = BUTTONS_SIZES
    offset = 20  # Độ lệch để tạo hình bình hành

    # Tạo các điểm cho hình bình hành
    points = [
        (pos_x - width // 2 + offset, pos_y),
        (pos_x + width // 2 + offset, pos_y),
        (pos_x + width // 2 - offset, pos_y + height),
        (pos_x - width // 2 - offset, pos_y + height)
    ]


    pygame.draw.polygon(surface, color, points)  # Vẽ hình bình hành


def button(surface, pos_y, text=None, click_sound=None, font=FONTS["medium"]):
    global last_click_time
    width, height = BUTTONS_SIZES
    pos_x = SCREEN_WIDTH // 2
    offset = 20  # Độ lệch để tạo hình bình hành

    # Tạo các điểm cho hình bình hành
    points = [
        (pos_x - width // 2 + offset, pos_y),
        (pos_x + width // 2 + offset, pos_y),
        (pos_x + width // 2 - offset, pos_y + height),
        (pos_x - width // 2 - offset, pos_y + height)
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
        draw_text(surface, text, (pos_x, pos_y + height // 2), COLORS["buttons"]["text"], font=font, pos_mode="center",
                  shadow=True, shadow_color=COLORS["buttons"]["shadow"])

    current_time = time.time()
    if on_button and pygame.mouse.get_pressed()[0]:  # Nếu người dùng nhấn vào button
        if current_time - last_click_time > CLICK_COOLDOWN:  # Check if cooldown period has passed
            last_click_time = current_time  # Update the last click time
            if click_sound is not None:  # Phát âm thanh nếu cần
                click_sound.play()
            return True
    return False
    
def input_box(surface, rect, text, font=FONTS["medium"], color=COLORS["buttons"]["text"], border_color=COLORS["buttons"]["shadow"], border_width=2):  
    # Draw the border
    pygame.draw.rect(surface, border_color, rect, border_width)
    
    # Render the text
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (rect.x + 5, rect.y + (rect.height - text_surface.get_height()) // 2))

def text_input(event, text):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_BACKSPACE:
            text = text[:-1]
        elif event.key == pygame.K_RETURN:
            return text, True
        else:
            text += event.unicode
    return text, False

def draw_input_box(surface, rect, text, font=FONTS["medium"], color=COLORS["black"], border_color=COLORS["buttons"]["shadow"], border_width=2):
    # Draw the border
    pygame.draw.rect(surface, border_color, rect, border_width)
    
    # Render the text
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (rect.x + 5, rect.y + (rect.height - text_surface.get_height()) // 2))
    
def vertical_button(surface, pos_x, pos_y, text=None, click_sound=None, font=FONTS["medium"]):
    width, height = 80, font.get_height() * len(text) *0.8 + 20
    rect = pygame.Rect(pos_x, pos_y, width, height)

    on_button = False
    if rect.collidepoint(pygame.mouse.get_pos()):
        color = COLORS["buttons"]["second"]
        on_button = True
    else:
        color = COLORS["buttons"]["default"]

    pygame.draw.rect(surface, COLORS["buttons"]["shadow"], (rect.x - 6, rect.y - 6, rect.w, rect.h)) # draw the shadow rectangle
    pygame.draw.rect(surface, color, rect) # draw the rectangle
    # draw the text
    if text is not None:
         draw_vertical_text(surface, text, (pos_x + width // 3, pos_y), COLORS["buttons"]["text"], font=font, shadow=True, shadow_color=COLORS["buttons"]["shadow"])

    if on_button and pygame.mouse.get_pressed()[0]: # if the user press on the button
        if click_sound is not None: # play the sound if needed
            click_sound.play()
        return True
    
def draw_vertical_text(surface, text, pos, color, font=FONTS["medium"], shadow=True, shadow_color=(0,0,0), shadow_offset=2):
    x, y = pos
    line_height = font.get_height() * 0.8
    for letter in text:
        draw_text(surface, letter, (x, y), color, font, pos_mode="top_left", shadow=shadow, shadow_color=shadow_color, shadow_offset=shadow_offset)
        y += line_height  # Move down for the next letter
   
def rect_button(surface, pos_y, text=None, click_sound=None):
    rect = pygame.Rect((SCREEN_WIDTH//2 - BUTTONS_SIZES[0]//2 - 50, pos_y), (BUTTONS_SIZES[0] + 100, BUTTONS_SIZES[1]))

    on_button = False
    if rect.collidepoint(pygame.mouse.get_pos()):
        color = COLORS["red"]
        on_button = True
    else:
        color = COLORS["light_red"]

    pygame.draw.rect(surface, COLORS["buttons"]["shadow"], (rect.x - 6, rect.y - 6, rect.w, rect.h)) # draw the shadow rectangle
    pygame.draw.rect(surface, color, rect) # draw the rectangle
    # draw the text
    if text is not None:
        draw_text(surface, text, rect.center, COLORS["yellow"], pos_mode="center",
                    shadow=True, shadow_color=COLORS["black"])

    if on_button and pygame.mouse.get_pressed()[0]: # if the user press on the button
        if click_sound is not None: # play the sound if needed
            click_sound.play()
        return True

def draw_gradient_frame(surface, x, y, width, height, thickness, color_start, color_end):
        for i in range(thickness):
            color = (
                color_start[0] + (color_end[0] - color_start[0]) * i // thickness,
                color_start[1] + (color_end[1] - color_start[1]) * i // thickness,
                color_start[2] + (color_end[2] - color_start[2]) * i // thickness,
            )
            pygame.draw.rect(surface, color, (x - width // 2 - i, y - height // 2 - i, width + 2 * i, height + 2 * i), 1)
            
def linkWordpress (surface, pic, pos_x, pos_y):
    global last_click_time
    image.draw(surface, pic, (pos_x, pos_y), pos_mode="center")
    rect = pygame.Rect((pos_x - pic.get_width() // 2, pos_y - pic.get_height() // 2), (pic.get_width(), pic.get_height()))
    
    current_time = time.time()
    if rect.collidepoint(pygame.mouse.get_pos()):
        pic.set_alpha(200)  # Make the image lighter
        if pygame.mouse.get_pressed()[0]:
            if current_time - last_click_time > CLICK_COOLDOWN:
                last_click_time = current_time
                webbrowser.open("https://bmeelearning.wordpress.com/2024/12/21/20241-et2031e-152560-group-19-capture-objects-for-hand-tracking-interraction-2/")
                return True
    else:
        pic.set_alpha(255)  # Reset to original color

    return False

def Settin (surface, pic, pos_x, pos_y):
    image.draw(surface, pic, (pos_x, pos_y), pos_mode="center")
    rect = pygame.Rect((pos_x - pic.get_width() // 2, pos_y - pic.get_height() // 2), (pic.get_width(), pic.get_height()))
    if rect.collidepoint(pygame.mouse.get_pos()):
        pic.set_alpha(200)
        if pygame.mouse.get_pressed()[0]:
            return True
    else:
        pic.set_alpha(255)
    return False

def music_button(surface, pos_y, text, music_file, click_sound=None, font=FONTS["medium"]):
    global last_click_time
    width, height = (340,70)
    pos_x = SCREEN_WIDTH // 1.25
    corner_radius = 20  # Radius for rounded corners

    rect = pygame.Rect(pos_x - width // 2, pos_y, width, height)

    on_button = False
    if rect.collidepoint(pygame.mouse.get_pos()):
        color = COLORS["blue"]
        on_button = True
    else:
        color = COLORS["pink"]

    pygame.draw.rect(surface, color, rect, border_radius=corner_radius)  # Draw rounded rectangle

    # Draw text
    if text is not None:
        draw_text(surface, text, rect.center, COLORS["quote"], font=FONTS["supersmall"], pos_mode="center",
                  shadow=False)

    current_time = time.time()
    if on_button and pygame.mouse.get_pressed()[0]:  # If the user clicks the button
        if current_time - last_click_time > CLICK_COOLDOWN:  # Check if cooldown period has passed
            last_click_time = current_time  # Update the last click time
            if click_sound is not None:  # Play click sound if needed
                click_sound.play()
            pygame.mixer.music.load(music_file)
            pygame.mixer.music.play(-1)
            return True
    return False

import pygame
import image
from settings import *
from hand_tracking import HandTracking
from crystalfly import PyroCrystalfly  # Import PyroCrystalfly
import cv2

class Hand:
    def __init__(self):
        self.orig_image = image.load("Assets/skin/huy.png", size=(HAND_SIZE, HAND_SIZE))
        self.image = self.orig_image.copy()
        self.image_smaller = image.load("Assets/skin/huy.png", size=(HAND_SIZE - 50, HAND_SIZE - 50))
        self.rect = pygame.Rect(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, HAND_HITBOX_SIZE[0], HAND_HITBOX_SIZE[1])
        self.left_click = False
        self.hand_tracking = HandTracking()

    def follow_mouse(self): # change the hand pos center at the mouse pos
        self.rect.center = pygame.mouse.get_pos()
        self.hand_tracking.display_hand()

    def draw_hitbox(self, surface):
        pygame.draw.rect(surface, (200, 60, 0), self.rect)

    def draw(self, surface):
        image.draw(surface, self.image, self.rect.center, pos_mode="center")
        if DRAW_HITBOX:
            self.draw_hitbox(surface)

    def on_objects(self, objects): # return a list with all objects that collide with the hand hitbox
        return [object for object in objects if self.rect.colliderect(object.rect)]

    def kill_objects(self, objects, score, sounds, game_instance): # will kill the objects that collide with the hand when the left mouse button is pressed
        if self.left_click: # if left click
            for object in self.on_objects(objects):
                object_score = 0
                if isinstance(object, PyroCrystalfly):
                    object_score = object.kill(objects, game_instance)
                    score += object_score
                else:
                    object_score += object.kill(objects)
                    score += object_score
                sounds["slap"].play()
                if object_score < 0:
                    sounds["dattebayo"].play()
    
        else:
            self.left_click = False
        return score

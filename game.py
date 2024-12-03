import pygame
import time
import random
from settings import *
from background import Background
from hand import Hand
from hand_tracking import HandTracking
from crystalfly import Crystalfly
from octobaby import Octobaby
import cv2
import ui
from leaderboard import Leaderboard

class Game:
    def __init__(self, surface, player):
        self.surface = surface
        self.background = Background()
        self.player = player

        # Load camera
        self.cap = cv2.VideoCapture(0)

        self.sounds = {}
        self.sounds["slap"] = pygame.mixer.Sound(f"Assets/Sounds/slap.wav")
        self.sounds["slap"].set_volume(SOUNDS_VOLUME)
        self.sounds["dattebayo"] = pygame.mixer.Sound(f"Assets/Sounds/dattebayo.wav")
        self.sounds["dattebayo"].set_volume(SOUNDS_VOLUME)
        self.sounds["getout"] = pygame.mixer.Sound(f"Assets/Sounds/getout.wav")
    
    def reset(self): # reset all the needed variables
        self.hand_tracking = HandTracking()
        self.hand = Hand()
        self.objects = []
        self.objects_spawn_timer = 0
        self.score = 0
        self.game_start_time = time.time()


    def spawn_objects(self):
        t = time.time()
        if t > self.objects_spawn_timer:
            self.objects_spawn_timer = t + CRYSTALFLYS_SPAWN_TIME

            #increase the probability that the object will be a over time
            nb = (GAME_DURATION-self.time_left)/GAME_DURATION * 100  / 2  # increase from 0 to 50 during all  the game (linear)
            if random.randint(0, 100) < nb:
                self.objects.append(Octobaby())
            else:
                self.objects.append(Crystalfly())

            # spawn a other after the half of the game
            if self.time_left < GAME_DURATION/2:
                self.objects.append(Crystalfly())

    def load_camera(self):
        _, self.frame = self.cap.read()


    def set_hand_position(self):
        self.frame = self.hand_tracking.scan_hands(self.frame)
        (x, y) = self.hand_tracking.get_hand_center()
        self.hand.rect.center = (x, y)

    def draw(self):
        self.background.draw(self.surface)
        for object in self.objects:
            object.draw(self.surface)
        self.hand.draw(self.surface)
        ui.draw_text(self.surface, f"Score : {self.score}", (5, 5), COLORS["score"], font=FONTS["medium"],
                    shadow=True, shadow_color=(255,255,255))
        timer_text_color = (160, 40, 0) if self.time_left < 5 else COLORS["timer"] # change the text color if less than 5 s left
        ui.draw_text(self.surface, f"Time left : {self.time_left}", (SCREEN_WIDTH//3, 5),  timer_text_color, font=FONTS["medium"],
                    shadow=True, shadow_color=(255,255,255))


    def game_time_update(self):
        self.time_left = max(round(GAME_DURATION - (time.time() - self.game_start_time), 1), 0)


    def update(self):
        self.load_camera()
        self.set_hand_position()
        self.game_time_update()
        self.draw()

        if self.time_left > 0:
            self.spawn_objects()
            (x, y) = self.hand_tracking.get_hand_center()
            self.hand.rect.center = (x, y)
            self.hand.left_click = self.hand_tracking.hand_closed
            print("Hand closed", self.hand.left_click)
            if self.hand.left_click:
                self.hand.image = self.hand.image_smaller.copy()
            else:
                self.hand.image = self.hand.orig_image.copy()
            self.score = self.hand.kill_objects(self.objects, self.score, self.sounds)
            for object in self.objects:
                object.move()

        else: 
            if ui.button(self.surface, 400, "Continue", click_sound=self.sounds["getout"]):
                Leaderboard.WriteLeaderboard("leaderboard.csv", self.player, self.score)
                # Leaderboard.list_leaderboard.sort(subject: leaderboard.score)
                return "leaderboard"

        cv2.imshow("Frame", self.frame)
        cv2.waitKey(1)

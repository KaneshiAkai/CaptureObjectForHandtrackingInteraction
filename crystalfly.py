import pygame
import random
import time
import image
from settings import *

class Crystalfly:
    def __init__(self):
        #size
        random_size_value = random.uniform(CRYSTALFLYS_SIZE_RANDOMIZE[0], CRYSTALFLYS_SIZE_RANDOMIZE[1])
        size = (int(CRYSTALFLYS_SIZES[0] * random_size_value), int(CRYSTALFLYS_SIZES[1] * random_size_value))
        # moving
        moving_direction, start_pos = self.define_spawn_pos(size)
        # sprite
        self.rect = pygame.Rect(start_pos[0], start_pos[1], size[0]//1.4, size[1]//1.4)
        self.images = [image.load("Assets/crystalfly/crystalfly.png", size=size, flip=moving_direction=="right")] #viết thường hết
        self.current_frame = 0
        self.animation_timer = 0


    def define_spawn_pos(self, size): # define the start pos and moving vel of the CRYSTALFLY
        vel = random.uniform(CRYSTALFLYS_MOVE_SPEED["min"], CRYSTALFLYS_MOVE_SPEED["max"])
        moving_direction = random.choice(("left", "right", "up", "down"))
        if moving_direction == "right":
            start_pos = (-size[0], random.randint(size[1], SCREEN_HEIGHT-size[1]))
            self.vel = [vel, 0]
        if moving_direction == "left":
            start_pos = (SCREEN_WIDTH + size[0], random.randint(size[1], SCREEN_HEIGHT-size[1]))        
            self.vel = [-vel, 0]
        if moving_direction == "up":
            start_pos = (random.randint(size[0], SCREEN_WIDTH-size[0]), SCREEN_HEIGHT+size[1])
            self.vel = [0, -vel]
        if moving_direction == "down":
            start_pos = (random.randint(size[0], SCREEN_WIDTH-size[0]), -size[1])
            self.vel = [0, vel]
        return moving_direction, start_pos


    def move(self):
        self.rect.move_ip(self.vel)


    def animate(self): # change the frame of the insect when needed
        t = time.time()
        if t > self.animation_timer:
            self.animation_timer = t + ANIMATION_SPEED
            self.current_frame += 1
            if self.current_frame > len(self.images)-1:
                self.current_frame = 0


    def draw_hitbox(self, surface):
        pygame.draw.rect(surface, (200, 60, 0), self.rect)



    def draw(self, surface):
        self.animate()
        image.draw(surface, self.images[self.current_frame], self.rect.center, pos_mode="center")
        if DRAW_HITBOX:
            self.draw_hitbox(surface)


    def kill(self, crystalflys): # remove the CRYSTALFLY from the list  #viết thường hết
        crystalflys.remove(self)                                      #viết thường hết
        return 1


class PyroCrystalfly(Crystalfly):
    def __init__(self):
        super().__init__()
        self.images = [image.load("Assets/crystalfly/pyro_crystalfly.png", size=self.rect.size, flip=self.vel[0] > 0)]

    def kill(self, crystalflys, game_instance):
        crystalflys.remove(self)
        game_instance.pyro_caught_time = time.time()
        return 1  # Ensure it returns 1 to increment the score

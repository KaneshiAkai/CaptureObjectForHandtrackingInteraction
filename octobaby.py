import pygame
import random
import image
from settings import *
from crystalfly import Crystalfly

class Octobaby(Crystalfly):
    def __init__(self):
        #size
        random_size_value = random.uniform(OCTOBABY_SIZE_RANDOMIZE[0], OCTOBABY_SIZE_RANDOMIZE[1])
        size = (int(OCTOBABY_SIZES[0] * random_size_value), int(OCTOBABY_SIZES[1] * random_size_value))
        # moving
        moving_direction, start_pos = self.define_spawn_pos(size)
        # sprite
        self.rect = pygame.Rect(start_pos[0], start_pos[1], size[0]//1.4, size[1]//1.4)
        self.images = [image.load(f"Assets/octobaby/octobaby.png", size=size, flip=moving_direction=="right")]
        self.current_frame = 0
        self.animation_timer = 0
        

    def kill(self, crystalflys): # remove the  from the list
        crystalflys.remove(self)
        return -OCTOBABY_PENALITY

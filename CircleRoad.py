import numpy as np
import pygame
import sys


class CircleRoad(object):
    def __init__(self, radius, x, y, thickness):
        self.radius = radius
        self.x = x 
        self.y = y
        self.thickness = thickness

        self.topleft_x = self.x - self.radius
        self.topleft_y = self.y - self.radius

    def draw(self,screen): #render
        pygame.draw.arc(screen, 'black', [self.topleft_x, self.topleft_y + self.radius - self.thickness//2, self.radius*2, self.radius*2], 0, np.pi/2, self.thickness)


import numpy as np
import pygame
import sys


class CircleRoad(object):
    def __init__(self, radius, position, thickness):
        self.radius = radius
        self.position = position  # 2D numpy array.
        self.thickness = thickness

        self.topleft_x = self.position[0] - self.radius
        self.topleft_y = self.position[1] - self.radius

    def draw(self, screen): # Rendering using pygame.
        pygame.draw.arc(screen, 'black', [self.topleft_x, self.topleft_y + self.radius - self.thickness//2,
                                          self.radius*2, self.radius*2], 0, np.pi/2, self.thickness)


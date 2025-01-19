'''
This file holds the CircleRoad class.
'''
import numpy as np
import pygame
import sys

'''
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
'''

import numpy as np
import pygame


class CircleRoad:
    def __init__(self, radius, position, thickness):
        self.radius = radius
        self.position = position
        self.thickness = thickness

    def draw(self, screen):
        num_segments = 3000  # Number of segments for smoothness
        angle_step = 2 * np.pi / num_segments

        outer_points = []
        inner_points = []

        for i in range(num_segments + 1):  # +1 to close the shape
            angle = i * angle_step
            outer_points.append((
                self.position[0] + self.radius * np.cos(angle),
                self.position[1] + self.radius * np.sin(angle)
            ))
            inner_points.append((
                self.position[0] + (self.radius - self.thickness) * np.cos(angle),
                self.position[1] + (self.radius - self.thickness) * np.sin(angle)
            ))

        arc_points = outer_points + inner_points[::-1]
        pygame.draw.polygon(screen, (0, 0, 0), arc_points)

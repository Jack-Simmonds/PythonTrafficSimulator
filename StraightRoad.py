import numpy as np
import pygame
import sys

# StraightRoad is defined as a straight line for the car to drive along. However, it is rendered as a rectangle.
# Thus, its width must extend either side of the line dimensions.
class StraightRoad(object):
    def __init__(self,start_x, start_y, end_x, end_y, width):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y

        # Calculate slope 
        self.dx = self.end_x - self.start_x # probably doesn't need to be self.dx, rather just dx. can change later.
        self.dy = self.end_y - self.start_y

        self.angle = np.arctan(self.dy/self.dx) if self.dx != 0 else np.pi/2 if self.dy > 0 else -np.pi/2 

        # Calculate rectangle parameters
        self.rect_width = width

    def draw(self, screen): # Render
        pygame.draw.line(screen, 'black', (self.start_x, self.start_y), (self.end_x, self.end_y), self.rect_width)  # self.start_point, self.end_point, 2)

        # old code:
        # pygame.draw.rect(screen, 'black', (self.start_x, self.start_y, self.width, self.height))
        # self.start_x, self.start_y, self.end_x, self.end_y

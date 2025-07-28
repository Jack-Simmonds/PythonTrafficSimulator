'''
This file holds the CircleRoad class.
'''
import numpy as np
import pygame
import sys

class CircleRoad:
    def __init__(self, radius, centre, thickness):
        self.radius = radius
        self.centre = np.array(centre)
        
        self.thickness = thickness

    def project_to_path(self, position):


        rel_pos = position - self.centre #self.position is the centre of the circle.
        direction = rel_pos / np.linalg.norm(rel_pos) #Normalise
        return self.center + direction * self.radius

    def heading_at(self, position):
        position = np.asarray(position).reshape(-1)
        centre = self.centre.reshape(-1)
        rel = position - self.centre

        tangent = np.array([-rel[1], rel[0]])
        return tangent / np.linalg.norm(tangent) #Normalise

    def draw(self, screen):
        '''
        old (trying out semicircle customisability):
        num_segments = 3000  #Number of segments for smoothness
        angle_step = 2 * np.pi / num_segments # change this for how much the segment is.

        outer_points = []
        inner_points = []

        for i in range(num_segments + 1):  #+1 to close the shape
            angle = i * angle_step
            outer_points.append((
                self.centre[0] + self.radius * np.cos(angle),
                self.centre[1] + self.radius * np.sin(angle)
            ))
            inner_points.append((
                self.centre[0] + (self.radius - self.thickness) * np.cos(angle),
                self.centre[1] + (self.radius - self.thickness) * np.sin(angle)
            ))

        arc_points = outer_points + inner_points[::-1]
        pygame.draw.polygon(screen, (0, 0, 0), arc_points)
        '''
        # Draw outer boundary
        pygame.draw.circle(screen, (0, 0, 0), self.centre.astype(int), int(self.radius))
        # Draw inner boundary (erase inside to create thickness)
        pygame.draw.circle(screen, screen.get_colorkey() or (255, 255, 255), self.centre.astype(int), int(self.radius - self.thickness))
        

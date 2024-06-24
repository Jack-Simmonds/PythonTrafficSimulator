import numpy as np
import pygame
import sys

class Car(object):
    def __init__(self, identifier, x, y, defaultVelocity, path=None):
        self.identifier = identifier
        self.color = (0,0,0) #black. can add an argument if I want to change.
        self.position = np.array([[x], [y]], dtype="float64")
        self.a = np.array([[10], [0]], dtype="float64")
        self.v = np.array([[defaultVelocity], [0]], dtype="float64")
        self.path = path

    def move(self, dt):
        self.v[0] += self.a[0] * dt  # x-direction velocity
        self.v[1] += self.a[1] * dt  # y-direction velocity
        self.position[0] += self.v[0] * dt  # x-position
        self.position[1] += self.v[1] * dt  # y-position

    def draw(self, screen):
        pygame.draw.circle(screen, 'red', (int(self.position[0]), int(self.position[1])), 25) #last number is radius


import numpy as np
import pygame
import sys


# Define Model Parameters:

# Desired Velocity
v0 = np.float32(30) #ms-1
# Minimum Spacing
s0 = np.float32(1)
# Desired Time Headway
T = np.float32(1)
# Max Acceleration
a = np.float32(1)
# Comfortable Breaking Deceleration (positive number)
b = np.float32(1)
# Exponent, usually set to 4.
exponent = 4
# Length of car, set to 1.
length = 1

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

    def get_attributes(self):
        return [self.position, self.v, self.a]

    def calculate_acceleration(self, v_alpha, v_alpha_previous, s_alpha):
        dvdt = a(1 - (v_alpha / v0) ** 4 - ((s0 + v_alpha * T + (v_alpha * (v_alpha - v_alpha_previous)) / (
                    2 * np.sqrt(a * b)) / s_alpha) ** 2))

        return dvdt

    def draw(self, screen):
        pygame.draw.circle(screen, 'red', (int(self.position[0]), int(self.position[1])), 16) #last number is radius


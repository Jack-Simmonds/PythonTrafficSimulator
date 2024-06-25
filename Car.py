import numpy as np
import pygame
import sys


# Define Model Parameters:

# Desired Velocity
v0 = float(30) #ms-1
# Minimum Spacing
s0 = float(2)
# Desired Time Headway
T = float(1.5)
# Max Acceleration
a = float(10)
# Comfortable Breaking Deceleration (positive number)
b = float(10)
# Exponent, usually set to 4.
exponent = 4
# Length of car, set to 5.
length = 5

class Car(object):
    def __init__(self, identifier, x, y, defaultVelocity, path=None):
        self.identifier = identifier
        self.color = (0, 0, 0) #black. can add an argument if I want to change.
        self.position = np.array([[x], [y]], dtype="float64")
        self.a = np.array([[0], [0]], dtype="float64")
        self.v = np.array([[defaultVelocity], [0]], dtype="float64")
        self.path = path

        # Plotting elements:
        self.accelerations = []

    def move(self, dt):
        self.v[0] += self.a[0] * dt  # x-direction velocity
        self.v[1] += self.a[1] * dt  # y-direction velocity
        self.position[0] += self.v[0] * dt  # x-position
        self.position[1] += self.v[1] * dt  # y-position

    def get_attributes(self):
        return [self.position, self.v, self.a]

    def calculate_acceleration(self, v_alpha_front, x_front):
        """
        Function Calculate_acceleration ...

        Parameters:
                v_alpha_front (float): The velocity of the car in front of this car.
                x_front: The x-coordinates of the car in front of this car.

        """
        s_alpha = x_front - self.position[0] - length  # X-position of car in front, minus this car's position,
        # minus the length of the car in front.

        v_alpha = self.v[0]
        # Calculate alpha acceleration.

        s_star = s0 + v_alpha * T + (v_alpha * (v_alpha - v_alpha_front)) / (2 * np.sqrt(a * b))
        a_alpha = a * (1 - (v_alpha / v0) ** exponent - (s_star / s_alpha) ** 2)

        self.a[0] = a_alpha
    def calculate_linear_path_distance(self, car_position, car_front_position):
        return np.linalg.norm(np.array(car_position) - np.array(car_front_position))

    def calculate_circular_path_distance(self):
        

    def calculate_acceleration2(self, v_front, position_front): #Creating a new function for 'distance' rather than x-direction.
        """

        New parameters:
        v_front, position_front.

        Function Calculate_acceleration ...

        Parameters:
                v_alpha_front (float): The velocity of the car in front of this car.
                x_front: The x-coordinates of the car in front of this car.

        Assumptions:
            Car shape is roughly circular. (This simplifies the alpha distance equation)
        """
        '''
        s_alpha = np.sqrt(
            (position_front[0] - self.position[0]) ** 2 + (position_front[1] - self.position[1]) ** 2) - length

        # Calculate v_alpha = ||v||
        v_alpha = np.sqrt((self.v[0])**2 + (self.v[1])**2)

        # Calculate v_alpha_front = ||v_alpha-1||
        v_alpha_front = np.sqrt((v_front[0])**2 + (v_front[1])**2)
        '''

        s_alpha =

        # Calculate alpha acceleration, where a_alpha = a_t, (tangential acceleration).
        s_star = s0 + v_alpha * T + (v_alpha * (v_alpha - v_alpha_front)) / (2 * np.sqrt(a * b))
        a_alpha = a * (1 - (v_alpha / v0) ** exponent - (s_star / s_alpha) ** 2)

        self.a[0] = a_alpha

    def draw(self, screen):
        pygame.draw.circle(screen, 'red', (int(self.position[0]), int(self.position[1])), 5) # last number is radius


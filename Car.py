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

    def calculate_acceleration(self, v_alpha_front, x_front):  # This is the 1D version, currently not being used.
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
        return np.linalg.norm(np.array(car_position) - np.array(car_front_position)) #maybe I can remove np.array()?

    def calculate_circular_path_distance(self, car_position, car_front_position, circle_centre, radius):
        # This find the arc length (S = r*theta) between two cars, for the path distance between two cars in a circular
        # path.
        # calculate angles for both cars, normalize to be in a good range (0--> 2pi?), calculate difference in angle,
        # make sure the angle doesn't have errors for negative angle etc, find arc length S = r*theta, return.

        """
        Parameters:
            car_position:
            car_front_position:
            circle_centre:
            radius:

        Returns:
            distance (float): The distance between the two cars.
        Preconditions:
            Assume that both cars are positioned on the circle.
        """

        behind_car_angle = np.arctan2(car_position[1] - circle_centre[1], car_position[0] - circle_centre[0])
        front_car_angle = np.arctan2(car_front_position[1] - circle_centre[1], car_front_position[0] - circle_centre[0])
        '''
        if behind_car_angle < 0:
            behind_car_angle = 
        '''

        angle = front_car_angle - behind_car_angle
        distance = radius * angle

        print(f'Front car angle = {front_car_angle}, behind_car_angle = {behind_car_angle}, delta angle = {angle}, '
              f'distance = {distance}.')
        return distance

    def calculate_acceleration2(self, v_front, position_front): #Creating a new function for 'distance' rather than x-direction.
        """
        Function Calculate_acceleration ...

        Parameters:
            v_front (2D numpy float array): The velocity of the car in front of this car.
            position_front (2D numpy float array): The x-coordinates of the car in front of this car.
        Returns:
            a_alpha (float): The tangential acceleration of the vehicle.

        Assumptions:
            Car shape is roughly circular. (This simplifies the alpha distance equation)
            Given this, we can assume that for a circular path, the arc distance minus the length of the car is equal to
            s_alpha. This is not completely accurate, but is a fair assumption given the change in distance is minimal.
            We assume that the velocity of the car in tangential to the path, which should hold for constant paths.
                Note: Consider this for when the car in front has a different path to the car behind?
        """

        if self.path.__class__.__name == "StraightRoad":
            s_alpha = self.calculate_linear_path_distance(self.position, position_front) - length
        elif self.path.__class__.__name == "StraightRoad":
            s_alpha = self.calculate_circular_path_distance(self.position, position_front) - length

        # Calculate v_alpha = ||v|| = v_tangential
        v_alpha = np.sqrt((self.v[0])**2 + (self.v[1])**2)

        # Calculate v_alpha_front = ||v_alpha-1|| = v_alpha-1_tangential
        v_alpha_front = np.sqrt((v_front[0])**2 + (v_front[1])**2)

        # Calculate alpha acceleration, where a_alpha = a_t, (tangential acceleration).
        s_star = s0 + v_alpha * T + (v_alpha * (v_alpha - v_alpha_front)) / (2 * np.sqrt(a * b))
        a_alpha = a * (1 - (v_alpha / v0) ** exponent - (s_star / s_alpha) ** 2)

        return a_alpha #where a_alpha is now the tangential acceleration.

    def draw(self, screen):
        pygame.draw.circle(screen, 'red', (int(self.position[0]), int(self.position[1])), 5) # last number is radius


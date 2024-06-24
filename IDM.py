import numpy as np
import pygame
import sys
import scipy
from Car import Car

WIDTH, HEIGHT = 800, 600

# Define Model Parameters:

# Desired Velocity
v0 = np.float32(30) #ms-1
# Minimum Spacing
s0 = np.float32(1)
# Desired Time Headway
T = np.float32(1)
# Max Accleration
a = np.float32(1)
# Comfortable Breaking Deceleration (positive number)
b = np.float32(1)
# Exponent, usually set to 4.
exponent = 4
# Length of car, set to 1.
length = 1

# Creating the system of cars:
# Car 1: The first car, of which I will apply the ODE model to.
Car1 = Car(1, 125, 300, 0)
# Car 2: The car in front, set to have a steady velocity of 30.
Car2 = Car(2, 125, 300, 30)


def find_s_alpha(x_alpha_previous, x_alpha):
    s_alpha = x_alpha_previous - x_alpha - length
    return s_alpha

def acceleration(v_alpha, v_alpha_previous, s_alpha):
    dvdt = a(1-(v_alpha/v0)**4 - ((s0 + v_alpha*T + (v_alpha * (v_alpha - v_alpha_previous))/(2*np.sqrt(a*b))/s_alpha)**2))

    return dvdt


# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Simple Traffic System')
clock = pygame.time.Clock()

# Tick system:
while True:
    dt = clock.tick(60) / 1000.0
    screen.fill('WHITE')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Sequence of movement, for 2 cars:
    Car1.move()
    attributes = []
    '''
    attributes = Car1.get_attributes()

    Car2.acceleration()
    '''

    # Update the display
    pygame.display.flip()
    # Control the frame rate --> 60fps.
    pygame.time.Clock().tick(60)






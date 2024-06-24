import numpy as np
import pygame
import sys
import scipy
from Car import Car

WIDTH, HEIGHT = 800, 600

# Creating the system of cars:
# Car 1: The first car, of which I will apply the ODE model to.
Car1 = Car(1, 25, 300, 0)
# Car 2: The car in front, set to have a steady velocity of 30.
Car2 = Car(2, 200, 300, 4)

length = 1

def find_s_alpha(x_alpha_previous, x_alpha):
    s_alpha = x_alpha_previous - x_alpha - length
    return s_alpha


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

    # Sequence of movement for 2 cars:
    Car2.move(dt)
    attributes = Car2.get_attributes()
    position = attributes[0]
    velocity = attributes[1]
    acceleration = attributes[2]
    #print(f'Attributes are: position {position}, velocity {velocity}, and acceleration {acceleration}')

    v_alpha_front = velocity[0]  # Assign v_(alpha - 1) for the behind car.

    Car1.calculate_acceleration(v_alpha_front, position[0])
    Car1.move(dt)
    print(Car1.a[0], Car1.v[0], Car1.position[0])

    Car1.draw(screen)
    Car2.draw(screen)

    # Update the display
    pygame.display.flip()
    # Control the frame rate --> 60fps.
    pygame.time.Clock().tick(60)






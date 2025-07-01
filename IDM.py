'''
This file demonstrates a simple IDM of same format to 'IDMDemo1.py', without the plotting element. 
'''

import numpy as np
import pygame
import sys
import matplotlib.pyplot as plt
import scipy
from Classes.Car import Car
from Classes.StraightRoad import StraightRoad

WIDTH, HEIGHT = 800, 600

# Creating the system of roads:
# Road 1:
Road1 = StraightRoad(50, 300, 350, 300, 15)
roads = [Road1]

# Creating the system of cars:
# Car 1: The first car, of which I will apply the IDM model to.
Car1 = Car(1, 25, 300, 0, path=Road1)
# Car 2: The car in front, set to have a steady velocity of 4.
Car2 = Car(2, 200, 300, 4, path=Road1)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Simple Traffic System')
clock = pygame.time.Clock()

# Tick system:
while True:
    dt = clock.tick(60) / 1000.0

    screen.fill('WHITE')

    for road in roads:
        road.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Sequence of movement for 2 cars:
    Car2.move(dt)
    attributes = Car2.get_attributes() # Finding attributes of the car in front.
    position = attributes[0]
    velocity = attributes[1]
    acceleration = attributes[2]

    # v_alpha_front = velocity[0]  # Assign v_(alpha - 1) for the behind car, x-direction.
    Car1.calculate_acceleration2(velocity, position) #Can be put inside move loop along the line.
    Car1.move(dt)

    Car1.draw(screen)
    Car2.draw(screen)

    # Update the display
    pygame.display.flip()
    # Control the frame rate --> 60fps.
    pygame.time.Clock().tick(60)







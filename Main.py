'''
This is the main testing file.
'''

import numpy as np
import pygame
import sys

#Classes:
from Car import Car
from StraightRoad import StraightRoad
from CircleRoad import CircleRoad

#constants
WIDTH, HEIGHT = 1280, 720

pygame.init()

#startx, starty, endx, endy, width
Road1 = StraightRoad(50, 300, 350, 300, 15)
#radius, centerofcircle_x, centerofcircle_y, thickness.
Road2 = CircleRoad(50, (350,300), 15)
roads = [Road1, Road2]


desired_velocity = 30 #ms-1
Car1 = Car(1, 25, 300, desired_velocity, path=Road1)
Car2 = Car(2, 125, 300, desired_velocity, path=Road1)
cars = [Car1, Car2]


# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Simple Traffic System')
clock = pygame.time.Clock()

while True:
    dt = clock.tick(60) / 1000.0 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Update ball positions and check for collisions
    for car in cars:
        car.move(dt)

    #Draw background. Note that this is updated every frame so the balls dont trail.
    screen.fill('WHITE')
    #Drawing the roads and cars:
    for road in roads:
        road.draw(screen)
    for car in cars:
        car.draw(screen)

    # Update the display
    pygame.display.flip()
    # Control the frame rate --> 60fps.
    pygame.time.Clock().tick(60)
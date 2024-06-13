import numpy as np
import pygame
import sys

#Classes:
from Car import Car
from StraightRoad import StraightRoad
from CircleRoad import CircleRoad

#constants
WIDTH, HEIGHT = 800, 600
VELOCITY = 20 #ms-1
pygame.init()

#startx, starty, endx, endy, width
Road1 = StraightRoad(50,300,350,300,15)
#radius, centerofcircle_x, centerofcircle_y, thickness.
Road2 = CircleRoad(50,350,300,15) 
roads = [Road1, Road2]
#RoadMapping is a dictionary that corresponds the car to its current road. can replace with in-class scripts later. (part of checking?)
#RoadMapping = {Car1:Road1, Car2:Road1} #bad memory allocation. replace with text. do later.


Car1 = Car(1, 25, 300, VELOCITY, path=Road1)
Car2 = Car(2, 125, 300, VELOCITY, path=Road1)
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
        for road in roads:#this won't work.
            car.move(dt, road) 

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
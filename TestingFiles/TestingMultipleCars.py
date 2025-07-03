'''
Testing multiple cars on a straight road.
'''

import numpy as np
import pygame
import sys
import matplotlib.pyplot as plt
import scipy
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Classes')))
from Car import Car
from StraightRoad import StraightRoad

WIDTH, HEIGHT = 800, 600
Road1 = StraightRoad(50, 300, 350, 300, 15)
roads = [Road1]

pygame.init()

# Car 1:
Car1 = Car(ID=1, x=25, y=300, defaultVelocity=0, path=Road1)
# Car 2: 
Car2 = Car(ID=2, x=40, y=300, defaultVelocity=0, path=Road1)
# Car 3: 
Car3 = Car(ID=3, x=55, y=300, defaultVelocity=0, path=Road1)
# Car 4: The car in front, set to have a steady velocity of 50.
Car4 = Car(ID=4, x=70, y=300, defaultVelocity=20, path=Road1)
idm_cars = [Car3, Car2, Car1]

#ABOVE: Car4 needs to have a sudden deceleration created.

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Simple Traffic System')
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 10)

while True:
    dt = clock.tick(60) / 1000.0
    screen.fill('WHITE')

    for road in roads:
        road.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Sequence of movement for multiple cars. First start with getting attributes for Car4.
    position,velocity,acceleration = Car4.get_attributes()
    Car4.move(dt)

    for car in idm_cars: #starting with car #3.
        car.calculate_acceleration2(velocity, position)    
        car.move(dt)
        position,velocity,acceleration = car.get_attributes()

    # v_alpha_front = velocity[0]  # Assign v_(alpha - 1) for the behind car, x-direction.
    Car4.draw(screen)
    for car in idm_cars:
        car.draw(screen)
    
    fps = clock.get_fps()
    pygame.time.Clock().tick(60)
    fps_text = font.render(f"FPS: {fps:.2f}", True, pygame.Color('black'))
    screen.blit(fps_text, (WIDTH - fps_text.get_width() - 10, 10))

    # Update the display
    pygame.display.flip()

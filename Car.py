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

        '''
        Essentially, the velocity and position directions should always remain in the direction of the path.
        '''

        '''
        if path.__class__.__name__ == 'StraightRoad': #works. problem = car's velocity might not go along path. should change.
        #potential problem is if the car reaches the end of the road, the velocity still accelerates?
            #check if extension is beyond end of road.
            self.vx = self.v * np.cos(path.angle) #quite taxing calculations. find better way later.
            self.vy = self.v * np.sin(path.angle) #--> potentially one-off the second part of the calculation in a different function.
            x_change = self.vx*dt
            y_change = self.vy*dt
            if self.x + x_change < path.end_x or self.y + y_change < path.end_y: #within bounds. might need changing for difference slopes.
                self.x += x_change
                self.y += y_change
            else:
                #print('self.x = {}, self.y = {}, stopping at end of road.'.format(self.x,self.y))
                #distance_remaining = etc, then can apply to next path. maybe return?
                self.x = path.end_x
                self.y = path.end_y1

        elif path.__class__.__name__ == 'CircleRoad':
            a = 5
        '''
    def check_path(self):
        # allow error tolerance
        return

    def check(self): #finish this later. need to work on path-tracking first.
        relativeDistanceCarInFront = 999
        relativeVelocityCarInFront = 999
        relativeAccelerationCarInFront = 999
        #check for cars in front:
        minCheck = 5 #let follow distance = 5
        '''
        for i in range(len(cars)): #PROBLEM: INCLUDES OWN CAR.
            if cars[i].identifier != self.identifier:
                if cars[i].x - self.x > 0:

                #minCheck = min(minCheck, abs(car.x - self.x))
        '''
        #return (minCheck)/5
        #float ranging from 1--> 0. 1 = free to move. 0 = harsh break. 0.5 = start breaking, etc. need to research this. 

    def draw(self, screen):
        pygame.draw.circle(screen, 'red', (int(self.position[0]), int(self.position[1])), 25) #last number is radius


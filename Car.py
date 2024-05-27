import numpy as np
import pygame
import sys

class Car(object):
    def __init__(self, identifier, x, y, defaultVelocity):
        self.identifier = identifier
        self.x = x
        self.y = y
        self.color = (0,0,0) #black. can add an argument if I want to change.
        self.v = defaultVelocity #default linear velocity
        self.vx = 0 #velocity in x
        self.vy = 0 #velocity in y
        self.a = 10 #default linear acceleration
        self.ax = 0 #acceleration in x
        self.ay = 0 #acceleration in y

    def move(self, dt, path):
        #self.ay += self.ay * dt #not sure about these acceleration equations. are they right?
        #self.ax = self.ax * dt #Car.check(self) #check collisions
        self.vx += self.ax * dt
        self.vy += self.ay * dt

        #assumptions: Car is initially on the path. Given a velocity, now calculate changes in x and y.
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
                self.y = path.end_y

        elif path.__class__.__name__ == 'CircleRoad':
            a = 5
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
        pygame.draw.circle(screen, 'red', (int(self.x), int(self.y)), 25) #last number is radius


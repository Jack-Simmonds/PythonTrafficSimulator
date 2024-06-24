import numpy as np
import pygame
import sys
import scipy

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

# Creating the first car:


def find_s_alpha(x_alpha_previous, x_alpha):
    s_alpha = x_alpha_previous - x_alpha - length
    return s_alpha

def acceleration(v_alpha, v_alpha_previous, s_alpha):
    dvdt = a(1-(v_alpha/v0)**4 - ((s0 + v_alpha*T + (v_alpha * (v_alpha - v_alpha_previous))/(2*np.sqrt(a*b))/s_alpha)**2))

    return dvdt

# Tick system:
while True:
    dt = clock.tick(60) / 1000.0
    screen.fill('WHITE')






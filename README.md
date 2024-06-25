# PythonTrafficSimulator [in progress]
Python Traffic Simulator implements the Intelligent Driver Model to simulate basic 2-dimensional traffic from a top-down perspective. 
When using this repository, use the file "IDM.py" to access the simulation rather than "main.py" (temporary)

## Intelligent Driver Model:
The intelligent driver model uses two ordinary differential equations to define the movement of each car in the system.

In my project, these ODES are solved using the 3rd-order Range-Kutta method.

(Currently solved using a 1st-order euler method with h = dt $\approx$ 1/60)

Ordinary differential equations that characterise the movement of the vehicles when considered only in one direction:

$\frac{dx_\alpha}{dt} = v_\alpha$

$a_\alpha = \frac{dv_\alpha}{dt} = a\left(1 - \left(\frac{v_\alpha}{v_0}\right)^\delta - \frac{s^*(v_\alpha, \Delta v_\alpha)}{s_\alpha}^2\right)$

where $s^*(v_\alpha, \Delta v_\alpha) = s_0 + v_\alpha T + \frac{v_\alpha \Delta v_\alpha}{2 \sqrt{ab}}$

Parameters:

$v_0$: Desired velocity; essentially the speed limit.

$s_0$: Minimum spacing of two vehicles. The distance between the two cars must exceed $s_0$ for the behind car to move.

$T$: The desired time headway. This is the minimum possible time to the car in front.

$a$: Acceleration, the maximum acceleration of the car.  

$b$: Comfortable braking deceleration. 

$\delta$: The exponent value, here set to 4.

## Model Behavior:

# PythonTrafficSimulator [in progress]
Python Traffic Simulator implements the Intelligent Driver Model to simulate basic 2-dimensional traffic from a top-down perspective. 
When using this repository, use the file "IDMDemo1.py" for a short demonstration of the simulation.

## Intelligent Driver Model:
The intelligent driver model uses two ordinary differential equations to define the movement of each car in the system.

In my project, these ODES are solved using the 3rd-order Range-Kutta method.

(Currently solved using a 1st-order euler method with h = dt $\approx$ 1/60)

Ordinary differential equations that characterise the movement of a vehicle $\alpha$ when considered only in one direction:

$\frac{dx_\alpha}{dt} = v_\alpha$

$a_\alpha = \frac{dv_\alpha}{dt} = a\left(1 - \left(\frac{v_\alpha}{v_0}\right)^\delta - (\frac{s^*(v_\alpha, \Delta v_\alpha)}{s_\alpha})^2\right)$

where $s^*(v_\alpha, \Delta v_\alpha) = s_0 + v_\alpha T + \frac{v_\alpha \Delta v_\alpha}{2 \sqrt{ab}}$

Parameters:

$v_0$: Desired velocity; essentially the speed limit.

$s_0$: Minimum spacing of two vehicles. The distance between the two cars must exceed $s_0$ for the behind car to move.

$T$: The desired time headway. This is the minimum possible time to the car in front.

$a$: Acceleration, the maximum acceleration of the car.  

$b$: Comfortable braking deceleration. 

$\delta$: The exponent value, here set to 4.

## Model Behaviour:

### Free road:

On a free road, the model reaches $v_0$ at steady state (asymptotically). This is because the distance between cars ($s_\alpha$) is large, so essentially:
$a_\alpha = \frac{dv_\alpha}{dt} = a\left(1 - \left(\frac{v_\alpha}{v_0}\right)^\delta \right)$

As $v_\alpha$ $\rightarrow$ $v_0$, $a_\alpha$ $\rightarrow$ $0$.

### High approaching rates:

At high approaching rates, there is a large difference in velocity. The initial terms, $\left(1 - \left(\frac{v_\alpha}{v_0}\right)^\delta \right)$, lose relevance, and instead the $s^*(v_\alpha, \Delta v_\alpha) = s_0 + v_\alpha T + \frac{v_\alpha \Delta v_\alpha}{2 \sqrt{ab}}$ term dominates. (Due to the squared difference in velocity). We observe that the driving behaviour does not want to break much harder than the comfortable breaking deceleration $b$, but deceleration strongly relies on the difference in velocity to minimise the chance of collision. 

### Small differences in distances between cars:

Assuming that $v_\alpha \approx v_0$, we observe that the s* dominates. The acceleration becomes $-a \frac{(s_0 + v_\alpha T)^2}{s^2_\alpha}$. This is considered to be a 'simple repulsive force', that expands the small distance to an equilibrium net distance reliant on the minimum gap between cars.

## End goal of model:
The end goal of this model is to simulate large numbers of vehicles in different traffic systems by using path elements such as circles and straight roads. With this, simulation can optimise routes or convey traffic concepts such as [Traffic Waves](https://en.wikipedia.org/wiki/Traffic_wave).

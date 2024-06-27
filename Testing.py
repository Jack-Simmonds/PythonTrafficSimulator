import numpy as np
from Car import Car

def t_circular_path_distance():

    Car1 = Car(1, 25, 300, 0)
    Car2 = Car(1, 25, 350, 2)
    position = Car1.get_attributes()[0]
    position2 = Car2.get_attributes()[0]
    #print(position)
    #Car1.calculate_circular_path_distance(car_position,car_front_position,circle_centre,radius)
    Car1.calculate_circular_path_distance(position, position2, np.array([[0], [0]]), 10)

    return

t_circular_path_distance()
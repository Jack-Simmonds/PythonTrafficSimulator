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

def t_calculate_linear_path_distance():
    Car1 = Car(1, 25, 300, 0)
    position1 = np.array([[10],[0]])
    position2 = np.array([[15], [20]])
    distance = Car1.calculate_linear_path_distance(position1, position2)
    exact = np.sqrt(425)
    assert(distance == exact)

t_circular_path_distance()
#t_calculate_linear_path_distance()
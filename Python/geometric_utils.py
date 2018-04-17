import numpy as np


def distance_from_point_to_rectangle(point, rectangle):
    dist = 0

    if point[0] > rectangle[2]:
        dist += np.power(point[0] - rectangle[2], 2)
    elif point[0] < rectangle[0]:
        dist += np.power(point[0] - rectangle[0], 2)

    if point[1] > rectangle[3]:
        dist += np.power(point[1] - rectangle[3], 2)
    elif point[1] < rectangle[1]:
        dist += np.power(point[1] - rectangle[1], 2)

    return np.sqrt(dist)


def circle_field(radius):
    return np.pi * np.power(radius, 2)


def are_things_in_collision(thing1, thing2):
    return thing1.x_min < thing2.x_max and thing1.x_max > thing2.x_min and \
           thing1.y_min < thing2.y_max and thing1.x_max > thing2.x_min

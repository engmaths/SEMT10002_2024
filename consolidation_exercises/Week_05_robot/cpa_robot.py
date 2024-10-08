from matplotlib import pyplot as plt
from math import cos, sin
from numpy import sinc, pi

_x = 0.
_y = 0.
_theta = 0.

history = [(_x,_y,_theta)]

def reset_robot(x_init = 0.0, y_init=0.0, theta_init = 0.0):
    global _x, _y, _theta
    _x = x_init
    _y = y_init
    _theta = theta_init
    history.clear()
    history.append((_x,_y,_theta))

WHEEL_SEP = 5.0

def drive(left_turn, right_turn):
    global _x, _y, _theta
    num_steps = 50
    delta_left = left_turn/num_steps
    delta_right = right_turn/num_steps
    delta_angle = (delta_left - delta_right)/WHEEL_SEP
    delta_length = 0.5*(delta_right + delta_left)
    for ii in range(num_steps):
        _x = _x + delta_length*sin(_theta)
        _y = _y + delta_length*cos(_theta)
        _theta = _theta + delta_angle
        history.append((_x,_y,_theta))

def position_x():
    return _x

def position_y():
    return _y

def orientation():
    return _theta

TAPE_CTR_X = 50.
TAPE_CTR_Y = 50.
TAPE_RAD = 40.
TAPE_HALF_WIDTH = 0.5

SENSOR_Y = 3.0
LEFT_SENSOR_X = -1.5
MIDDLE_SENSOR_X = -1.5
RIGHT_SENSOR_X = -1.5

def sensor_left():
    return True

def sensor_middle():
    return True

def sensor_right():
    return True

def plot_path():
    plt.plot([p[0] for p in history],
             [p[1] for p in history])
    plt.axis('equal')
    plt.show()
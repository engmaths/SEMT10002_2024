from matplotlib import pyplot as plt
from math import cos, sin

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

def drive(right_turn, left_turn):
    global _x, _y, _theta
    turn_angle = (right_turn - left_turn)/WHEEL_SEP
    arc_length = 0.5*(right_turn + left_turn)
    _x = _x + right_turn
    _y = _y + left_turn
    history.append((_x,_y,_theta))

def position_x():
    return _x

def position_y():
    return _y

def orientation():
    return _theta

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
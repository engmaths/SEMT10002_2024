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

def _robot_to_global(x_robot,y_robot):
    x_global = _x + x_robot*cos(_theta) + y_robot*sin(_theta)
    y_global = _y - x_robot*sin(_theta) + y_robot*cos(_theta)
    return x_global, y_global

SENSOR_Y = 3.0
LEFT_SENSOR_X = -0.75
MIDDLE_SENSOR_X = 0.0
RIGHT_SENSOR_X = +0.75

def _on_tape(x,y):
    radsq = (x - TAPE_CTR_X)**2 + (y - TAPE_CTR_Y)**2
    result = True
    if radsq > (TAPE_RAD + TAPE_HALF_WIDTH)**2:
        result = False
    if radsq < (TAPE_RAD - TAPE_HALF_WIDTH)**2:
        result = False
    return result

def sensor_left():
    x,y = _robot_to_global(LEFT_SENSOR_X,SENSOR_Y)
    return _on_tape(x,y)

def sensor_middle():
    x,y = _robot_to_global(MIDDLE_SENSOR_X,SENSOR_Y)
    return _on_tape(x,y)

def sensor_right():
    x,y = _robot_to_global(RIGHT_SENSOR_X,SENSOR_Y)
    return _on_tape(x,y)

ROBOT_BOX = [(2.5,5),(-2.5,5),(-2.5,-2.5),(2.5,-2.5),(2.5,5)]
def draw_robot():
    box_global = [_robot_to_global(x,y) for (x,y) in ROBOT_BOX]
    plt.plot([p[0] for p in box_global],
             [p[1] for p in box_global],'b-')
    sensors_global = [_robot_to_global(x,SENSOR_Y) for x in [LEFT_SENSOR_X,MIDDLE_SENSOR_X,RIGHT_SENSOR_X]]
    #print(sensors_global)
    plt.plot([p[0] for p in sensors_global],
             [p[1] for p in sensors_global],'r.')

def _plot_tape():
    NUM_TICKS = 720
    angs = [2*pi*ii/NUM_TICKS for ii in range(NUM_TICKS)]
    for ang in angs:
        plt.plot([TAPE_CTR_X + (TAPE_RAD + r)*cos(ang) for r in [-TAPE_HALF_WIDTH,TAPE_HALF_WIDTH]],
                 [TAPE_CTR_Y + (TAPE_RAD + r)*sin(ang) for r in [-TAPE_HALF_WIDTH,TAPE_HALF_WIDTH]],'c')

def plot_path():
    _plot_tape()
    plt.plot([p[0] for p in history],
             [p[1] for p in history],'g-')
    draw_robot()
    plt.axis('equal')
    plt.show()

def _demo_robot():
    NORMAL_DRIVE = 1.0
    SLOW_DRIVE = 0.5
    for _ in range(100):
        drive(1.1*SLOW_DRIVE,SLOW_DRIVE)
        if sensor_middle():
            print('found line')
            break
    for _ in range(50):
        if position_y() >= 75:
            print('at y=75')
            break
        if sensor_middle():
            if sensor_right() and sensor_left():
                print('pivot left')
                drive(-SLOW_DRIVE,SLOW_DRIVE)
            elif sensor_left():
                print('left a bit')
                drive(SLOW_DRIVE,NORMAL_DRIVE)
            elif sensor_right():
                print('right a bit')
                drive(NORMAL_DRIVE,SLOW_DRIVE)
            else:
                print('straight')
                drive(NORMAL_DRIVE,NORMAL_DRIVE)
        else:
            if sensor_right() and sensor_left():
                raise(RuntimeError('Sensor fault - on,off,on'))
            elif sensor_left():
                print('pivot left')
                drive(-SLOW_DRIVE,SLOW_DRIVE)
            elif sensor_right():
                print('pivot right')
                drive(SLOW_DRIVE,-SLOW_DRIVE)
            else:
                print('lost')
                drive(1.1*SLOW_DRIVE,SLOW_DRIVE)
    for _ in range(50):
        TARGET_ANGLE = 0.5*pi
        error = orientation() - TARGET_ANGLE
        print('Angle',orientation(),'error',error)
        K = 0.25
        drive(-K*error,K*error)
    distance = 50 - position_x()
    drive(distance,distance)
    print('Should be at 50,75')
    print(position_x(),position_y())
    plot_path()

if __name__=='__main__':
    _demo_robot()
from matplotlib import pyplot as plt
from matplotlib import animation as animation
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

def _robot_to_global(x_robot,y_robot,robot_state=None):
    if robot_state is None:
        robot_state = (_x,_y,_theta)
    x_global = robot_state[0] + x_robot*cos(robot_state[2]) + y_robot*sin(robot_state[2])
    y_global = robot_state[1] - x_robot*sin(robot_state[2]) + y_robot*cos(robot_state[2])
    return x_global, y_global

SENSOR_Y = 3.5
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

ROBOT_BOX = [(2.0,5.0),(-2.0,5.0),(-2.0,-3.0),(2.0,-3.0),(2.0,5.0)]
def _draw_robot(ax,robot_state = None):
    if robot_state is None:
        robot_state = (_x,_y,_theta)
    box_global = [_robot_to_global(x,y,robot_state) for (x,y) in ROBOT_BOX]
    robot_line = ax.plot([p[0] for p in box_global],
                         [p[1] for p in box_global],'b-')[0]
    sensors_global = [_robot_to_global(x,SENSOR_Y,robot_state) for x in [LEFT_SENSOR_X,MIDDLE_SENSOR_X,RIGHT_SENSOR_X]]
    sensors_line = ax.plot([p[0] for p in sensors_global],
                           [p[1] for p in sensors_global],'r.')[0]
    left_wheel_global = [_robot_to_global(-0.5*WHEEL_SEP,y,robot_state) for y in [-0.5*WHEEL_SEP, 0.5*WHEEL_SEP]]
    left_wheel_line = ax.plot([p[0] for p in left_wheel_global],
                              [p[1] for p in left_wheel_global],'k-')[0]
    right_wheel_global = [_robot_to_global(0.5*WHEEL_SEP,y,robot_state) for y in [-0.5*WHEEL_SEP, 0.5*WHEEL_SEP]]
    right_wheel_line = ax.plot([p[0] for p in right_wheel_global],
                               [p[1] for p in right_wheel_global],'k-')[0]
    return robot_line, sensors_line

def _plot_tape(ax):
    NUM_TICKS = 720
    angs = [2*pi*ii/NUM_TICKS for ii in range(NUM_TICKS)]
    for ang in angs:
        ax.plot([TAPE_CTR_X + (TAPE_RAD + r)*cos(ang) for r in [-TAPE_HALF_WIDTH,TAPE_HALF_WIDTH]],
                 [TAPE_CTR_Y + (TAPE_RAD + r)*sin(ang) for r in [-TAPE_HALF_WIDTH,TAPE_HALF_WIDTH]],'c')

def plot_robot():
    fig,ax = plt.subplots()
    _draw_robot(ax)
    plt.axis('equal')
    plt.show()


def plot_path():
    fig,ax = plt.subplots()
    _plot_tape(ax)
    plt.plot([p[0] for p in history],
             [p[1] for p in history],'k-')
    _draw_robot(ax)
    plt.axis('equal')
    plt.show()

def animate_path():
    fig,ax = plt.subplots()
    _plot_tape(ax)
    ax.axis('equal')
    path_line = ax.plot([],[],'k-')[0]
    robot_line, sensors_line = _draw_robot(ax)
    def update(frame):
        print(frame)
        path_line.set_xdata([p[0] for p in history[:frame]])
        path_line.set_ydata([p[1] for p in history[:frame]])
        box_global = [_robot_to_global(x,y,history[frame]) for (x,y) in ROBOT_BOX]
        robot_line.set_xdata([p[0] for p in box_global])
        robot_line.set_ydata([p[1] for p in box_global])
        sensors_global = [_robot_to_global(x,SENSOR_Y,history[frame]) for x in [LEFT_SENSOR_X,MIDDLE_SENSOR_X,RIGHT_SENSOR_X]]
        sensors_line.set_xdata([p[0] for p in sensors_global])
        sensors_line.set_ydata([p[1] for p in sensors_global])
        return path_line, robot_line, sensors_line
    ani = animation.FuncAnimation(fig=fig, func=update, frames=range(0,len(history),10), interval=15)
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
    #animate_path()

if __name__=='__main__':
    _demo_robot()
from matplotlib import pyplot as plt

WHEEL_SEP = 5.0

x = 0.
y = 0.
theta = 0.

history = [(x,y,theta)]

def reset_robot():
    global x, y, theta
    x = 0
    y = 0
    history.clear()
    history.append((x,y,theta))

def drive(right_turn, left_turn):
    global x, y, theta
    turn_angle = (right_turn - left_turn)/WHEEL_SEP
    arc_length = 0.5*(right_turn + left_turn)
    curvature = turn_angle/arc_length
    x = x + right_turn
    y = y + left_turn
    history.append((x,y,theta))

def position_x():
    return x

def position_y():
    return y

def orientation():
    return theta

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
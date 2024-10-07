from matplotlib import pyplot as plt

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
    x = x + right_turn
    y = y + left_turn
    history.append((x,y,theta))

def position_x():
    return x

def position_y():
    return y

def orientation():
    return theta

def plot_path():
    plt.plot([p[0] for p in history],
             [p[1] for p in history])
    plt.axis('equal')
    plt.show()
import numpy as np
import random

DEAD = 0
ALIVE = 1
ALIVE_PROBABILITY = 0.1

def generate_grid(length, alive_probability):
    """
    Make a grid of specified shape with cells randomly set to one or zero, with probabillity p. 
    Inputs:
      length (integer) - The size of the grid. The grid will be a square with width and height of magnitude length.
      alive_probability (float) - The probability that any given cell is set to alive.
    """
    grid = (np.random.random((length,length)) < alive_probability).astype(np.int8)
    return grid
def update_grid(old_grid, rule=None):
    pass

def update_cell(cell_section: np.array):
    pass

def display_grid(grid):
    pass




def test_update_grid():
    pass

print(generate_grid(5,0.1))
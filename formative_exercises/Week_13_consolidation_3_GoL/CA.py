import numpy as np 
import matplotlib.pyplot as plt 
import random
import copy

ALIVE = 1 
DEAD = 0 
GRID_LENGTH = 100
#ALIVE INDEX is the index of the single cell which is set to 1.
ALIVE_INDEX = 10
#ALIVE probability is the fraction of a random grid which is set to 1.
ALIVE_PROBABILITY = 0.1 
NUM_STEPS = 100

def create_singleton_grid(length, alive_index):
  '''
  Make a grid of specified length with all cells apart from one set to zero.
  Inputs:
    grid_length (integer) - the size of the grid
    one_index (integer) - the index of the cell which is set to one.
  Returns:
    grid (numpy array)
  '''
  
  grid = np.zeros(length, dtype=np.int8)
  #Your code goes here

  return grid

def create_random_grid(length, alive_probability):
  '''
  Make a grid of specified length with cells randomly set to one or zero, with probability p.
  Inputs:
    #You should edit this to match your function.
  Returns:
    grid (numpy array)
  '''

  #Your code goes here
  grid = [0 for _ in range(length)] 

  return np.array(grid, dtype=np.int8)

def update_cell(old_value, left_neighbour, right_neighbour):
  '''
  Calculates the new value for a cell given the old value and the values of the left and right neighbours
  Inputs:
    old_value (integer)
    left_neighbour (integer)
    right_neighbour (integer)
  Returns:
    new_value (integer)
  '''

  new_value = 0 
  #Your code goes here
  return new_value

def update_grid(old_grid, rule=None):
  '''
  Update the values within a grid according to local rules.
  Inputs:
      old_grid (numpy array)
  Returns:
    new_grid (numpy array)
    '''

  #Your code goes here
  new_grid = np.zeros(len(old_grid))

  return np.array(new_grid, dtype=np.int8)

def test_update_cell():

  assert update_cell(0,0,0)==0, "test 1"
  assert update_cell(1,0,0)==0, "test 2"
  assert update_cell(0,1,0)==1, "test 3"
  assert update_cell(0,0,1)==0, "test 4"
  assert update_cell(1,1,0)==0, "test 5"
  assert update_cell(l1,0,1)==0, "test 6"
  #Add the rest of the tests here - you should cover inputs of (0, 1, 1) and (1, 1, 1)

def test_update_grid():

  assert (update_grid((np.array([1, 0, 0], dtype=np.int8)))==np.array([0, 1, 0], dtype=np.int8)).all()==True
  assert (update_grid((np.array([0, 1, 0], dtype=np.int8)))==np.array([0, 0, 1], dtype=np.int8)).all()==True
  assert (update_grid((np.array([0, 0, 1], dtype=np.int8)))==np.array([1, 0, 0], dtype=np.int8)).all()==True
  assert (update_grid((np.array([1, 1, 1], dtype=np.int8)))==np.array([0, 0, 0], dtype=np.int8)).all()==True
  assert (update_grid((np.array([0, 0, 0], dtype=np.int8)))==np.array([0, 0, 0], dtype=np.int8)).all()==True  
  #Add more tests here - for a length 3 grid, you should have 8 possible initial states to test.


def plot_grids(grids):

  fig = plt.figure(figsize=(10, 10))
  ax1 = fig.add_subplot(211)
  ax1.set_axis_off()
  image = np.zeros((len(grids), GRID_LENGTH), dtype = np.int8)
  #Copy CA_grid into the image array

  for (index, grid) in enumerate(grids):
    image[index, :] = grid
  #Display the image

  ax1.imshow(image, interpolation='none', cmap='RdPu')
  plt.show()

def run_tests():

  print("Testing update cell\n")
  test_update_cell()
  print("Tests passed")
  print("Testing update grid\n")
  test_update_grid()
  print("Tests passed")


def main():

  #Uncomment the line below to run test functions
  #run_tests()

  #Functions for making a grid - use commenting to choose which runs.
  grid = create_singleton_grid(GRID_LENGTH, ALIVE_INDEX)
  #grid = create_random_grid(GRID_LENGTH, ALIVE_PROBABILITY)

  grids = []

  #Use a list to store all the grids we generate
  grids = []
  #Repeatedly apply the update rule for a certain number of steps
  for t in range(NUM_STEPS):
    #Calculate the values in each position for the new grid
    new_grid = update_grid(grid)
    #Overwrite the old grid with the new grid
    grid=copy.deepcopy(new_grid)
    #Add the updated grid to our store
    grids.append(new_grid)

  #Plot all grids we've generated to observe how the CA evolves.
  plot_grids(grids)

main()
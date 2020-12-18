#!/usr/bin/python3 

from __future__ import print_function
import os
import sys
sys.path.append('/home/skyler/aoc')
import numpy as np
from aoc.aoc_common.input import InputManager

class CubeGrid:
  def __init__(self, initial_plane):
    self.initial_plane = initial_plane

  def initialize_grid(self, iters):
    x_size, y_size = self.initial_plane.shape
    self.grid = np.zeros((x_size + 2*iters, y_size + 2*iters, 1 + 2*iters, 1 + 2*iters), dtype=np.uint8)
    self.grid[iters:(iters+x_size), iters:(iters+y_size), iters, iters] = self.initial_plane

  def simulate(self, iters):
    self.initialize_grid(iters)
    self.print_grid()
    for i in range(iters):
      self.step_grid()
      self.print_grid()
  
  def step_grid(self):
    x_size, y_size, z_size, j_size = self.grid.shape
    new_grid = self.grid.copy()
    for x in range(x_size):
      for y in range(y_size):
        for z in range(z_size):
          for j in range(j_size):
            new_grid[x,y,z,j] = self.step_cell(x,y,z,j)
    self.grid = new_grid

  def step_cell(self, x,y,z,j):
    nbr_cnt = self.count_neighbors(x,y,z,j)
    if self.grid[x,y,z,j] == 1:
      return int(nbr_cnt in [2,3])
    else:
      return int(nbr_cnt == 3)

  def count_neighbors(self, x,y,z,j):
    x_size, y_size, z_size,j_size = self.grid.shape
    rng = [-1, 0, 1]
    nbr_cnt = 0
    x_min, x_max = max(0,x-1), min(x+1, x_size-1)
    y_min, y_max = max(0,y-1), min(y+1, y_size-1)
    z_min, z_max = max(0,z-1), min(z+1, z_size-1)
    j_min, j_max = max(0,j-1), min(j+1, j_size-1)
    return np.sum(self.grid[x_min:x_max+1, y_min:y_max+1, z_min:z_max+1, j_min:j_max+1]) - self.grid[x,y,z,j]


  def count_occupied(self):
    return np.sum(self.grid)

  def print_grid(self):    
    x_size, y_size, z_size, j_size = self.grid.shape
    for layer in range(z_size):
      if np.sum(self.grid[:,:,layer]) == 0:
        continue
      print("Layer ", layer)
      for row in range(x_size):
        for col in range(y_size):
          print(self.grid[row, col, layer], end='')
        print()
      print('\n')    


class GridCell:
  EMPTY = '.'
  OCCUPIED = '#'

class MyClass:
  def __init__(self, input_file):
    self.input = InputManager(input_file)
    self.lines = self.input.get_lines()
    # Do common input processing here
    initial_plane = []
    for line in self.lines:
      line_vals = []
      for ch in line:
        if ch == GridCell.EMPTY:
          line_vals.append(0)
        elif ch == GridCell.OCCUPIED:
          line_vals.append(1)
        else:
          raise RuntimeError("Bad input")
      initial_plane.append(line_vals)
    self.cube_grid = CubeGrid(np.array(initial_plane))

  def get_part1_result(self):
    self.cube_grid.simulate(6)
    return self.cube_grid.count_occupied()

  def get_part2_result(self):
    pass



def main():
  cur_dir = os.path.dirname(os.path.realpath(__file__))
  input_file = os.path.join(cur_dir, "input.txt")
  myclass = MyClass(input_file)
  print(" == Part 1 Result: ==\n", myclass.get_part1_result())

  print("\n == Part 2 Result: ==\n", myclass.get_part2_result())


if __name__ == '__main__':
  main()



#!/usr/bin/python3 

from __future__ import print_function
import os
import sys
sys.path.append('/home/skyler/aoc')
import numpy as np
from aoc.aoc_common.input import InputManager
from functools import reduce

class SeatType:
  FLOOR = '.'
  EMPTY = 'L'
  OCCUPIED = '#'

class SeatingArea:
  def __init__(self, rows):
    self.seats = np.array([[c for c in row] for row in rows])
    self.prev_seats = None
    self.rows = len(self.seats)
    self.cols = len(self.seats[0])

  def get_occupied_neighbor_count(self, row, col):
    cnt = 0
    for i in [-1, 0, 1]:
      if (row+i) < 0 or row+i > self.rows-1: 
        continue
      for j in [-1, 0, 1]:
        if col+j < 0 or col+j > self.cols-1 or i==j==0:
          continue
        if self.seats[row+i][col+j] == SeatType.OCCUPIED:
          cnt += 1
    return cnt 

  def get_occupied_neighbor_count_part2(self, row, col):
    cnt = 0
    cnts = np.zeros((3,3))
    for row_delta in [-1, 0, 1]:
      for col_delta in [-1, 0, 1]:
        if row_delta==col_delta==0:
          continue
        r,c = row,col
        while 0 <= r < self.rows and 0 <= c < self.cols:
          r += row_delta
          c += col_delta
          if r < 0 or r > self.rows-1 or c < 0 or c > self.cols-1:
            break
          seat_type = self.seats[r][c]
          if seat_type == SeatType.OCCUPIED:
            cnts[row_delta+1][col_delta+1] = 1
            cnt += 1
            break
          if seat_type == SeatType.EMPTY:
            break
    # print("row, col = {}, {}".format(row_delta, col_delta))
    # print("neighbor counts: \n", cnts)
    return cnt 

  def iterate_seat(self, row, col):
    # If floor, return the same
    val = self.seats[row][col]
    occupied_nbr_cnt = self.get_occupied_neighbor_count_part2(row, col)
    if val == SeatType.EMPTY and occupied_nbr_cnt == 0:
      return SeatType.OCCUPIED
    elif val == SeatType.OCCUPIED and occupied_nbr_cnt >= 5:
      return SeatType.EMPTY
    else:
      return val

  def iterate_area(self):
    new_seats = np.copy(self.seats)
    for row in range(self.rows):
      for col in range(self.cols):
        new_seats[row][col] = self.iterate_seat(row, col)
    self.prev_seats = np.copy(self.seats)
    self.seats = new_seats

  def is_stable(self):
    if self.prev_seats is None:
      return False
    comparison = self.prev_seats == self.seats
    changes = np.size(comparison) - np.count_nonzero(comparison)
    return changes == 0

  def __str__(self):
    s = ''
    for r in range(self.rows):
      for c in range(self.cols):
        s += self.seats[r][c]
      s += '\n'
    return s
    

class MyClass:
  def __init__(self, input_file):
    self.input = InputManager(input_file)
    self.lines = self.input.get_lines()
    self.seating_area = SeatingArea(self.lines)
    # print(self.seating_area)

  def get_part1_result(self):
    while not self.seating_area.is_stable():
      self.seating_area.iterate_area()
      # print(self.seating_area)
    return np.count_nonzero(self.seating_area.seats == SeatType.OCCUPIED)
    

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



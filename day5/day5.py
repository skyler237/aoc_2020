#!/usr/bin/python3 

from __future__ import print_function
import os
import sys
sys.path.append('/home/skyler/aoc')
import numpy as np
from aoc.aoc_common.input import InputManager

class MyClass:
  def __init__(self, input_file):
    self.input = InputManager(input_file)
    self.lines = self.input.get_lines()
    # Do common input processing here
    self.boarding_passes = []
    self.get_boarding_passes()

  def get_boarding_passes(self):
    for l in self.lines:
      row_str = self.convert_to_binary(l[0:7])
      col_str = self.convert_to_binary(l[7:10])
      row = int(row_str, 2)
      col = int(col_str, 2)
      seat_id = row*8 + col
      self.boarding_passes.append({'row':row, 'col':col, 'id':seat_id})

  def convert_to_binary(self, s):
    return s.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')

  def get_part1_result(self):
    max_id = 0
    for bp in self.boarding_passes:
      max_id = max(bp['id'], max_id)
    return max_id

  def get_part2_result(self):
    valid_ids = set(range(0, 128*8))
    for bp in self.boarding_passes:
      valid_ids.remove(bp['id'])
    for x in valid_ids:
      if not ((x+1) in valid_ids or (x-1) in valid_ids):
        return x



def main():
  cur_dir = os.path.dirname(os.path.realpath(__file__))
  input_file = os.path.join(cur_dir, "input.txt")
  # input_file = os.path.join(cur_dir, "test_input.txt")
  myclass = MyClass(input_file)
  print(" == Part 1 Result: ==\n", myclass.get_part1_result())

  print("\n == Part 2 Result: ==\n", myclass.get_part2_result())


if __name__ == '__main__':
  main()



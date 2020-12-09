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
    self.lines = self.input.get_lines(as_type=int)
    # Do common input processing here

  def is_valid_number_at(self, idx):
    if idx < 25:
      return True
    val = self.lines[idx]
    is_valid = False
    for i in range(25):
      is_valid |= (val - self.lines[idx-i]) in self.lines[idx-25:idx]
    return is_valid

  def get_part1_result(self):
    for i in range(len(self.lines)):
      if not self.is_valid_number_at(i):
        return self.lines[i]

  def get_part2_result(self):
    magic_number = self.get_part1_result()
    for i in range(len(self.lines)):
      total = 0
      j = i
      numbers = []
      while total < magic_number:
        total += self.lines[j]
        numbers.append(self.lines[j])
        j += 1
      if total == magic_number:
        return min(numbers) + max(numbers)



def main():
  cur_dir = os.path.dirname(os.path.realpath(__file__))
  input_file = os.path.join(cur_dir, "input.txt")
  myclass = MyClass(input_file)
  print(" == Part 1 Result: ==\n", myclass.get_part1_result())

  print("\n == Part 2 Result: ==\n", myclass.get_part2_result())


if __name__ == '__main__':
  main()



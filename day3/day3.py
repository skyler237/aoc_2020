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
    self.trees = self.input.get_lines()

  def count_trees(self, slope):
    row = 0
    col = 0
    tree_cnt = 0
    while row < len(self.trees):
      row_width = len(self.trees[row])
      if self.trees[row][col % row_width] == '#':
        tree_cnt += 1
      if slope > 1:
        row += 1
        col += slope
      else:
        row += int(1.0/slope)
        col += 1
    return tree_cnt

  def get_final_result(self):
    # return self.count_trees(3)
    c1 = self.count_trees(1)
    c2 = self.count_trees(3)
    c3 = self.count_trees(5)
    c4 = self.count_trees(7)
    c5 = self.count_trees(0.5)
    print("{} {} {} {} {}".format(c1,c2,c3,c4,c5))
    return c1 * c2 * c3 * c4 * c5


def main():
  cur_dir = os.path.dirname(os.path.realpath(__file__))
  input_file = os.path.join(cur_dir, "input.txt")
  myclass = MyClass(input_file)
  print(" == Result: ==\n", myclass.get_final_result())


if __name__ == '__main__':
  main()



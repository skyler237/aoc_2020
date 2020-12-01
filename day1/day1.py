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

  def find_2020_part2(self):
    numbers = np.array(self.input.get_lines(as_type=int)).reshape(-1,1,1)
    numbers_vert = numbers.reshape(1,-1,1)
    numbers_3 = numbers.reshape(1, 1, -1)
    sums = numbers + numbers_vert + numbers_3
    print(sums)
    for i, mat in enumerate(sums):
      for j, row in enumerate(mat):
        for k, val in enumerate(row):
          if val == 2020:
            return (numbers[i], numbers[j], numbers[k])

  def find_2020(self):
    numbers = np.array(self.input.get_lines(as_type=int))
    numbers_vert = numbers.reshape(-1,1)
    sums = numbers + numbers_vert
    for i, row in enumerate(sums):
      for j, val in enumerate(row):
        if val == 2020:
          return (numbers[i], numbers[j])

  def get_final_result(self):
    num1, num2, num3 = self.find_2020_part2()
    print(num1, num2, num3)
    return num1*num2*num3



def main():
  cur_dir = os.path.dirname(os.path.realpath(__file__))
  input_file = os.path.join(cur_dir, "input.txt")
  myclass = MyClass(input_file)
  print(" == Result: ==\n", myclass.get_final_result())


if __name__ == '__main__':
  main()



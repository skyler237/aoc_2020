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
    self.jolts = [0] + self.input.get_lines(as_type=int)
    self.jolts.append(max(self.jolts) + 3)
    self.jolts.sort()
    self.cnt = 0
    self.permutation_counts = {}
    # Do common input processing here

  def get_part1_result(self):
    jolts_array = np.array(self.jolts)
    diff = list(jolts_array[1:] - jolts_array[0:-1])
    print(max(diff))
    return diff.count(1) * diff.count(3)

  def count_permutations(self, idx):
    if idx in self.permutation_counts:
      return self.permutation_counts[idx]
    cnt = 0
    if idx == len(self.jolts) - 1:
      cnt = 1
    else:
      i = idx + 1
      while i < len(self.jolts) and (self.jolts[i] - self.jolts[idx]) < 4:
        cnt += self.count_permutations(i)
        i += 1
    self.permutation_counts[idx] = cnt
    return cnt

  def get_part2_result(self):
    return self.count_permutations(0)
    pass



def main():
  cur_dir = os.path.dirname(os.path.realpath(__file__))
  input_file = os.path.join(cur_dir, "input.txt")
  myclass = MyClass(input_file)
  print(" == Part 1 Result: ==\n", myclass.get_part1_result())

  print("\n == Part 2 Result: ==\n", myclass.get_part2_result())


if __name__ == '__main__':
  main()



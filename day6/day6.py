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
    self.lines = self.input.get_lines(strip_whitespace=False)
    # Do common input processing here
    self.groups = []
    self.get_groups()
    # print(self.groups)

  def get_groups(self):
    self.current_group = []
    for l in self.lines:
      if l == '\n':
        self.groups.append(self.current_group)
        self.current_group = []
      else:
        self.current_group.append(l.strip())
    self.groups.append(self.current_group)


  def get_part1_result(self):
    total_count = 0
    for group in self.groups:
      unique_answers = set()
      for line in group:
        for char in line:
          unique_answers.add(char)
      total_count += len(unique_answers)
    return total_count

  def get_part2_result(self):
    total_count = 0
    for group in self.groups:
      group_answers = [set(c for c in line) for line in group]
      common_answers = group_answers[0]
      for answers in group_answers:
        common_answers.intersection_update(answers)      
      total_count += len(common_answers)
    return total_count



def main():
  cur_dir = os.path.dirname(os.path.realpath(__file__))
  input_file = os.path.join(cur_dir, "input.txt")
  myclass = MyClass(input_file)
  print(" == Part 1 Result: ==\n", myclass.get_part1_result())

  print("\n == Part 2 Result: ==\n", myclass.get_part2_result())


if __name__ == '__main__':
  main()



#!/usr/bin/python3 

from __future__ import print_function
import os
import sys
sys.path.append('/home/skyler/aoc')
import numpy as np
from aoc_common.input import InputManager

class MyClass:
  def __init__(self, input_file):
    self.input = InputManager(input_file)

  def get_final_result(self):
    pass



def main():
  cur_dir = os.path.dirname(os.path.realpath(__file__))
  input_file = os.path.join(cur_dir, "input.txt")
  myclass = MyClass(input_file)
  print(" == Result: ==\n", myclass.get_final_result())


if __name__ == '__main__':
  main()



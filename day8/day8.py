#!/usr/bin/python3 

from __future__ import print_function
import os
import sys
sys.path.append('/home/skyler/aoc')
import numpy as np
from aoc.aoc_common.input import InputManager
import copy

class CodeRunner:
  def __init__(self, code):
    self.idx = 0
    self.original_code = code
    self.code = code  
    self.executed_idxs = set()
    self.accumulator = 0
    self.nop_jmp_idxs = [i for i,x in enumerate(self.code) if 'nop' in x or 'jmp' in x]
    self.execution_trail = []
  
  def execute_instruction(self):
    instruction, num_str = self.code[self.idx].split()
    num = int(num_str)
    self.executed_idxs.add(self.idx)
    self.execution_trail.append((instruction, num, self.idx, self.accumulator))
    if instruction == 'nop':
      self.idx += 1
    elif instruction == 'acc':
      self.accumulator += num
      self.idx += 1
    elif instruction == 'jmp':
      self.idx += num

  def run_code(self):
    while self.idx not in self.executed_idxs:
      self.execute_instruction()
      if self.idx == len(self.code):
        return True, self.accumulator
    return False, self.accumulator

  def reset(self):
    self.idx = 0
    self.accumulator = 0
    self.executed_idxs = set()
    self.code = copy.deepcopy(self.original_code)
    self.execution_trail = []

  def run_modified_code(self):
    for i in self.nop_jmp_idxs:
      self.reset()
      if 'jmp' in self.code[i]:
        self.code[i] = self.code[i].replace('jmp', 'nop')
      elif 'nop' in self.code[i]:
        self.code[i] = self.code[i].replace('nop', 'jmp')
      finished, acc = self.run_code()
      if (finished):
        print(self.execution_trail)
        return acc
    return None    


class MyClass:
  def __init__(self, input_file):
    self.input = InputManager(input_file)
    self.lines = self.input.get_lines()
    # Do common input processing here
    self.code_runner = CodeRunner(self.lines)

  def get_part1_result(self):
    return self.code_runner.run_code()[1]

  def get_part2_result(self):
    return self.code_runner.run_modified_code()


def main():
  cur_dir = os.path.dirname(os.path.realpath(__file__))
  input_file = os.path.join(cur_dir, "input.txt")
  myclass = MyClass(input_file)
  print(" == Part 1 Result: ==\n", myclass.get_part1_result())

  print("\n == Part 2 Result: ==\n", myclass.get_part2_result())


if __name__ == '__main__':
  main()



#!/usr/bin/python3 

from __future__ import print_function
import os
import sys
sys.path.append('/home/skyler/aoc')
import numpy as np
from aoc.aoc_common.input import InputManager

class PasswordManager:
  def __init__(self, input_file):
    self.input = InputManager(input_file)
    self.passwords = [list(line.split(':')) for line in self.input.get_lines()]
    self.valid_passwords = [x[1] for x in self.passwords if self.is_pw_valid(*x)]
    self.valid_passwords_part2 = [x for x in self.passwords if self.is_pw_valid_part2(*x)]
    self.invalid_passwords_part2 = [x for x in self.passwords if not self.is_pw_valid_part2(*x)]

  def is_pw_valid(self, rule, pw):
    range_str, char = rule.split()
    lower, upper = range_str.split('-')
    if int(lower) <= pw.count(char) <= int(upper):
      return True

  def is_pw_valid_part2(self, rule, pw):
    pw = pw.strip()
    range_str, char = rule.split()
    lower, upper = range_str.split('-')
    return (pw[int(lower)-1] == char) ^ (pw[int(upper)-1] == char)

  def get_final_result(self):
    return len(self.valid_passwords_part2)



def main():
  cur_dir = os.path.dirname(os.path.realpath(__file__))
  input_file = os.path.join(cur_dir, "input.txt")
  pw_manager = PasswordManager(input_file)
  print(" == Result: ==\n", pw_manager.get_final_result())


if __name__ == '__main__':
  main()



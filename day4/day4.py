#!/usr/bin/python3 

from __future__ import print_function
import os
import sys
sys.path.append('/home/skyler/aoc')
import numpy as np
import re
from aoc.aoc_common.input import InputManager

class MyClass:
  def __init__(self, input_file):
    self.input = InputManager(input_file)
    self.lines = self.input.get_lines(strip_whitespace=False)
    # Do common input processing here
    self.get_passports()
    self.required_keys = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    self.complete_passports = []
    self.get_complete_passports()
    self.valid_passports = []
    self.get_valid_passports()
    # self.required_keys = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid',]

  def get_passports(self):
    self.passports = []
    current_pp = {}
    for l in self.lines:
      # print("line = '", l, "'")
      if l == '\n':
        self.passports.append(current_pp.copy())
        current_pp = {}
      else:
        for pair in l.split():
          k,v = pair.split(':')
          current_pp[k.strip()] = v.strip()
    if len(current_pp) > 0:
      self.passports.append(current_pp)
    # print(self.passports)

  def get_complete_passports(self):
    complete_pp_cnt = 0
    for p in self.passports:
      is_valid = True
      for k in self.required_keys:
        if k not in p.keys():
          is_valid = False
          break
      if is_valid:
        complete_pp_cnt += 1
        self.complete_passports.append(p)

  def get_valid_passports(self):
    for p in self.complete_passports:
      is_valid = True
      for k,v in p.items():
        if not self.is_valid(k, v):
          is_valid = False
          break
      if is_valid:
        self.valid_passports.append(p)
    

  def is_valid(self, key, value):
    is_pair_valid = True
    if key == 'byr':
      is_pair_valid = len(value) == 4 and (1920 <= int(value) <= 2002)
    elif key == 'iyr':
      is_pair_valid = len(value) == 4 and (2010 <= int(value) <= 2020)
    elif key == 'eyr':
      is_pair_valid = len(value) == 4 and (2020 <= int(value) <= 2030)
    elif key == 'hgt':
      if len(value) < 4:
        is_pair_valid = False
      else:
        ending = value[-2:]
        num = int(value[:-2])
        is_pair_valid = (ending == 'in' and (59 <= num <= 76)) or (ending == 'cm' and (150 <= num <= 193))
    elif key == 'hcl':
      re_str = '#[0-9a-f]{6}'
      is_pair_valid = re.search(re_str, value) is not None and len(value) == 7
    elif key == 'ecl':
      is_pair_valid = value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif key == 'pid':
      re_str = '[0-9]{9}'
      is_pair_valid = re.search(re_str, value) is not None and len(value) == 9
    elif key == 'cid':
      is_pair_valid = True
    return is_pair_valid


  def get_part1_result(self):
    return len(self.complete_passports)

  def get_part2_result(self):
    return len(self.valid_passports)


def main():
  cur_dir = os.path.dirname(os.path.realpath(__file__))
  input_file = os.path.join(cur_dir, "input.txt")
  myclass = MyClass(input_file)
  print(" == Part 1 Result: ==\n", myclass.get_part1_result())

  print("\n == Part 2 Result: ==\n", myclass.get_part2_result())


if __name__ == '__main__':
  main()



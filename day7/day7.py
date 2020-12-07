#!/usr/bin/python3 

from __future__ import print_function
import os
import sys
sys.path.append('/home/skyler/aoc')
import numpy as np
from aoc.aoc_common.input import InputManager
from collections import defaultdict


class MyClass:
  def __init__(self, input_file):
    self.input = InputManager(input_file)
    self.lines = self.input.get_lines()
    # Do common input processing here
    self.rules = self.get_rules()
    # print(self.rules)
    self.flattened_rules = self.flatten_rules()
    print(self.flattened_rules)
    self.contains_colors_dict = self.get_contains_colors_dict(self.flattened_rules)

  def get_rules(self):
    # rule = {color: [(cnt0, contains_color0), (cnt1, contains_color1), ...], ...}
    # Example: light red bags contain 1 bright white bag, 2 muted yellow bags.
    #   -> {'light red': [(1, 'bright white'), (2, 'muted yellow')], ...}
    rules = {}
    for l in self.lines:
      words = l.split()
      color = ' '.join(words[0:2])
      contains_strs = l.split('contain')[1].strip().strip('.').split(',')
      contains_list = []
      for c_str in contains_strs:
        if c_str == "no other bags":
          break
        words = c_str.split()
        cnt = int(words[0])
        contains_color = ' '.join(words[1:3])
        contains_list.append((cnt, contains_color))
      rules[color] = contains_list
    return rules      

  def flatten_rules(self):
    return {color:self.get_bags_list(color) for color in self.rules.keys()}

  def get_bags_list(self, color, multiplier=1):
    bags_list = []
    contains_list = self.rules[color]
    if len(contains_list) == 0:
      return bags_list
    for cnt, contains_color in contains_list:
      bags_list.append((multiplier*cnt, contains_color))
      bags_list.extend(self.get_bags_list(contains_color, multiplier*cnt))
    return bags_list

  def get_contains_colors_dict(self, rules):
    contains_colors_dict = defaultdict(set)
    for color, contains_colors in rules.items():
      for cnt, contains_color in contains_colors:
        contains_colors_dict[color].add(contains_color)
    return contains_colors_dict

  def get_part1_result(self):
    shiny_gold_cnt = 0
    for color, contains_colors in self.contains_colors_dict.items():
      if 'shiny gold' in contains_colors:
        shiny_gold_cnt += 1
    return shiny_gold_cnt

  def get_part2_result(self):
    total_contained_bags = 0
    for cnt, contains_color in self.flattened_rules['shiny gold']:
      total_contained_bags += cnt
    return total_contained_bags



def main():
  cur_dir = os.path.dirname(os.path.realpath(__file__))
  input_file = os.path.join(cur_dir, "input.txt")
  myclass = MyClass(input_file)
  print(" == Part 1 Result: ==\n", myclass.get_part1_result())

  print("\n == Part 2 Result: ==\n", myclass.get_part2_result())


if __name__ == '__main__':
  main()



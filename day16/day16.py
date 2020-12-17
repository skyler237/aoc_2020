#!/usr/bin/python3 

from __future__ import print_function
import os
import sys
sys.path.append('/home/skyler/aoc')
import numpy as np
from aoc.aoc_common.input import InputManager
from copy import deepcopy

class Rule:
  def __init__(self, rule_str=None, ranges=None):
    self.name, ranges_str = rule_str.split(':')
    self.ranges = []
    for range_str in ranges_str.split('or'):
      low, high = [int(x) for x in range_str.split('-')]
      self.ranges.append([low, high])

  def __add__(self, other):
    combined_ranges = []
    all_ranges = self.ranges + other.ranges
    all_ranges.sort(key=lambda x : x[0])
    low, high = all_ranges[0]
    for r in all_ranges[1:]:
      if r[0] > high:
        combined_ranges.append([low, high])
        low, high = r
      elif r[1] > high:
        high = r[1]
    combined_ranges.append([low, high])
    rule = deepcopy(self)
    rule.name += ', ' + other.name
    rule.ranges = combined_ranges
    return rule

  def is_valid_value(self, val):
    is_valid = False
    for r in self.ranges:
      is_valid |= (r[0] <= val <= r[1])
    return is_valid

class Rules:
  def __init__(self, rule_lines):
    self.rules = [Rule(l) for l in rule_lines]
    self.combined_rule = self.get_combined_rule()
    self.solved_rules_candidates = []

  def get_combined_rule(self):
    return np.sum(self.rules)

  def get_invalid_fields(self, ticket):
    invalid_fields = []
    for v in ticket.fields:
      if not self.combined_rule.is_valid_value(v):
        invalid_fields.append(v)
    return invalid_fields

  def test_rules(self, tickets):
    for i in range(len(tickets[0])):
      valid_rules = []
      for rule in self.rules:
        all_values_valid = True
        for t in tickets:
          all_values_valid &= rule.is_valid_value(t[i])
          if not all_values_valid:
            break
        if all_values_valid:
          valid_rules.append(rule)
      self.solved_rules_candidates.append(valid_rules)
    
    self.solved_rules = [None]*len(self.solved_rules_candidates)
    idx = 0
    while None in self.solved_rules:
      if len(self.solved_rules_candidates[idx]) == 1:
        solved_rule = self.solved_rules_candidates[idx][0]
        self.solved_rules[idx] = solved_rule
        for candidates in self.solved_rules_candidates:
          if solved_rule in candidates:
            candidates.remove(solved_rule)
      idx = (idx + 1)%len(self.solved_rules_candidates)

        


class Ticket:
  def __init__(self, ticket_str):
    self.ticket_str = ticket_str
    self.fields = [int(x) for x in ticket_str.split(',')]

  def __len__(self):
    return len(self.fields)

  def __getitem__(self, i):
    return self.fields[i]

class MyClass:
  def __init__(self, input_file):
    self.input = InputManager(input_file)
    line_groups = self.input.get_lines(group=True)
    rule_lines = line_groups[0]
    self.rules = Rules(rule_lines)
    self.my_ticket = Ticket(line_groups[1][1])
    self.nearby_tickets = [Ticket(l) for l in line_groups[2][1:]]
    self.valid_tickets = []

  def get_part1_result(self):
    invalid_fields_sum = 0
    for ticket in self.nearby_tickets:
      invalid_fields = self.rules.get_invalid_fields(ticket)
      if len(invalid_fields) == 0:
        self.valid_tickets.append(ticket)
      else:
        invalid_fields_sum += sum(invalid_fields)
    return invalid_fields_sum

  def get_part2_result(self):
    self.valid_tickets.append(self.my_ticket)
    self.rules.test_rules(self.valid_tickets)
    departure_product = 1
    for idx in range(len(self.rules.solved_rules)):
      if self.rules.solved_rules[idx].name.startswith('departure'):
        departure_product *= self.my_ticket[idx]
    return departure_product



def main():
  cur_dir = os.path.dirname(os.path.realpath(__file__))
  input_file = os.path.join(cur_dir, "input.txt")
  myclass = MyClass(input_file)
  print(" == Part 1 Result: ==\n", myclass.get_part1_result())

  print("\n == Part 2 Result: ==\n", myclass.get_part2_result())


if __name__ == '__main__':
  main()



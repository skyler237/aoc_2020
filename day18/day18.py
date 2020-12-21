#!/usr/bin/python3 

from __future__ import print_function
import os
import sys
sys.path.append('/home/skyler/aoc')
import numpy as np
from aoc.aoc_common.input import InputManager

def split_expression(e):
  split_expr = []
  e = e.replace(' ','')
  i = 0
  current_group = ''
  while i < len(e):
    c = e[i]
    if c.isdigit():
      current_group += c
    else:
      split_expr.append(current_group)
      split_expr.append(c)
      current_group = ''
    i += 1
  split_expr.append(current_group)
  return split_expr
  

def eval_expression(e):
  groups = e.split('*')
  result_prod = 1
  for g in groups:
    e = split_expression(g)
    result = int(e[0])
    i = 1
    while i < len(e)-1:
      if e[i] == '+':
        result += int(e[i+1])
        i += 2
      elif e[i] == '*':
        result *= int(e[i+1])
        i += 2
      else:
        print("invalid character: ", e[i])
        return 0
    result_prod *= result
  return result_prod

def find_sub_expression(expr):
  left = expr.find('(')
  right = -1
  left_cnt = 1
  right_cnt = 0
  i = left + 1
  while i < len(expr):
    c = expr[i]
    if c == '(':
      left_cnt += 1
    elif c == ')':
      right_cnt += 1
    if left_cnt == right_cnt:
      right = i
      break
    i += 1
  return left, right

def eval_all_expressions(expr):
  left, right = find_sub_expression(expr)
  while left != -1:
    sub_expr = expr[left+1:right]
    sub_result = eval_all_expressions(sub_expr)
    expr = "{} {} {}".format(expr[:left], sub_result, expr[right+1:])
    left, right = find_sub_expression(expr)
  return eval_expression(expr)

class MyClass:
  def __init__(self, input_file):
    self.input = InputManager(input_file)
    self.lines = self.input.get_lines()
    # Do common input processing here


  def get_part1_result(self):
    result_sum = 0
    for line in self.lines:
      res = eval_all_expressions(line)
      result_sum += res
    return result_sum

  def get_part2_result(self):
    pass



def main():
  cur_dir = os.path.dirname(os.path.realpath(__file__))
  input_file = os.path.join(cur_dir, "input.txt")
  myclass = MyClass(input_file)
  print(" == Part 1 Result: ==\n", myclass.get_part1_result())

  print("\n == Part 2 Result: ==\n", myclass.get_part2_result())


if __name__ == '__main__':
  main()



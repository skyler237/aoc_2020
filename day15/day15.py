#!/usr/bin/python3 

from __future__ import print_function
import os
import sys
sys.path.append('/home/skyler/aoc')
import numpy as np
from aoc.aoc_common.input import InputManager
from collections import deque, defaultdict

class MemoryGame:
  def __init__(self, starting_numbers):
    self.starting_numbers = starting_numbers
    self.turn = 0
    self.prev_number = None
    self.numbers_last_turns = defaultdict(lambda : deque(maxlen=2))

  def play_game(self, turns):
    while self.turn < turns:
      if self.turn < len(self.starting_numbers):
        number_spoken = self.starting_numbers[self.turn]
      else:
        prev_number_turns = self.numbers_last_turns[self.prev_number]
        if len(prev_number_turns) < 2:
          number_spoken = 0
        else:
          number_spoken = prev_number_turns[1] - prev_number_turns[0]
      self.numbers_last_turns[number_spoken].append(self.turn)
      self.prev_number = number_spoken
      self.turn += 1
    return number_spoken

class MyClass:
  def __init__(self, input_file):
    self.input = InputManager(input_file)
    self.lines = self.input.get_lines()
    self.starting_numbers = [int(x) for x in self.lines[0].split(',')]
    # Do common input processing here

  def get_part1_result(self):
    game = MemoryGame(self.starting_numbers)
    return game.play_game(2020)

  def get_part2_result(self):
    game = MemoryGame(self.starting_numbers)
    return game.play_game(30000000)



def main():
  cur_dir = os.path.dirname(os.path.realpath(__file__))
  input_file = os.path.join(cur_dir, "input.txt")
  myclass = MyClass(input_file)
  print(" == Part 1 Result: ==\n", myclass.get_part1_result())

  print("\n == Part 2 Result: ==\n", myclass.get_part2_result())


if __name__ == '__main__':
  main()



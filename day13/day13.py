#!/usr/bin/python3 

from __future__ import print_function
import os
import sys
sys.path.append('/home/skyler/aoc')
import numpy as np
from aoc.aoc_common.input import InputManager

class BusSchedule:
  def __init__(self, interval):
    self.interval = interval
    self.scaled_interval = interval
    # Speed up delta t calculation
    self.prev_multiple = 0

  def get_earliest_time_after(self, t):
    return t + self.get_delta_t_after(t)

  def get_delta_t_after(self, t, min_delta=0):
    if self.scaled_interval < min_delta:
      self.scaled_interval *= int(np.ceil(min_delta / float(self.interval)))

    t -= self.prev_multiple*self.scaled_interval
    delta_t = (self.scaled_interval - (t % self.scaled_interval)) % self.scaled_interval
    self.prev_multiple += t // self.scaled_interval
    return delta_t

  def __repr__(self):
    return 'BusSchedule({})'.format(self.interval)

class MyClass:
  def __init__(self, input_file):
    self.input = InputManager(input_file)
    self.lines = self.input.get_lines()
    # Do common input processing here
    self.earliest_time = int(self.lines[0])
    self.bus_schedules = []
    for bus_id in self.lines[1].split(','):
      if bus_id.strip() == 'x':
        self.bus_schedules.append(None)
      else:
        self.bus_schedules.append(BusSchedule(int(bus_id.strip())))

  def get_part1_result(self):
    min_delta_t = np.inf
    min_id = None
    for bus in self.bus_schedules:
      if bus is None:
        continue
      delta_t = bus.get_delta_t_after(self.earliest_time)
      if delta_t < min_delta_t:
        min_delta_t = delta_t
        min_id = bus.interval
    return min_delta_t * min_id

  def get_part2_result(self):
    soln_found = False
    k = 0
    last_known_match_idx = 0
    increment = 1
    while not soln_found:
      k += increment
      soln_found = True
      for i, bus in enumerate(self.bus_schedules):
        if bus is None or i <= last_known_match_idx:
          continue
        delta_t = bus.get_delta_t_after(k*self.bus_schedules[0].interval, i)
        soln_found &= (i == delta_t)
        if soln_found:
          last_known_match_idx = i
          increment *= bus.interval
        else:
          break
    return k*self.bus_schedules[0].interval



def main():
  cur_dir = os.path.dirname(os.path.realpath(__file__))
  input_file = os.path.join(cur_dir, "input.txt")
  myclass = MyClass(input_file)
  print(" == Part 1 Result: ==\n", myclass.get_part1_result())

  print("\n == Part 2 Result: ==\n", myclass.get_part2_result())


if __name__ == '__main__':
  main()



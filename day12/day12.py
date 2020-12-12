#!/usr/bin/python3 

from __future__ import print_function
import os
import sys
sys.path.append('/home/skyler/aoc')
import numpy as np
from aoc.aoc_common.input import InputManager

class MotionType:
  NORTH = 'N'
  EAST = 'E'
  SOUTH = 'S'
  WEST = 'W'
  FORWARD = 'F'
  RIGHT = 'R'
  LEFT = 'L'

class ShipLocation:
  def __init__(self):
    self.pos = np.array([0., 0.]) # North, East
    self.direction = np.array([0., 1.]) # Facing east
    self.wp_pos = np.array([1., 10.])

  def move(self, command):
    motion_type = command[0]
    motion_value = int(command[1:])
    if motion_type == MotionType.NORTH:
      self.pos += np.array([motion_value, 0])
    elif motion_type == MotionType.EAST:
      self.pos += np.array([0, motion_value])
    elif motion_type == MotionType.SOUTH:
      self.pos += np.array([-motion_value, 0])
    elif motion_type == MotionType.WEST:
      self.pos += np.array([0, -motion_value])
    elif motion_type == MotionType.FORWARD:
      self.pos += self.direction*motion_value
    elif motion_type == MotionType.RIGHT:
      self.direction = self.get_rotation(motion_value).dot(self.direction)
    elif motion_type == MotionType.LEFT:
      self.direction = self.get_rotation(-motion_value).dot(self.direction)

  def move_to_wp(self, command):
    print("pos: ", self.pos)
    print("wp_pos: ", self.wp_pos)
    print(command)
    motion_type = command[0]
    motion_value = int(command[1:])
    if motion_type == MotionType.NORTH:
      self.wp_pos += np.array([motion_value, 0])
    elif motion_type == MotionType.EAST:
      self.wp_pos += np.array([0, motion_value])
    elif motion_type == MotionType.SOUTH:
      self.wp_pos += np.array([-motion_value, 0])
    elif motion_type == MotionType.WEST:
      self.wp_pos += np.array([0, -motion_value])
    elif motion_type == MotionType.FORWARD:
      self.pos += self.wp_pos*motion_value
    elif motion_type == MotionType.RIGHT:
      self.wp_pos = self.get_rotation(motion_value).dot(self.wp_pos)
    elif motion_type == MotionType.LEFT:
      self.wp_pos = self.get_rotation(-motion_value).dot(self.wp_pos)

  @staticmethod
  def get_rotation(theta):
    theta_rad = np.radians(theta)
    return np.array([[np.cos(theta_rad), -np.sin(theta_rad)],
                     [np.sin(theta_rad), np.cos(theta_rad)]])

  def get_manhattan_distance(self):
    print(self.pos)
    return np.abs(self.pos[0]) + np.abs(self.pos[1])

class MyClass:
  def __init__(self, input_file):
    self.input = InputManager(input_file)
    self.lines = self.input.get_lines()
    # Do common input processing here
    self.ship_location = ShipLocation()

  def get_part1_result(self):
    for command in self.lines:
      self.ship_location.move(command)
    return self.ship_location.get_manhattan_distance()

  def get_part2_result(self):
    for command in self.lines:
      self.ship_location.move_to_wp(command)
    return self.ship_location.get_manhattan_distance()



def main():
  cur_dir = os.path.dirname(os.path.realpath(__file__))
  input_file = os.path.join(cur_dir, "input.txt")
  myclass = MyClass(input_file)
  # print(" == Part 1 Result: ==\n", myclass.get_part1_result())

  print("\n == Part 2 Result: ==\n", myclass.get_part2_result())


if __name__ == '__main__':
  main()



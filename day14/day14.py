#!/usr/bin/python3 

from __future__ import print_function
import os
import sys
sys.path.append('/home/skyler/aoc')
import numpy as np
from aoc.aoc_common.input import InputManager

class BitMask:
  def __init__(self, bitmask_str):
    self.bitmask_str = bitmask_str
    self.valid_bits = {i:bit for i,bit in enumerate(bitmask_str) if bit != 'X'}
    self.wildcard_cnt = self.bitmask_str.count('X')

  def apply_to(self, val):
    val_binary_str = list('{:036b}'.format(val))
    for i, bit in self.valid_bits.items():
      val_binary_str[i] = bit
    return int(''.join(val_binary_str), 2)

  # For part 2
  def apply_to_address(self, addr):
    addr_binary_str = list('{:036b}'.format(addr))
    for i, bit in enumerate(self.bitmask_str):
      if bit in ['1','X']:
        addr_binary_str[i] = bit
    return [int(x, 2) for x in self.expand(addr_binary_str)]
    
  def expand(self, binary_list):
    expanded_strs = []
    wildcard_idxs = [i for i,bit in enumerate(binary_list) if bit == 'X']
    width = len(wildcard_idxs)
    for wildcard in range(2**len(wildcard_idxs)):
      wildcard_str = '{:0{width}b}'.format(wildcard, width=width)
      expansion = np.copy(binary_list)
      for i, bit in enumerate(wildcard_str):
        expansion[wildcard_idxs[i]] = bit
      expanded_strs.append(''.join(expansion))
    return expanded_strs

  def __str__(self):
    return self.bitmask_str


class BitMaskProgram:
  def __init__(self, code):
    self.mask = None
    self.code = code
    self.memory = {}

  def execute_code(self):
    for line in self.code:
      if line.startswith('mask'):
        self.mask = BitMask(line.split()[2])
      elif line.startswith('mem') and self.mask is not None:
        address = int(line[line.find('[') + 1 : line.find(']')])
        val = int(line.split()[2])
        masked_val = self.mask.apply_to(val)
        self.memory[address] = masked_val

  def execute_code_part2(self):
    for i, line in enumerate(self.code):
      if line.startswith('mask'):
        self.mask = BitMask(line.split()[2])
      elif line.startswith('mem') and self.mask is not None:
        address = int(line[line.find('[') + 1 : line.find(']')])
        val = int(line.split()[2])
        masked_addresses = self.mask.apply_to_address(address)
        memory_updates = {addr:val for addr in masked_addresses}
        # print("Line {} (mask={}, X={}) updating {} addresses\n{}"
        #      .format(i, self.mask, self.mask.wildcard_cnt, len(memory_updates), memory_updates))
        self.memory.update(memory_updates)        

  def get_memory_sum(self):
    return sum(self.memory.values())

  def reset(self):
    self.mask = None
    self.memory = {}


class MyClass:
  def __init__(self, input_file):
    self.input = InputManager(input_file)
    self.lines = self.input.get_lines()
    # Do common input processing here
    self.program = BitMaskProgram(self.lines)

  def get_part1_result(self):
    self.program.execute_code()
    return self.program.get_memory_sum()

  def get_part2_result(self):
    self.program.reset()
    self.program.execute_code_part2()
    return self.program.get_memory_sum()



def main():
  cur_dir = os.path.dirname(os.path.realpath(__file__))
  input_file = os.path.join(cur_dir, "input.txt")
  myclass = MyClass(input_file)
  print(" == Part 1 Result: ==\n", myclass.get_part1_result())

  print("\n == Part 2 Result: ==\n", myclass.get_part2_result())


if __name__ == '__main__':
  main()



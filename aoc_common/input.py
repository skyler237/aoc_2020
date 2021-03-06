#!/usr/bin/python3

class InputManager:
  def __init__(self, input_file):
    self.file = None
    try:
      self.file = open(input_file)
    except Exception as e:
      print(e)

  def get_lines(self, strip_whitespace=True, as_type=None, group=False):
    if group:
      groups = []
    lines = []
    for line in self.file:
      l = line
      if group and l == '\n':
        groups.append(lines)
        lines = []
      if (strip_whitespace):
        l = l.strip()
        if len(l) == 0:
          continue
      if as_type is not None:
        l = as_type(l)
      lines.append(l)
    if group:
      groups.append(lines)
      return groups
    else:
      return lines

  

  def __del__(self):
    if self.file is not None:
      self.file.close()
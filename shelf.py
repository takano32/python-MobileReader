#!/usr/bin/env python
import os
import fnmatch
import book
class Shelf:
  def __init__(self, path, pattern):
    self.path = os.path.abspath(path)
    if not self.path.startswith(os.path.abspath(".")):
      raise RuntimeError("Permission denied: " + abspath)
    self.pattern = pattern

  def list(self):
    alist = list()
    for(root, dirs, files) in os.walk(self.path):
      for file in files:
        if fnmatch.fnmatch(file, self.pattern):
          alist.append(file)
    return alist

shelf = Shelf("./maria", "*.txt")
for file in  shelf.list():
  print file
#for book in shelf.list():
#  print book

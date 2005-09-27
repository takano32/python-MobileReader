#!/usr/bin/env python
# coding: euc-jp
import os
def walk():
  for (root, dirs, files) in os.walk(u"."):
    print root, dirs
    #print dirs
    for f in files:
      if f == u'ふが':
        print f
        path = os.path.join(root, f)
        infile = open(path, 'r')
        data = infile.read()
        print data

walk()

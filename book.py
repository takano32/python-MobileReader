#!/usr/bin/env python
import os
from stat import *
import math

class Book:
  def __init__(self, path, page_size):
    self.path = path
    self.file = open(path)
    self.page_size = page_size
    self.size = self.size()

  def size(self):
    stat = os.stat(self.path)
    size = stat[ST_SIZE]
    return size

  def max_page(self):
    return math.ceil( float(self.size) / self.page_size)

  def page(self, page_number):
    self.file.seek(self.page_size * page_number)
    pos = self.file.tell()
    if page_number != 0:
      self.file.readline()
    pos -= self.file.tell()
    body = self.file.read(self.page_size + pos)
    lastLine = self.file.readline()
    if len(lastLine) != 0:
      lastLine = lastLine.splitlines()[0]
    body += lastLine
    return body

book = Book('/home/takano32/cvswork/python/'
                + 'mobilereader/maria/readme.txt', 200)

print book.max_page()

for i in range(book.max_page()):
  print "=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
  #print book.page(i)
  print unicode(book.page(i), "shift_jis")




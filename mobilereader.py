#!/usr/bin/env python
# vim: fileencoding=euc-jp
# coding: euc-jp
import os
import nkf
print u"普通の日本語"
print unicode("日本語の量が", "japanese.euc_jp")
print unicode("少ないとご認識", "japanese.euc_jp")


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


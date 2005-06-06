#!/usr/bin/env python
# vim: fileencoding=euc-jp
# coding: euc-jp
import os
from Cheetah.Template import Template
import nkf

template = Template(file='cheetah.tmpl')
template.entry = [
  {'title': "日本語", 'description': '内容 1, blah blah'},
  {'title': "タイトル", 'description': '内容 2, blah, blah'}
  ]
print template



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


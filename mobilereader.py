#!/usr/bin/env python
# vim: fileencoding=euc-jp
# coding: euc-jp
import os
import nkf
print u"���̤����ܸ�"
print unicode("���ܸ���̤�", "japanese.euc_jp")
print unicode("���ʤ��Ȥ�ǧ��", "japanese.euc_jp")


for (root, dirs, files) in os.walk(u"."):
  print root, dirs
  #print dirs
  for f in files:
    if f == u'�դ�':
      print f
      path = os.path.join(root, f)
      infile = open(path, 'r')
      data = infile.read()
      print data


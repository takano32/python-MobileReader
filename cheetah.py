#!/usr/bin/env python
# coding: euc-jp


from Cheetah.Template import Template
#import nkf

template = Template(file='cheetah.tmpl')
template.entry = [
  {'title': "���ܸ�", 'description': '���� 1, blah blah'},
  {'title': "�����ȥ�", 'description': '���� 2, blah, blah'}
  ]
print template


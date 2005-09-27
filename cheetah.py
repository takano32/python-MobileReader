#!/usr/bin/env python
# coding: euc-jp


from Cheetah.Template import Template
#import nkf

template = Template(file='cheetah.tmpl')
template.entry = [
  {'title': "日本語", 'description': '内容 1, blah blah'},
  {'title': "タイトル", 'description': '内容 2, blah, blah'}
  ]
print template


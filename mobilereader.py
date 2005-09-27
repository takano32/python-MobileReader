#!/usr/bin/env python
# coding: euc-jp
# vim: fileencoding=euc-jp

import cgi

form = cgi.FieldStorage()
if form.has_key('inputname'):
  # inputname が指定されていたら、ご挨拶を表示
  inputname = form['inputname'].value
  print _output_form % inputname
else:
  # 入力フォームを表示
  print _input_form



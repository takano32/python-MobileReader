#!/usr/bin/env python
# coding: euc-jp
# vim: fileencoding=euc-jp

import cgi

form = cgi.FieldStorage()
if form.has_key('inputname'):
  # inputname �����ꤵ��Ƥ����顢��������ɽ��
  inputname = form['inputname'].value
  print _output_form % inputname
else:
  # ���ϥե������ɽ��
  print _input_form



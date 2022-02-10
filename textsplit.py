#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import re, sys
from xml.sax.saxutils import escape

text = sys.stdin.read()
separator = '/| |\n'

if len(sys.argv) > 1 and len(sys.argv[1]) > 0:
	separator = sys.argv[1]

if '\n' not in separator:
    separator += '|\n'

text_splited_array = re.split(separator, text)

output = """<?xml version="1.0"?><items>"""
for text_splited in text_splited_array:
  if text_splited:
    output += """
      <item arg="%(text_splited)s">
        <title>"%(text_splited)s"</title>
        <subtitle>"输入分隔符重新分割"</subtitle>
        <icon>icon.png</icon>
      </item>
    """ % {"text_splited": text_splited}
output += "</items>"

print output

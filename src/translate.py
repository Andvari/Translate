#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on Nov 24, 2012

@author: nemo
'''

import httplib

conn = httplib.HTTPConnection("translate.google.com")
conn.request("GET","/translate_a/t?client=t&text=mistress&hl=en&sl=auto&tl=ru&ie=UTF-8&oe=UTF-8&multires=1&otf=1&pc=1&ssel=0&tsel=0&uptl=ru&alttl=en&sc=1")
res = conn.getresponse()
print res.status, res.reason
data = res.read()

print data

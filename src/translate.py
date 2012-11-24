#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on Nov 24, 2012

@author: nemo
'''

import httplib
import re

term = "apple"

conn = httplib.HTTPConnection("translate.google.com")
#conn.request("GET","/translate_a/t?client=t&text=" + term + "&hl=en&sl=auto&tl=ru&ie=UTF-8&oe=UTF-8&multires=1&otf=1&pc=1&ssel=0&tsel=0&uptl=ru&alttl=en&sc=1")
conn.request("GET","/translate_a/t?client=t&text=" + term + "&hl=en&tl=ru&ie=UTF-8&oe=UTF-8") #&multires=1&otf=1&pc=1&ssel=0&tsel=0&uptl=ru&alttl=en&sc=1")
res = conn.getresponse()
print res.status, res.reason
data = res.read()

terms = re.compile('"(.*?)"').findall(data)

print terms[0]

#for term in terms:
#    print term.encode('utf-8')

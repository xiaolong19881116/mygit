#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for marisa_trie"

import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

s = []
with open("jhs_road.txt","r") as f:
    for line in f:
        s.append(unicode(line.strip()))

print s[0:10]
#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for urllib"
 
__author__ = 'mxl'

import urllib
f = urllib.urlopen("http://www.python.org")
with open("output.html",'w') as wf:
    wf.write(f.read())
print "done"
f.close()
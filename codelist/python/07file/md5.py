#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for md5"
 
__author__ = 'mxl'

import hashlib   
print hashlib.md5("abc").hexdigest()
print hashlib.md5("abc").hexdigest()
print hashlib.md5("abcd").hexdigest()
print hashlib.md5("abce").hexdigest()
print type(hashlib.md5("abce").hexdigest() )
print "-----------------------------------------"
with open("input.txt","r") as f:
    str = ''.join(f.readlines() )
    print hashlib.md5(str).hexdigest()

with open("output.txt","r") as f:
    str = ''.join(f.readlines() )
    print hashlib.md5(str).hexdigest()
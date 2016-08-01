#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module"
 
__author__ = 'mxl'

import sys
import os

debug = True 

class Foo(object):
    "Foo class"
    pass

def Func():
    "test function"
    foo = Foo()
    if debug:
        print "ran test()"

if __name__ == '__main__':
    Func()
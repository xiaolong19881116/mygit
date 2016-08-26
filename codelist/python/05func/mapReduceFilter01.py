#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for map reduce filter"
 
__author__ = 'mxl'

print map(str,range(10))
print map(lambda x:x+5,range(10))

print reduce(lambda x,y:x+y,range(1,101))

li = ['123','abc','23%*','12']

def func(y):
    return not y.isdigit()

print filter(lambda x:x.isdigit(),li)
print filter(func,li)
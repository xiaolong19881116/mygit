#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for Generator"
 
__author__ = 'mxl'

def odd(num):
    i = 1
    while i < num:
        yield i
        i = i + 2

g = odd(10)

for i in g:
    print i

mylist = [x for x in range(10)] #[]�����������б�

mygen = (x for x in range(10))  #()Բ��������Generator

print "mylist : ",mylist

print "mygen : ",mygen

print "use for :"
for i in mygen:
    print i
#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for classproperty"
 
__author__ = 'mxl'

class TestProperty(object):
    def __init__(self,v):
        self.__value = v
    def __getValue(self):
        return self.__value 
    def __setValue(self,v):
        self.__value = v
    Value = property(__getValue,__setValue)

test = TestProperty(5)
print test.Value
test.Value = 20
print test.Value
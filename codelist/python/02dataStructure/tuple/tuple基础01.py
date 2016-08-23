#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for tuple"
 
__author__ = 'mxl'

#元组的创建与删除
tuple_a = ('a',)
tuple_b = ('a','b','z','abc')
tuple_c = tuple('abc')
#元组是不可变序列，不能插入和删除元素，若删除只能删除整个元组
print tuple_a
print tuple_b
print tuple_c
#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for set"
 
__author__ = 'mxl'

#集合的创建与删除
set_a = {8,9,10,11,12,13}
set_b = set([0,1,2,3,7,8])
print set_a
print set_b
set_a.add(14)
print set_a
set_a.pop()
print set_a
set_a.add(8)
set_a.remove(14)
print set_a

#集合的操作
print set_a.union(set_b) #并集
print set_a&set_b        #交集
print set_a.intersection(set_b) #交集
print set_a.difference(set_b) #差集
print set_a.symmetric_difference(set_b) #对称差
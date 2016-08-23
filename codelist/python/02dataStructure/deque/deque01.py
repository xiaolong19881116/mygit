#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for deque"
 
__author__ = 'mxl'

from collections import deque

queue = deque([1,2,3,4])
print queue

queue.append(5)
print queue

queue.appendleft(0)
print queue

itm = queue.pop()
print itm
print queue

itm = queue.popleft()
print itm
print queue
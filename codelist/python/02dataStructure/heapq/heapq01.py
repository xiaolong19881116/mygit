#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for heapq"
 
__author__ = 'mxl'

import heapq
import random

data = range(10)
print data

print random.choice(data)
print random.choice(data)

random.shuffle(data)

print data

heap = []

for n in data:
    heapq.heappush(heap,n)

print "heap:",heap

heapq.heappush(heap,1)
print "now heap:",heap

min_itm = heapq.heappop(heap)
print min_itm
print heap

min_itm = heapq.heappop(heap)
print min_itm
print heap

another_heap = [1,2,3,5,7,8,9,4,10]
heapq.heapify(another_heap)
print another_heap
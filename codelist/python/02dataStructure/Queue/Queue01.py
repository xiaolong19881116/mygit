#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for Queue"
 
__author__ = 'mxl'

import Queue

myqueue = Queue.Queue()

myqueue.put(1)
myqueue.put(2)
myqueue.put(3)
myqueue.put(4)
print myqueue.queue

itm = myqueue.get()
print itm
print myqueue.queue

itm = myqueue.get()
print itm
print myqueue.queue

for i in range(10):
    print i,
#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for PriorityQueue"

import Queue

class Job(object):
    def __init__(self,priority,desc):
        self.priority = priority
        self.desc = desc

    def __cmp__(self,other):
        return cmp(self.priority,other.priority)

pq = Queue.PriorityQueue()
pq.put(Job(1,"A"))
pq.put(Job(3,"C"))
pq.put(Job(2,"B"))

re = pq.get()

print re.priority,re.desc

re = pq.get()

print re.priority,re.desc

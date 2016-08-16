#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for list"
 
__author__ = 'mxl'

import time
result = []
start = time.time()
for i in range(50000):
    result = result + [i]
print len(result),',',time.time() - start

result = []
start = time.time()
for i in range(50000):
    result.append(i)
print len(result),',',time.time() - start

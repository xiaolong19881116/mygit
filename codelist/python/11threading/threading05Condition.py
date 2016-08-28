#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for threading"
 
__author__ = 'mxl'

import threading
import time
def consumer(cond):
    with cond:
        print("consumer before wait")
        cond.wait()
        print("consumer after wait")
   
def producer(cond):
    with cond:
        print("producer before notifyAll")
        cond.notifyAll()
        print("producer after notifyAll")
   
condition = threading.Condition()
c1 = threading.Thread(name="c1", target=consumer, args=(condition,))
c2 = threading.Thread(name="c2", target=consumer, args=(condition,))
   
p = threading.Thread(name="p", target=producer, args=(condition,))
   
c1.start()
print "main."
time.sleep(2)
c2.start()
print "main.."
time.sleep(2)
p.start()
print "main..."
c1.join()
c2.join()
p.join()

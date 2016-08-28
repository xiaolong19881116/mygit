#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for threading"
 
__author__ = 'mxl'

import threading
import time 

def func(x,y):
    for i in range(x,y):
        print i
    time.sleep(8)
    print "**"

t1 = threading.Thread(target = func,args = (15,20))
t1.start()
t1.join(5)

t2 = threading.Thread(target = func,args = (5,10))
t2.start()
t2.join(5)

print "t1:",t1.isAlive()
print "t2:",t2.isAlive()
print threading.activeCount()

#def doWaiting():  
#    print 'start waiting1: ' + time.strftime('%H:%M:%S') + "\n"  
#    time.sleep(3)  
#    print 'stop waiting1: ' + time.strftime('%H:%M:%S') + "\n" 
#def doWaiting1():  
#    print 'start waiting2: ' + time.strftime('%H:%M:%S') + "\n"   
#    time.sleep(8)  
#    print 'stop waiting2: ', time.strftime('%H:%M:%S') + "\n"  
#tsk = []    
#thread1 = threading.Thread(target = doWaiting)  
#thread1.start()  
#tsk.append(thread1)
#thread2 = threading.Thread(target = doWaiting1)  
#thread2.start()  
#tsk.append(thread2)
#print 'start join: ' + time.strftime('%H:%M:%S') + "\n"   
#for tt in tsk:
#    tt.join() #join的作用是阻塞主线程，不带参数等待所有线程结束再执行主线程
#    #tt.join(2) #仅仅等待线程2秒之后，就不管了，直接执行主线程
#print 'end join: ' + time.strftime('%H:%M:%S') + "\n"
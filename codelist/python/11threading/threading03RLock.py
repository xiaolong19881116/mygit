#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for threading"
 
__author__ = 'mxl'

import threading
import time 

globals_num = 0
   
lock = threading.RLock()
   
def Func():
    lock.acquire()  # �����
    global globals_num
    globals_num += 1
    time.sleep(1)
    print(globals_num)
    lock.release()  # �ͷ���
   
for i in range(10):
    t = threading.Thread(target=Func)
    t.start()
    t.join()

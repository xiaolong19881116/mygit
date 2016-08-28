#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for threading"
 
__author__ = 'mxl'

import threading
import time 


def music(s):
    print s,time.strftime('%H:%M:%S')
    time.sleep(2)
    print s,time.strftime('%H:%M:%S')

def movie(m):
    print m,time.strftime('%H:%M:%S')
    time.sleep(5)
    print m,time.strftime('%H:%M:%S')

t1 = threading.Thread(target = music,args = ("try",))
t2 = threading.Thread(target = movie,args = ("TARZAN",))

# ͬʱִ��main�����߳�
print "Main..",time.strftime('%H:%M:%S')
#t1.start()
#t2.start()

#����main
#t1.start()
#t2.start()
#t1.join()
#t2.join()

#����main 2s
#t1.start()
#t2.start()
#t1.join(2)
#t2.join(2)

#���߳̽������ӽ���Ҳ����
t1.setDaemon(True)
t2.setDaemon(True)
t1.start()
t2.start()
#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for threading"
 
__author__ = 'mxl'

import threading
   
def do(event):
    print('start')
    event.wait() #�ȴ�eventΪ����߳�ʱ
    print('execute')
   
event_obj = threading.Event()
for i in range(10):
    t = threading.Thread(target=do, args=(event_obj,))
    t.start()
   
event_obj.clear() #����Ϊ��
inp = raw_input('input:')
if inp == 'true':
    event_obj.set() #���߳�����Ϊ��
#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for Binaryfile"
 
__author__ = 'mxl'

import pickle

'''
���ݿ��ļ���ͼ���ļ�����ִ���ļ�����Ƶ�ļ���office�ĵ����ļ����Ƕ������ļ�
���л�����ָ���ڴ��е������ڲ���ʧ����Ϣ�������ת�ɶ���Ķ�������ʽ�ı�ʾ����
'''
f = open("BinaryFile.dat",'wb')
n = 6
i = 1000
a =99.999
s = "�й�123abc"
li = [[1,2],[3,4]]
tu = (2,3,4,5)
dic = {'a':12,'b':13}

try:
    pickle.dump(n,f)
    pickle.dump(i,f)
    pickle.dump(a,f)
    pickle.dump(s,f)
    pickle.dump(li,f)
    pickle.dump(tu,f)
    pickle.dump(dic,f)
except:
    print "д�ļ��쳣"
finally:
    f.close()

f2 = open("BinaryFile.dat","rb")
n = pickle.load(f2)   #�����ļ����ݸ���
i = 0
print n
while i < n:
    x = pickle.load(f2)
    print x
    i = i + 1
f2.close()

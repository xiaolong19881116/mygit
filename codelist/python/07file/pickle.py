#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for Binaryfile"
 
__author__ = 'mxl'

import pickle

'''
数据库文件，图像文件，可执行文件，音频文件和office文档等文件都是二进制文件
序列化：是指把内存中的数据在不丢失其信息的情况下转成对象的二进制形式的表示过程
'''
f = open("BinaryFile.dat",'wb')
n = 6
i = 1000
a =99.999
s = "中国123abc"
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
    print "写文件异常"
finally:
    f.close()

f2 = open("BinaryFile.dat","rb")
n = pickle.load(f2)   #读出文件数据个数
i = 0
print n
while i < n:
    x = pickle.load(f2)
    print x
    i = i + 1
f2.close()

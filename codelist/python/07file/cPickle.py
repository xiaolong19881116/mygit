#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for cPickle"
 
__author__ = 'mxl'

import cPickle

'''
cPickle��pickle��һ�������C���Ա���汾
'''

#���л����ļ�
obj = 123,99.99,[1,2,3],('a','b'),{'a':34,'b':45}
print obj
f = open("BinaryFile.dat","wb")
cPickle.dump(obj,f)
f.close()
#��ȡ���л��ļ�
f = open("BinaryFile.dat","rb")
obj1 = cPickle.load(f)
print obj1

#���л����ڴ�
obj2 = cPickle.dumps(obj)
print "type of obj2:",type(obj2)
print "obj2:",obj2

obj3 = cPickle.loads(obj2)
print "type of obj3:",type(obj3)
print "obj3:",obj3
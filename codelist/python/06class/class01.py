#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for class"
 
__author__ = 'mxl'

#������ԣ���Ϊ�����Ժ�ʵ������
class Car:
    price = 100000 #������
    def __init__(self,c):
        self.color = c #ʵ������,����
        self.__value = 12 #ʵ������,˽��
        self._isNew = True #ʵ������,������ ���������Է���

car1 = Car("red")
car2 = Car("blue")
print "car1 :",car1.price,car1.color,car1._isNew,Car.price
print "car2 :",car2.price,car2.color,car2._isNew,Car.price
Car.price = 111
print "car1 :",car1.price,car1.color,car1._isNew,Car.price
print "car2 :",car2.price,car2.color,car2._isNew,Car.price

#˽��Ҳ���Է���
print car1._Car__value #ͨ��������._����__xxx

#��ķ���
'''
��ķ�����4�ࣺ���з�����˽�з������෽������̬����
���з�����˽�з������ڶ��󣬿��Է��ʶ������ĳ�Ա
�෽���;�̬���������ֻ࣬�ܷ������Ա
'''

class Root:
    __total = 0  #˽�����Ա
    def __init__(self,v):
        self.__value = v #˽�ж����Ա
        Root.__total += 1
    def show(self):      #���з���
        print "self.__value",self.__value
        print "Root.__total",Root.__total
    @classmethod 
    def calssShow(cls): #�෽��
        print cls.__total
    @staticmethod
    def staticShow(): #��̬����
        print Root.__total

r = Root(3)
r.show()
Root.calssShow()
Root.staticShow()

rr = Root(30)
rr.show()
Root.calssShow()
Root.staticShow()
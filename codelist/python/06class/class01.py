#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for class"
 
__author__ = 'mxl'

#类的属性，分为类属性和实例属性
class Car:
    price = 100000 #类属性
    def __init__(self,c):
        self.color = c #实例属性,公有
        self.__value = 12 #实例属性,私有
        self._isNew = True #实例属性,保护型 类和子类可以访问

car1 = Car("red")
car2 = Car("blue")
print "car1 :",car1.price,car1.color,car1._isNew,Car.price
print "car2 :",car2.price,car2.color,car2._isNew,Car.price
Car.price = 111
print "car1 :",car1.price,car1.color,car1._isNew,Car.price
print "car2 :",car2.price,car2.color,car2._isNew,Car.price

#私有也可以访问
print car1._Car__value #通过对象名._类名__xxx

#类的方法
'''
类的方法有4类：公有方法，私有方法，类方法，静态方法
公有方法，私有方法属于对象，可以访问对象和类的成员
类方法和静态方法属于类，只能访问类成员
'''

class Root:
    __total = 0  #私有类成员
    def __init__(self,v):
        self.__value = v #私有对象成员
        Root.__total += 1
    def show(self):      #公有方法
        print "self.__value",self.__value
        print "Root.__total",Root.__total
    @classmethod 
    def calssShow(cls): #类方法
        print cls.__total
    @staticmethod
    def staticShow(): #静态方法
        print Root.__total

r = Root(3)
r.show()
Root.calssShow()
Root.staticShow()

rr = Root(30)
rr.show()
Root.calssShow()
Root.staticShow()
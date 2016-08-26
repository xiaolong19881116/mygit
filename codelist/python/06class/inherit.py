#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for inherit"
 
__author__ = 'mxl'

class Person(object):
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def tell(self):
        print "name is %s,age is %d" % (self.__name,self.__age)

class Student(Person): #�̳�
    def __init__(self,name,age,score):
        Person.__init__(self,name,age)  #���๹�캯��
        self.__score = score
    def tell(self):
        super(Student, self).tell() # ���ø��ຯ��
        print "score is %f" %self.__score
        Person.tell(self) # ���ø��ຯ��

stu1 = Student("xiaolong",28,98.5)
stu2 = Student("yayay",26,99)

stus = [stu1,stu2]

for stu in stus:
    stu.tell()
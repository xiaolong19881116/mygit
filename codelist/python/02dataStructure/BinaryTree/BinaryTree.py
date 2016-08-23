#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for BinaryTree"
 
__author__ = 'mxl'

class BinaryTree:
    def __init__(self,value):
        self.__left = None
        self.__right = None
        self.__value = value
    def insertLeft(self,value):
        if self.__left:
            print "left child is already exists"
        else:
            self.__left = BinaryTree(value)
            return self.__left
    def insertRight(self,value):
        if self.__right:
            print "right child is already exists"
        else:
            self.__right = BinaryTree(value)
            return self.__right
    def show(self):
        print self.__value
    def preOrder(self):
        print self.__value
        if self.__left:
            self.__left.preOrder()
        if self.__right:
            self.__right.preOrder()
    def postOrder(self):
        if self.__left:
            self.__left.postOrder()
        if self.__right:
            self.__right.postOrder()
        print self.__value
    def inOrder(self):
        if self.__left:
            self.__left.inOrder()
        print self.__value
        if self.__right:
            self.__right.inOrder()
if __name__ == '__main__':
    print "Please use me as a module"
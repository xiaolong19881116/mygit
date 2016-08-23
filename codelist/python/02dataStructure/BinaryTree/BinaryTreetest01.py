#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for BinaryTree"
 
__author__ = 'mxl'

import BinaryTree
root = BinaryTree.BinaryTree('root')
root.show()

firstL = root.insertLeft('A')
firstR = root.insertRight('B')
secondL = firstL.insertLeft('C')
thirdR = secondL.insertRight('D')

root.preOrder()
print '-------------------------'

root.postOrder()
print '-------------------------'

root.inOrder()
print '-------------------------'
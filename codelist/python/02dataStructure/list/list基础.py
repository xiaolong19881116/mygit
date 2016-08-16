#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for list"
 
__author__ = 'mxl'

#列表的创建与删除
list_a = ['a','b','xyz']
#range(start,stop,step),start默认为0，stop(结果中不包含这个值)，步长默认为1
list_b = range(2,11,2) 
print list_b
#删除列表
del list_a

#列表元素的增加与删除
list_b = list_b + [12] #该方式会创建一个新的列表返回
print list_b
list_b.append(14) #真正意义上的在尾部添加元素，在原地址修改列表，速度快，推荐使用
print list_b
list_b.extend([16,18]) #同样extend方法也是原地操作
print list_b
list_b.insert(3,30) #在指定位置添加元素
print list_b
print list_b[0] #访问第一个元素
print list_b[1] #访问第二个元素
print list_b[-1] #访问最后一个元素

del list_b[3] #删除指定位置上的元素
print list_b
list_b.pop(2) #删除指定位置上的元素,默认最后一个
print list_b
list_b.pop()
print list_b

list_c = [1,1,23,568,88,88,12,0,88]
print list_c.count(88) #返回指定元素在列表中出现的次数
print list_c
list_c.remove(88) #删除首次出现的指定元素
print list_c
print list_c.count(88) #返回指定元素在列表中出现的次数

print 23 in list_c #成员资格判断
print 13 in list_c

#列表排序
list_d = [3,4,5,6,7,9,11,13,15,17,19,23]
import random
random.shuffle(list_d) #打乱顺序,直接操作列表
print list_d

list_d.sort() #默认升序排列
print list_d
list_d.sort(reverse = True)
print list_d
list_d.sort(key = lambda x:len(str(x))) #自定义排序
print list_d

'''
内置函数sorted()对列表进行排序，与列表对象的sort()方法不同，
该函数返回新的列表，不对原列表进行任何修改
同样
内置函数reversed()对列表进行逆序,返回一个逆序后的迭代对象，与列表对象的reverse()方法不同，
该函数返回新的列表，不对原列表进行任何修改
'''
alist = [1,3,7,5,4]
print sorted(alist)
print alist
print reversed(alist)
print list(reversed(alist) )
print alist

#常用函数
'''
zip
'''
alist = [1,2,3]
blist = [4,5,6]
clist = [7,8,9]
dlist = zip(alist,blist,clist)#将列表或元组对应位置元素组合成元组，并返回包含这些元组的列表
print dlist

'''
enumerate 返回下标和元素值的元组
'''
alist = ['a','b','c']
for index,value in enumerate(alist):
    print index,value

'''
 列表推导式
'''

print [x**2 for x in range(2,11,2)]
print [x+y for x in 'ABC' for y in 'ABC']
print [(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]


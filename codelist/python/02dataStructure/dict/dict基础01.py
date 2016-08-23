#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for dict"
 
__author__ = 'mxl'

#字典的创建与删除
dict_a = {'a':1,'b':2,'c':3}
keys = ['a','b','c','d']
values = [1,2,3,4]
dict_b = dict(zip(keys,values))
dict_c = dict(name = 'xiaolong',age = 28)
print dict_a
print dict_b
print dict_c

#字典元素的获取
print dict_c['name'] #使用下标，若下标不存在，抛出异常
print dict_c.get('addr') #不存在，默认返回None
print dict_c.get('addr','China') #不存在返回指定值
print dict_c.get('age','China')

#读取方式
for item in dict_c.items():
    print item 

for key,value in dict_c.items():
    print key,value

print dict_c.keys()
print dict_c.values()

#字典的操作，指定键值为字典元素赋值时，若该键值存在则更新该键对应的值，若不存在则创建新的键值对
dict_c['age'] = 29
dict_c['addr'] = 'China.HZ'
print dict_c

#使用update方法将一个字典的元素全部添加到当前字典
print dict_a
print dict_c
dict_c.update(dict_a)
print dict_c
#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for BinaryTree"
 
__author__ = 'mxl'

import types

#字符串类型
s = "Hello World"
print type(s)
print type(s) == types.StringType

s2 = u"Hello World"
print type(s2)
print type(s2) == types.UnicodeType

s3 = 5
print type(s3)
print type(s3) == types.IntType

s4 = 5.0
print type(s4)
print type(s4) == types.FloatType

f = lambda x:x**2
print type(f)
print type(f) == types.FunctionType

print "----------------------------------------------------"

#格式化字符串
'''
'% [-] [+] [0] [m] [.n] 格式化字符 '% x
[-]:左对齐
[+]:右对齐
[0]:填充字符
[m]:指定最小宽度
[.n]:指定精度
格式化字符：%s,%b,%d,%o,%x,%e,%f,%%(字符%)
'''
print "%d"%123
print "%o"%123
print "%x"%123
print "%3.2e"%123
print "%3.2f"%123

name1 = "xiaolong"
age1 = 28
qq1 = [123,678]
print "my name is {name},my QQ is {qq},my age is {age}".format(name=name1,qq=qq1,age=age1)

#常用的字符串方法
s = "apple,peach,pear"
print s.find("peachs") #自定字符串中查找子串第一次出现的位置, 不存在返回-1
li = s.split(",") #分隔成列表
print li
sep = "*"
print sep.join(li) # 将列表链接起来

print s
print s.upper()
print s
print s.lower()
print s
print s.title()
print s
print s.replace("a","**") # 使用**替换所有a
s = "  "+ s+ "  "
print s
print s.strip() #去除左右空白字符

print "----------------------------------------------------"

import string
table = string.maketrans("abc","@#&") #生成映射表
str = "abheloacbzate"
print str
print str.translate(table) #按照对应关系进行替换

print "----------------------------------------------------"

print string.digits
print string.punctuation
print string.printable
print string.lowercase
print string.uppercase
print string.letters

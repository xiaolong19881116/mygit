#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for BinaryTree"
 
__author__ = 'mxl'

import types

#�ַ�������
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

#��ʽ���ַ���
'''
'% [-] [+] [0] [m] [.n] ��ʽ���ַ� '% x
[-]:�����
[+]:�Ҷ���
[0]:����ַ�
[m]:ָ����С���
[.n]:ָ������
��ʽ���ַ���%s,%b,%d,%o,%x,%e,%f,%%(�ַ�%)
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

#���õ��ַ�������
s = "apple,peach,pear"
print s.find("peachs") #�Զ��ַ����в����Ӵ���һ�γ��ֵ�λ��, �����ڷ���-1
li = s.split(",") #�ָ����б�
print li
sep = "*"
print sep.join(li) # ���б���������

print s
print s.upper()
print s
print s.lower()
print s
print s.title()
print s
print s.replace("a","**") # ʹ��**�滻����a
s = "  "+ s+ "  "
print s
print s.strip() #ȥ�����ҿհ��ַ�

print "----------------------------------------------------"

import string
table = string.maketrans("abc","@#&") #����ӳ���
str = "abheloacbzate"
print str
print str.translate(table) #���ն�Ӧ��ϵ�����滻

print "----------------------------------------------------"

print string.digits
print string.punctuation
print string.printable
print string.lowercase
print string.uppercase
print string.letters

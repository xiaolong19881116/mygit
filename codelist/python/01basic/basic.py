#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for basic"
 
__author__ = 'mxl'

"function type()"
int_x = 3
float_x = 1.2
str_x = "123.456"
list_x = [1,2,3]
print "type int_x is ",type(int_x)
print "type float_x is ",type(float_x)
print "type str_x is ",type(str_x)
print "type list_x is ",type(list_x)

print "--------------------------------------------"

"function id()"
x = 3
y = 3
print "id(x) is ",id(x)
print "id(y) is ",id(y)

print "--------------------------------------------"

"��ʽ���ַ���"
a = 3.6674
str_a1 = "%10.3f" % a
str_a2 = "%-10.3f" % a
print str_a1
print str_a2

print "--------------------------------------------"

# תΪ������
''' 
0x��ͷ --> ʮ������
0o��ͷ --> �˽���
0b��ͷ --> ������ 
'''
print bin(10)
print oct(10)
print hex(10)

print "--------------------------------------------"

#�������ض���
#fp = open(r"output.txt","a+")
#print >>fp,"Hello World !!"
#fp.close()

print "--------------------------------------------"
''' 
����ģ��ʱ�����ڵ�ǰĿ¼�в�����Ҫ�����ģ�飬���û���ҵ���
��sysģ���path������ָ���Ŀ¼�в��ң������û���ҵ�����ʾģ�鲻����
Ҳ����ʹ��append()������path������Զ���Ŀ¼����չ����·��
'''
import keyword
import sys 
import random

print keyword.kwlist
print sys.path

list_a = [random.randint(1,100) for i in range(10)]
print list_a
y = sorted(list_a)
print y
print "(max,min,sum,avg) : ", (max(list_a),min(list_a),sum(list_a),sum(list_a)*1.0/len(list_a))

print "--------------------------------------------"

#python �ļ���
''' 
(1).py:PythonԴ�ļ�����python�������������ִ��
(2).pyw:pythonԴ�ļ���������ͼ�ν�������ļ�
(3).pyc:python�ֽ����ļ����޷�ʹ�ñ༭�������鿴�ļ����ݣ�����pythonģ�飬��һ�ε���ʱ���������
        �ֽ�����ʽ���������Ժ��ٴε���ʱ����ʹ��pyc�ļ��������ģ��ļ��غ������ٶȡ����ڷ�ģ���ļ�
        ֱ��ִ��ʱ������pyc�ļ������ǿ���ʹ��py_compileģ���compile()�������б��룬����߼���
        �������ٶ�
(4).pyo:�Ż���python�ֽ����ļ����޷�ʹ�ñ༭�������鿴�ļ�����
        ����ʹ�ã�python -O -m py-compile file.py�����Ż�
(5).pyd:һ�����������Ա�д������Ķ������ļ���������ʵ��ĳЩ������ߵ�python��̽ӿڻ�python��̬���ӿ�
'''

print "--------------------------------------------"

#��д�Լ��İ�
''' 
����python������֯�����ռ����ķ�ʽ�����Կ�������python����ģ����ļ��У���ÿһ��Ŀ¼�б������һ��
__init__.py�ļ������ļ�����Ϊ�գ������ڱ�ʾ��Ŀ¼��һ������__init__.py�ļ�����Ҫ��;������
__all__�����Լ�ִ�г�ʼ��������Ҫ�Ĵ��룬����__all__�����ж���Ķ�������� from ... import *
ʱȫ����ȷ���롣
��ʾ����

sound/
    __init__.py
    effects/
        __init__.py
        echo.py
        curl.py
    filters/
        __init__.py
        coder.py
        karade.py
        ...
'''

#python ָ�� import this 
s = ''' 
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

print s

raw_input()





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

"格式化字符串"
a = 3.6674
str_a1 = "%10.3f" % a
str_a2 = "%-10.3f" % a
print str_a1
print str_a2

print "--------------------------------------------"

# 转为二进制
''' 
0x打头 --> 十六进制
0o打头 --> 八进制
0b打头 --> 二进制 
'''
print bin(10)
print oct(10)
print hex(10)

print "--------------------------------------------"

#结果输出重定向
#fp = open(r"output.txt","a+")
#print >>fp,"Hello World !!"
#fp.close()

print "--------------------------------------------"
''' 
导入模块时首先在当前目录中查找需要导入的模块，如果没有找到则
从sys模块的path变量所指向的目录中查找，如果仍没有找到则提示模块不存在
也可以使用append()方法向path中添加自定义目录来扩展搜索路径
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

#python 文件名
''' 
(1).py:Python源文件，由python解释器负责解释执行
(2).pyw:python源文件，常用于图形界面程序文件
(3).pyc:python字节码文件，无法使用编辑器正常查看文件内容，对于python模块，第一次导入时将被编译成
        字节码形式，并且在以后再次导入时优先使用pyc文件，以提高模块的加载和运行速度。对于非模块文件
        直接执行时不生成pyc文件，但是可以使用py_compile模块的compile()函数进行编译，以提高加载
        和运行速度
(4).pyo:优化的python字节码文件，无法使用编辑器正常查看文件内容
        可以使用：python -O -m py-compile file.py进行优化
(5).pyd:一般由其他语言编写并编译的二进制文件，常用于实现某些软件工具的python编程接口或python动态链接库
'''

print "--------------------------------------------"

#编写自己的包
''' 
包是python用来组织命名空间和类的方式，可以看做包是python程序模块的文件夹，在每一个目录中必须包含一个
__init__.py文件，该文件可以为空，仅用于标示该目录是一个包，__init__.py文件的主要用途是设置
__all__变量以及执行初始化包所需要的代码，其中__all__变量中定义的对象可以在 from ... import *
时全部正确导入。
包示例：

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

#python 指禅 import this 
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




